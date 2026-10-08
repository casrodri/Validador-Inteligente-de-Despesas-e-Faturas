import os
from typing import TypedDict, Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
from schemas import Despesa


load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0
)

class EstadoDespesa(TypedDict):
    texto_entrada: str
    dados_despesa: Optional[Despesa]

def extrair_despesa(state: EstadoDespesa):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "És um assistente financeiro direto e conciso. Extrai os dados da despesa do texto fornecido."),
        ("user", "{texto}")
    ])
    chain = prompt | llm.with_structured_output(Despesa)
    resultado = chain.invoke({"texto": state["texto_entrada"]})
    return {"dados_despesa": resultado}

def validar_regras(state: EstadoDespesa):
    despesa = state["dados_despesa"]
    limites = {
        "refeicao": 40.0,
        "transporte": 60.0,
        "alojamento": 150.0
    }
    limite_categoria = limites.get(despesa.categoria.lower(), 20.0)
    
    if despesa.valor <= limite_categoria:
        despesa.status = "Aprovado"
        despesa.motivo = f"Valor abaixo do limite ({limite_categoria}€)."
    else:
        despesa.status = "Pendente de Revisão Manual"
        despesa.motivo = f"Excede o limite automático de {limite_categoria}€."
        
    return {"dados_despesa": despesa}


workflow = StateGraph(EstadoDespesa)

workflow.add_node("extracao", extrair_despesa)
workflow.add_node("validacao", validar_regras)

workflow.set_entry_point("extracao")
workflow.add_edge("extracao", "validacao")
workflow.add_edge("validacao", END)

app = workflow.compile()