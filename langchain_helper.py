# from dotenv import load_dotenv

# load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser


model = ChatOpenAI(
    model="gpt-3.5-turbo-16k-0613",
    temperature=0.7,
    max_tokens=7000,
)


def generate_sentence_and_dict(transcript):
    prompt1 = ChatPromptTemplate.from_template(
        "당신은 IELTS나 TOEFL 시험을 준비하는 한국인을 위한 탁월한 영어 교사입니다. 이제 다음 스크립트 중에서 영어 스피킹 공부에 유용한 영어문장 10개를 뽑아 리스트를 만들어주세요. \n\n {transcript}"
    )
    prompt2 = ChatPromptTemplate.from_template(
        "주어진 각 10문장에서 구동사나 숙어에 관한 사전을 만들어주세요. 사전은 표제어(구동사나 숙어), 한글 뜻, 원래 영어 문장, 그리고 프렌즈 시트콤에서의 영어 예문을 포함한 사전 리스트를 제작해주세요. 원래 영어 문장과 프렌즈 영어 예문에서 표제어에 해당하는 부분은 볼드 처리해주세요.  ```1. **[표제어]**\n   - 뜻: [표제어의 한글 뜻]\n    - 원래 문장 예시: [원래 영어 문장]\n   - 프렌즈 예문: [프렌즈 시트콤에서의 영어 예문]```\n\n {sentence_list}  "
    )

    chain1 = prompt1 | model | StrOutputParser()

    chain2 = {"sentence_list": chain1} | prompt2 | model | StrOutputParser()

    response = chain2.invoke({"transcript": transcript})

    return response


# if __name__ == "__main__":
#     print(generate_restaurant_name_and_items("Italian"))
