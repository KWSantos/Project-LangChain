import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from conversation_chain import conversation_chain
from pipeline_etl import extract, create_db
from retriever import retriever

def main():
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    
    model = "gemini-2.5-flash"
    llm = ChatGoogleGenerativeAI(model=model, google_api_key=google_api_key, temperature=0)

    data = extract()
    vectorstore = create_db(data)
    ensemble_retriever = retriever(vectorstore, data)
    qa_chain = conversation_chain(llm, ensemble_retriever)

    print("Sistema de Perguntas e Respostas está pronto para uso!")

    while True:
        question = input("Digite sua pergunta (ou 'sair' para encerrar): ")
        if question.lower() == 'sair':
            break

        response = qa_chain.invoke({"question": question})
        print("Resposta:", response['answer'])

if __name__ == "__main__":
    main()