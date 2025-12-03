from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def extract(directory = "docs/", chunk_size = 1500, chunk_overlap = 200, separators=None):
    if separators is None:
        separators = ["\n\n", "\n", ". ", " ", ""]

    loader = PyPDFDirectoryLoader(directory)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators= separators
    )

    chunks = text_splitter.split_documents(docs)

    print(f"Total de chunks criados = {len(chunks)}")

    return chunks

def create_db(chunks, model = "models/embedding-001"):
    embeddings_model = GoogleGenerativeAIEmbeddings(model=model)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings_model
    )

    print("Banco de dados criado com sucesso!")

    return vectorstore