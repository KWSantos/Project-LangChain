from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def conversation_chain(llm, ensemble_retriever):
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        return_messages=True
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=ensemble_retriever,
        memory=memory,
        verbose=False,
        return_source_documents=True
    )

    return qa_chain