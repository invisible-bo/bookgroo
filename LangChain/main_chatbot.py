from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

#### embeddings
embeddings = OpenAIEmbeddings()

#### vector store
book_DB = Chroma(
    persist_directory="book_DB",
    embedding_function=embeddings,
)

#### retriever
retriever = book_DB.as_retriever()

#### LLM
llm = ChatOpenAI(model="gpt-4o-mini")

#### prompt (gpt-4o 23년 10월)
prompt = ChatPromptTemplate.from_template(
    """
        1. 당신은 책을 추천해주는 봇 입니다.
        2. 검색된 context를 사용하여 질문에 답하세요.
        3. 책 추천이 아닌 다른 질문에 대해서는 답변하지 않고 사용자가 책 추천을 요청하도록 유도하세요.
        4. 책을 추천할때, 저자, 출판사, 출판일 등 책에 대한 정보도 함께 제공해주세요.
        
        예시 1
          질문 1: 아무책이나 추천해줘
          답변 1: 평소에 선호하시던 장르에 한해서 추천해드릴까요?
         
          질문 2: 아니 그냥 아무거나 추천해줘
          답변 2:
         
        예시 2
          질문 1: 졸리다
          답변 1: 졸릴 때 책을 읽으면 잠이 덜 오는 경우가 있어요. 책을 추천해드릴까요?
          
          질문 2: 아니 그냥 졸려
          답변 2: 저는 책을 추천해주는 챗봇입니다. 다른 컨텐츠에 대해서는 답변이 어려워요.
          
         

        Question: {user_question}
        Context: {context}
        Answer:
    """
)

prompt_none_context = ChatPromptTemplate.from_template(
    """
        1. 당신은 책을 추천해주는 봇 입니다.
        2. 검색된 context를 사용하여 질문에 답하세요.
        3. 책 추천이 아닌 다른 질문에 대해서는 답변하지 않고 사용자가 책 추천을 요청하도록 유도하세요.
        4. 책을 추천할때, 저자, 출판사, 출판일 등 책에 대한 정보도 함께 제공해주세요.

        Question: {user_question}
        Answer:
    """
)

#### question
user_question = "우울한데 내 기분을 좀 나아지게 해줄 책 있어?"
print(f"질문: {user_question}")

#### RAG
retrieved_docs = retriever.invoke(user_question)
context = "\n".join([doc.page_content for doc in retrieved_docs])

#### chain
# chain = prompt | llm
# res = chain.invoke({"context": context, "user_question": user_question})
# print(f"답변: {res.content}")

chain = prompt_none_context | llm
res = chain.invoke({"user_question": user_question})
print(f"답변: {res.content}")

