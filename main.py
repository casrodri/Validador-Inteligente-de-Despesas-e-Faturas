import os
from dotenv import load_dotenv
from agent_graph import app
from langfuse.langchain import CallbackHandler


load_dotenv()


langfuse_handler = CallbackHandler()

def processar_recibo(texto: str):
    print(f"\n--------------------------------------------------")
    print(f"A processar recibo: '{texto}'")
    print(f"--------------------------------------------------")
    
    estado_inicial = {"texto_entrada": texto, "dados_despesa": None}
    

    resultado = app.invoke(estado_inicial, config={"callbacks": [langfuse_handler]})
    
    despesa = resultado["dados_despesa"]
    print(f"🏢 Fornecedor: {despesa.fornecedor}")
    print(f"💰 Valor: {despesa.valor}€")
    print(f"📂 Categoria: {despesa.categoria}")
    print(f"📊 Status: {despesa.status}")
    print(f"💡 Motivo: {despesa.motivo}")

if __name__ == "__main__":

    processar_recibo("Gastei 32.50€ num jantar de negócios no restaurante O Pescador.")
    processar_recibo("Faturei 180€ de hotel na viagem de trabalho ao Porto.")