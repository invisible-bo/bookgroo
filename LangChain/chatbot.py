from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 모델 불러오기
model = ChatOpenAI(model="gpt-4o-mini")

# embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# ChromaDB
chroma_db = Chroma(persist_directory="../ChromaDB", embedding_function=embeddings)

# retriever
retriever = chroma_db.as_retriever()

# 프롬프트
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            """
        당신은 도서 추천 시스템입니다. 다음과 같은 규칙을 따라 주세요.
        1. 사용자의 입력을 아래 세 가지 카테고리로 분류해주세요.
        - off_topic: 도서 추천과 관련 없는 질문
        - no_keyword: 사용자의 기분이나 원하는 것에 대한 맥락 없이 책을 추천해달라는 경우
        - yes_keyword: 사용자의 기분이나 원하는 것에 대한 맥락이 있고 이에 따른 책을 추천해달라는 경우
        2. 각 카테고리 별로 다음과 같이 작동해주세요
        - off_topic: 책 추천과 관련된 질문을 해달라고 답변을 해주세요
          off_topic 예시 1
          질문 1: 아무책이나 추천해줘
          답변 1: 평소에 선호하시던 장르에 한해서 추천해드릴까요?
         
          질문 2: 아니 그냥 아무거나 추천해줘
          답변 2:
         
          off_topic  2
          질문 1: 졸리다
          답변 1: 졸릴 때 책을 읽으면 잠이 덜 오는 경우가 있어요. 책을 추천해드릴까요?
          
          질문 2: 아니 그냥 졸려
          답변 2: 저는 책을 추천해주는 챗봇입니다. 다른 컨텐츠에 대해서는 답변이 어려워요.
          
        - yes_keyword: 사용자의 입력 값에서 유의미한 키워드를 추출해 이를 바탕으로 추천
        3. LLM 모델이 가진 책 정보들에서 한권, chromaDB에서 retrieve 1권해서 총 2권을 추천해줘. 그리고 각각 LLM 모델 데이터인지, RAG데이터 출처인지도 알려줘.
        4. 추천 시 반드시 포함해야할 정보
        - 정보 출처
        - 책 제목
        - 저자
        - 출판사
        - 추천 이유 (키워드 또는 장르와의 연관성 등 구체적인 설명을 넣어줘)
        """
        ),
        HumanMessagePromptTemplate.from_template(
            """
        Question: {question}
        Context: {context}
        Answer: """
        ),
    ]
)


def get_rag_response(question):
    """
    잘뮨울 받아서 RAG 방식으로 응답하는 함수

    이 함수는 주어진 질문을 기반을 벡터 데이터베이스에서 연관있는 내용을 가져와서,
    이를 기반으로 LLM 모델을 통해 최종 응답을 생성.

    question: str
        사용자가 입력한 질문

    return: str
        RAG 기반으로 LLM이 생성한 응답
    """
    # 벡터 DB에서 관련 문서 검색
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    # RAG 실행
    chain = prompt | model
    response = chain.invoke({"context": context, "question": question})

    return response.content
