from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

def chatbot(user_question):
    load_dotenv()

    #### embeddings
    embeddings = OpenAIEmbeddings()

    #### vector store
    book_DB = Chroma(
        persist_directory="../book_DB",
        embedding_function=embeddings,
    )

    #### retriever
    retriever = book_DB.as_retriever()

    #### LLM
    llm = ChatOpenAI(model="gpt-4o-mini")
    
    #### prompt (gpt-4o 23년 10월)
    prompt_01 = ChatPromptTemplate.from_template(
            """
                Question: {user_question}
                Context: {context}
                Answer:
                
                - 상황 A : 기본
                    1. 당신은 책을 추천해주는 봇 입니다.
                    2. 모든 질문에 책을 추천할 필요는 없습니다. 사용자가 책 추천과 관련된 질문에 대해서만 책 추천을 진행하세요.
                    3. 사용자가 책 추천을 요청하지 않은 경우, 책 추천을 유도하세요.
                
                    예시 1
                        질문 1: 아무책이나 추천해줘
                        답변 1: 평소에 선호하시던 장르에 한해서 추천해드릴까요?
                        
                        질문 2: 아니 그냥 아무거나 추천해줘
                        답변 2: 상황 B 실행
                        
                    예시 2
                        질문 1: 졸리다
                        답변 1: 졸릴 때 책을 읽으면 잠이 덜 오는 경우가 있어요. 책을 추천해드릴까요?
                        
                        질문 2: 아니 그냥 졸려
                        답변 2: 저는 책을 추천해주는 챗봇입니다. 다른 컨텐츠에 대해서는 답변이 어려워요.
                        
                        질문 3 : 그냥 대화하는 기능은 없어?
                        답변 3 : 네 저는 책 추천만 해드릴 수 있습니다.
                        
                        질문 4 : 음.. 소설 아무거나 추천해줘
                        답변 4 : 상황 B 실행
                        
                    예시 3
                        질문 1: 뭐해
                        답변 1: 저는 사용자 분을 기다립니다. 책을 추천해드릴까요?
                        
                        질문 2: 그럼 판타지 책 추천해줘
                        답변 2: 상황 B 실행
                        
                    
                - 상황 B : 책 추천
                    1. 저자, 출판사, 출판일자 등 책에 대한 정보도 함께 제공해주세요.
                    2. 추천 A 타입에서 2권, 추천 B 타입에서 2권, 총 4권을 추천해주세요.
                    
                    
                - 추천 A 타입 :
                    1. context를 사용해서 책을 추천해주세요.
                    2. 첵 제목 옆에 RAG 태그를 붙여주세요.
                
                - 추천 B 타입 :
                    1. context를 사용하지 않고 책을 추천해주세요.
                    2. 첵 제목 옆에 LLM 태그를 붙여주세요.

                
            """
        )

# 3. 책 제목 옆에 context에서 검색된 책에는 RAG 태그, 사용하지 않은 책에는 LLM 태그를 붙여주세요.
    #### RAG
    retrieved_docs = retriever.invoke(user_question)
    context = "\n".join([doc.page_content for doc in retrieved_docs])
    
    ### chain
    chain = prompt_01 | llm
    res = chain.invoke({"context": context, "user_question": user_question})

    # chain = prompt_01 | llm
    # res = chain.invoke({"user_question": user_question})
    
    return res.content

user_question = "으어어어 재미없다"
# user_question = "음.. 그럼 판타지 장르의 책을 추천해줘"
bot_message = chatbot(user_question)
print(bot_message)

