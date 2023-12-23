# import time
# import streamlit as st

# st.set_page_config(
#     page_title="DocumentGPT",
#     page_icon="📃",
# )

# st.title("Document GPT")

# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# def send_message(message, role, save=True) :
#     with st.chat_message(role) :
#         st.write(message)
#         # messages.append({"message": message, "role": role})
#     if save :
#         st.session_state["messages"].append({"message": message, "role": role})
#     # st.write(messages)

# # messages = []
# for message in st.session_state["messages"]:
#     send_message(message["message"], message["role"], save=False)


# # with st.chat_message("human") :
# #     st.write("Hellooooo")

# # with st.chat_message("ai") :
# #     st.write("How are you?")

# message = st.chat_input("Send a message to the ai")

# # with st.status("Embedding file...", expanded=True) as status :
#     # time.sleep(3)
#     # st.write("Getting the file")
#     # time.sleep(3)
#     # st.write("Embedding the file")
#     # time.sleep(3)
#     # st.write("Caching the file")
    
#     # status.update(label="Error", state="error")

# if message :
#     send_message(message, "human")
#     time.sleep(2)
#     send_message(f"You said : {message}", "ai")

#     with st.sidebar:
#         st.write(st.session_state)


### 7.6 Uploading Documents
import streamlit as st
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="📃",
)

st.title("Document GPT")

st.markdown('''
Welcome!
            
Use this chatbot to ask questions to an AI about your files!
''')

file = st.file_uploader(
    "Upload a .txt .pdf or .docx file", 
    type=["pdf", "txt", "docx"]
)

if file :
    st.write(file)

    file_content = file.read()
    file_path = f"./.cache/files/{file.name}"
    st.write(file_content, file_path)

    with open(file_path, "wb") as f :
        f.write(file_content)
    
    cache_dir = LocalFileStore(f"./.cache/embeddings/{file.name}")

    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )

    loader = UnstructuredFileLoader('./files/chapter_one.docx')
    docs = loader.load_and_split(text_splitter=splitter)
    embeddings = OpenAIEmbeddings()
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(
        embeddings,
        cache_dir
    )
    vectorstore = FAISS.from_documents(docs, cached_embeddings)
    retriever = vectorstore.as_retriever()

    docs = retriever.invoke("ministry of truth")

    st.write(docs)

