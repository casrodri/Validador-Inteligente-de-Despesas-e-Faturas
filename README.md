# 🧾 Validador Inteligente de Despesas e Faturas

Sistema desenvolvido em **Python** para automatizar a extração, estruturação e validação de informações relacionadas a despesas e faturas a partir de **texto livre**.

A aplicação utiliza **LLMs**, **LangGraph** e **Pydantic** para transformar informações não estruturadas em dados estruturados, aplicar regras de negócio e determinar se uma despesa está dentro dos critérios definidos.

O projeto também utiliza **Langfuse** para observabilidade das execuções, permitindo acompanhar traces, latência e consumo de tokens durante o processamento.

---

## 🚀 Funcionalidades

* Extração automática de informações de despesas a partir de texto livre.
* Estruturação dos dados utilizando modelos definidos com **Pydantic**.
* Validação das informações extraídas.
* Aplicação de regras de negócio por categoria de despesa.
* Determinação automática do status da despesa.
* Orquestração do fluxo utilizando **LangGraph**.
* Integração com LLM através da **Groq API**.
* Monitoramento e rastreamento das execuções utilizando **Langfuse**.

---

## 🧠 Arquitetura

O projeto foi estruturado separando as responsabilidades entre entrada da aplicação, agente, modelos de dados e configurações.

```text
validador-despesas/
│
├── main.py              # Ponto de entrada e execução dos testes
├── agent_graph.py       # Grafo de execução e integração com a LLM
├── schemas.py           # Modelos e validações com Pydantic
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md             # Documentação
```

### 🔹 `main.py`

É o ponto de entrada da aplicação.

Responsável por executar os testes utilizando exemplos de despesas em texto livre e apresentar o resultado do processamento.

### 🔹 `agent_graph.py`

Contém a lógica principal do sistema.

Define o fluxo de processamento utilizando **LangGraph**, incluindo a comunicação com o modelo de linguagem e as etapas necessárias para estruturar e validar as informações recebidas.

### 🔹 `schemas.py`

Define os modelos de dados utilizando **Pydantic**.

Os schemas estabelecem uma estrutura esperada para as informações extraídas pela IA, permitindo validar os dados antes que sejam utilizados pelas demais etapas do sistema.

---

## 🔄 Fluxo da Aplicação

O processamento pode ser representado de forma simplificada:

```text
Texto da despesa
       │
       ▼
      LLM
       │
       ▼
Extração das informações
       │
       ▼
Validação com Pydantic
       │
       ▼
Regras de negócio
       │
       ▼
Status da despesa
       │
       ▼
Resultado estruturado
```

Durante esse processo, as execuções também podem ser acompanhadas através do **Langfuse**.

---

## 🛠️ Tecnologias

| Tecnologia      | Utilização                              |
| --------------- | --------------------------------------- |
| **Python**      | Linguagem principal                     |
| **LangChain**   | Integração com modelos de linguagem     |
| **LangGraph**   | Orquestração do fluxo de processamento  |
| **Pydantic**    | Estruturação e validação dos dados      |
| **Groq API**    | Inferência do modelo de linguagem       |
| **GPT-OSS-20B** | Modelo utilizado no processamento       |
| **Langfuse**    | Observabilidade e tracing das execuções |

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/casrodri/Validador-Inteligente-de-Despesas-e-Faturas.git
cd validador-despesas
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_da_groq

LANGFUSE_PUBLIC_KEY=sua_chave_publica
LANGFUSE_SECRET_KEY=sua_chave_secreta
LANGFUSE_HOST=https://cloud.langfuse.com
```

> **Importante:** não compartilhe suas chaves de API e não versione o arquivo `.env`. Certifique-se de que ele esteja incluído no `.gitignore`.

---

## 🚀 Executando o projeto

Com o ambiente virtual ativo e as variáveis de ambiente configuradas:

```bash
python main.py
```

O sistema irá processar exemplos de despesas em texto livre, extrair os dados relevantes, estruturar as informações e aplicar as regras de validação definidas no projeto.

---

## 📊 Observabilidade com Langfuse

O projeto utiliza **Langfuse** para acompanhar o comportamento das execuções envolvendo a LLM.

Entre as informações que podem ser analisadas estão:

* Traces das execuções;
* Etapas do processamento;
* Prompts enviados ao modelo;
* Respostas geradas;
* Latência das chamadas;
* Consumo de tokens;
* Informações relacionadas ao uso do modelo.

Essa camada de observabilidade facilita a análise e evolução de aplicações que utilizam modelos de linguagem.

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido como um estudo prático de conceitos relacionados a:

* Desenvolvimento de aplicações com **LLMs**;
* Engenharia de IA;
* Estruturação de dados gerados por modelos de linguagem;
* Validação de dados com **Pydantic**;
* Orquestração de fluxos com **LangGraph**;
* Implementação de regras de negócio;
* Observabilidade de aplicações de IA;
* Integração de APIs externas em aplicações Python.

---

## 📌 Possíveis evoluções

Algumas possibilidades para evolução do projeto:

* Adicionar novos tipos de despesas e regras de validação;
* Permitir o processamento de arquivos de notas fiscais;
* Criar uma interface web;
* Armazenar o histórico das despesas processadas;
* Adicionar testes automatizados;
* Implementar autenticação;
* Criar relatórios e métricas sobre as despesas;
* Adicionar suporte a diferentes modelos de linguagem.

---

## 👨‍💻 Autor

**Cássio Rodrigues**

Projeto desenvolvido como parte dos estudos práticos em **Python, Engenharia de IA, LLMs e desenvolvimento de software moderno**.
