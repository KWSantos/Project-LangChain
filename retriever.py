from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

def retriever(vectorstore, chunks, k = 5, wb = 0.4, wv = 0.6):
    bm25_retriever = BM25Retriever.from_documents(chunks)
    bm25_retriever.k = k

    vector_retriever = vectorstore.as_retriever(search_kwargs={"k" : k})

    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, vector_retriever],
        weights=[wb, wv]
    )

    print("Busca híbrida configurada")

    return ensemble_retriever