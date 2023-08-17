from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import GPT4All
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from pdf2image import convert_from_path
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("/home/user/ChatwithPDF/volsi.pdf") #Path to your PDF File
docs = loader.load()
documents = loader.load_and_split() 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64) 
texts = text_splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 
db = Chroma.from_documents(texts, embeddings, persist_directory="db")
retriever=db.as_retriever(search_kwargs={"k": 2})
model_n_ctx = 1000
model_path = "/home/user/ggml-gpt4all-j-v1.3-groovy.bin" #Path to where you downloaded the model using the follwoing link : https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin
llm = GPT4All(model=model_path, n_ctx=1000, backend="gptj",temp=0.1,verbose=False)
qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        verbose=False,
    )  
def generate_response(question):
    res=qa(question)
    return res
