# 🦜🔗 LangChain RAG Agent: Projeto de Estudo com Google Gemini

> Um assistente de conversação baseado em documentos (RAG), implementado com LangChain, Google Gemini e Busca Híbrida.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-v0.3-green)
![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![Status](https://img.shields.io/badge/Status-Educational-yellow)

## 📖 Sobre o Projeto

Este repositório é um **projeto pessoal de aprendizado** focado na exploração do framework **LangChain**. O objetivo principal foi construir uma aplicação de **RAG (Retrieval-Augmented Generation)** robusta, capaz de ler documentos PDF e responder a perguntas sobre eles com base em contexto, mantendo o histórico da conversa.

Diferente de implementações simples, este projeto explora conceitos avançados como **Busca Híbrida (Hybrid Search)** e persistência de memória conversacional.

### 🤔 O que é o LangChain?

Para quem está chegando agora: o **LangChain** é um framework poderoso projetado para simplificar o desenvolvimento de aplicações que utilizam Grandes Modelos de Linguagem (LLMs). Ele atua como uma "cola", permitindo conectar LLMs (como GPT ou Gemini) a fontes de dados externas (PDFs, Bancos de Dados, Web) e criar fluxos de trabalho complexos (Chains e Agentes).

---

## ⚙️ Arquitetura e Funcionalidades

O sistema foi modularizado em pipelines para facilitar o entendimento e a manutenção:

1.  **Ingestão de Dados (ETL):**
    * Carrega PDFs de um diretório local (`docs/`).
    * Realiza a quebra do texto em pedaços menores (Chunks) para otimizar o contexto.
    * Gera Embeddings utilizando o modelo do Google.
2.  **Armazenamento Vetorial:**
    * Utiliza o **ChromaDB** para armazenar os vetores semânticos dos documentos.
3.  **Retrieval (Recuperação) Híbrido:**
    * Este é o diferencial do projeto. Utilizamos um `EnsembleRetriever` que combina:
        * **Busca Semântica (Vector Store):** Entende o significado e o contexto da pergunta (peso 0.6).
        * **Busca por Palavras-chave (BM25):** Garante precisão em termos técnicos ou nomes específicos (peso 0.4).
4.  **Geração de Resposta:**
    * Utiliza o modelo **Google Gemini** (via API) para gerar respostas naturais baseadas nos documentos recuperados e no histórico da conversa.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **LangChain:** Orquestração do fluxo de IA.
* **Google Generative AI (Gemini):** LLM e Embeddings.
* **ChromaDB:** Banco de dados vetorial local.
* **Rank_BM25:** Algoritmo de busca baseada em frequência de termos.
* **Python-Dotenv:** Gerenciamento de variáveis de ambiente.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

* Python instalado.
* Uma API Key do Google AI Studio (Gemini).

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou
    venv\Scripts\activate     # Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Caso não tenha o arquivo requirements.txt, instale manualmente)*:
    ```bash
    pip install langchain langchain-community langchain-google-genai langchain-chroma chromadb rank_bm25 pypdf python-dotenv
    ```

4.  **Configure as Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave:
    ```env
    GOOGLE_API_KEY=sua_chave_aqui_cola_ela_inteira
    ```

5.  **Adicione seus Documentos:**
    Crie uma pasta chamada `docs` na raiz do projeto e coloque seus arquivos PDF lá.

6.  **Execute a Aplicação:**
    ```bash
    python main.py
    ```

---

## 📂 Estrutura de Arquivos

```text
📁 projeto/
│
├── 📄 main.py                 # Ponto de entrada (Entry point) da aplicação
├── 📄 pipeline_etl.py         # Carregamento de PDFs, Chunking e Criação do VectorDB
├── 📄 retriever.py            # Configuração da busca Híbrida (BM25 + Chroma)
├── 📄 conversation_chain.py   # Configuração da memória e da cadeia de conversação
├── 📄 .env                    # Arquivo de segredos (NÃO COMMITAR)
└── 📁 docs/                   # Coloque seus PDFs aqui
```
---

## 🧠 Aprendizados Chave

Durante o desenvolvimento deste projeto, foram consolidados os seguintes conhecimentos:
* Como estruturar um projeto de IA modular.
* A importância do **Chunking** correto para não estourar a janela de contexto do modelo.
* A diferença entre busca vetorial (significado) e busca lexical (palavra exata) e como a união das duas (**Hybrid Search**) melhora a precisão.
* Gerenciamento de memória em conversas contínuas com LLMs.

---

## 🤝 Contribuição

Sinta-se à vontade para fazer um fork deste projeto, abrir issues ou enviar Pull Requests. Este é um ambiente de aprendizado!

---

Desenvolvido por **Kauê Cruz** 🚀
