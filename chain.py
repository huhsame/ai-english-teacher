from dotenv import load_dotenv

load_dotenv()
from operator import itemgetter

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser


prompt1 = ChatPromptTemplate.from_template(
    "당신은 IELTS나 TOEFL 시험을 준비하는 한국인을 위한 탁월한 영어 교사입니다. 당신은 영어와 한국어 모두를 능숙하게 사용할 수 있으므로 두 언어로 개념을 명확하게 설명할 수 있습니다. 스크립트를 제공하면 당신은 중요한 영어 문장을 잘 찾아내고 자세히 설명할 수 있습니다. 단어나 표현에 대해 물어보면 영어와 한국어로 그 의미와 예문을 제공할 수  있습니다. 이제 다음 스크립트 중에서 영어 스피킹 공부에 유용한 영어문장 30개를 뽑아 리스트를 만들어주세요. \n\n {transcript}"
)
prompt2 = ChatPromptTemplate.from_template(
    "주어진 각 30문장에서 구동사나 숙어에 관한 한글 뜻, 원래 문장에서의 사용 예시, 그리고 프렌즈 시트콤에서의 예문을 포함한 사전 리스트를 제작해주세요. 원래 문장과 프렌즈 예문에서 표제에 해당하는 부분은 볼드 처리해주세요.  ```- **[주어진 숙어나 구동사]**\n- 뜻: [해당 표현의 뜻]\n- 원래 문장 예시: [원래 문장에서의 사용 예]\n- 프렌즈 예문: [프렌즈 시트콤에서의 예문]```\n\n {sentence_list}  "
)

model = ChatOpenAI()

chain1 = prompt1 | model | StrOutputParser()

chain2 = {"sentence_list": chain1} | prompt2 | model | StrOutputParser()

result = chain2.invoke({"transcript:"})
print(result)
