from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
import os

# 크롤링한 데이터 경로 및 ChromaDB 경로 설정
CSV_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "../crawling/result_final_with_genres_test.csv"
)
CHROMA_DB_DIR = os.path.join(os.path.dirname(__file__), "../chromaDB")


def store_chroma_db():
    """
    크롤링한 csv 데이터를 load해서 벡터 데이터베이스(ChromaDB)에 저장하는 함수.

    1. csv 문서 불러옴
    2. 문서를 작은 덩어리로 만듦 (Chunking)
    3. text-embedding-3-small (OpenAI)를 이용해서 작은 덩이리 텍스트를 벡터로 변환
    4. ChromaDB에 저장
    """
    # 크롤링 데이터 load
    loader = CSVLoader(file_path=CSV_FILE_PATH)
    data = loader.load()

    # Chunking
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_texts = text_splitter.split_documents(data)

    # embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # VectorDB에 저장
    chroma_db = Chroma.from_documents(
        documents=split_texts,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR,
    )

    print("DB에 저장했음")
    return chroma_db


def get_chroma_db():
    """
    ChromaDB 데이터를 불러오는 함수
    """
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    chroma_db = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)
    return chroma_db
