from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

####### Data Load
# loader = CSVLoader(file_path="./data/한국.csv", encoding='cp949')
loader = CSVLoader(file_path="./data/result.csv", encoding='utf-8')
whole_data = loader.load()

#### Split
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
split_data = splitter.split_documents(whole_data)

#### Embedding
embeddings = OpenAIEmbeddings()

#### Vector Store
vector_store = Chroma.from_documents(
    documents=split_data,
    embedding=embeddings,
    persist_directory="book_DB",
)