from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv


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
    prompt_A = ChatPromptTemplate.from_template(
        """
            Question: {user_question}
            Context: {context}
            Answer:
                
            - 상황 A : 기본
                1. 당신은 책을 추천해주는 봇 입니다.
                2. 모든 질문에 책을 추천할 필요는 없습니다. 사용자가 추천을 요청한 경우 책 추천을 진행하세요.
                3. 사용자가 책 추천을 요청하지 않은 경우, 책 추천을 유도하세요.
                4. 사용자의 질문은 제거 해주세요.
                5. context 안에서 책을 검색해서 추천해주세요.
            
            
                예시 1
                    질문 1: 아무책이나 추천해줘
                    답변 1: 상황 B 실행
                    
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
                    
                예시 5
                    질문 1: 문학 추천해줘
                    답변 1: 상황 B 실행
                    
                예시 6
                    질문 1: 뭐 재밌는거 없나?
                    답변 1: 재밌는 책을 추천해드릴까요?
                    
                    질문 2: 추천해줘
                    답변 2: 상황 B 실행
                    
                    
            - 상황 B : 책 추천
                1. 저자, 출판사, 출판일자 등 책에 대한 정보도 함께 제공해주세요.
                2. 책 제목 옆에 RAG 태그를 붙여주세요.
                3. 2권 추천해주세요.
                
        """)

    prompt_B = ChatPromptTemplate.from_template(
        """
            Question: {user_question}
            Answer:
                
            - 상황 A : 기본
                1. 당신은 책을 추천해주는 봇 입니다.
                2. 모든 질문에 책을 추천할 필요는 없습니다. 사용자가 추천을 요청한 경우 책 추천을 진행하세요.
                3. 사용자가 책 추천을 요청하지 않은 경우, 책 추천을 유도하세요.
                4. 사용자의 질문은 제거 해주세요.
            
            
                예시 1
                    질문 1: 아무책이나 추천해줘
                    답변 1: 상황 B 실행
                    
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
                    
                예시 5
                    질문 1: 문학 추천해줘
                    답변 1: 상황 B 실행
                    
                예시 6
                    질문 1: 뭐 재밌는거 없나?
                    답변 1: 재밌는 책을 추천해드릴까요?
                    
                    질문 2: 추천해줘
                    답변 2: 상황 B 실행
                    
                    
            - 상황 B : 책 추천
                1. 저자, 출판사, 출판일자 등 책에 대한 정보도 함께 제공해주세요.
                2. 책 제목 옆에 LLM 태그를 붙여주세요.
                3. 2권 추천해주세요.
                
        """)
    
    prompt_C = ChatPromptTemplate.from_template(
        """
            result_RAG : {result_RAG}
            result_LLM : {result_LLM}
            Answer:
                
            1. 당신은 추천 결과들을 취합하는 텍스트 편집 봇 입니다.
            2. 중복된 내용이 있는 경우, 중복된 내용을 제거해주세요.
            3. 다른 부가적인 설명 없이 취합된 결과만을 제공해주세요.
            
            
            - 상황 A : 일상 적인 대화
                2개의 답변을 하나의 답변으로 만들어주세요.
            
            - 상황 B : 책 추천 결과 취합
                책에 대한 추천 내용은 누락 없이 모두 취합해주세요.
            
        """)


    #### RAG
    retrieved_docs = retriever.invoke(user_question)
    context = "\n".join([doc.page_content for doc in retrieved_docs])
    
    ### chain
    chain_A = prompt_A | llm
    res_A = chain_A.invoke({"context": context, "user_question": user_question})
    result_RAG = res_A.content
    
    chain_B = prompt_B | llm
    res_B = chain_B.invoke({"user_question": user_question})
    result_LLM = res_B.content
    
    chain_C = prompt_C | llm
    res_C = chain_C.invoke({"result_RAG": result_RAG, "result_LLM": result_LLM})
    
    
    return res_C.content