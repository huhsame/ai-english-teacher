import streamlit as st
import langchain_helper
from langchain.document_loaders import YoutubeLoader
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# if cuisine:
#     response = langchain_helper.generate_restaurant_name_and_items(cuisine)
#     st.header(response["restaurant_name"].strip())
#     menu_items = response["menu_items"].strip().split(",")
#     st.write("**Menu Items**")
#     for item in menu_items:
#         st.write("-", item)


# Chat Model 초기화


st.title("AI 영어선생님 👩🏻‍🏫")
st.write("원하는 영상으로 학습자료를 만들어드립니다.")

# 사용자 입력 받기
ytURL = st.text_input("Youtube URL")


if st.button("🪄 만들어주세요"):
    with st.spinner("중요한 표현에 밑줄 긋는 중 ... 2~3분"):
        loader = YoutubeLoader.from_youtube_url(ytURL)
        yt = loader.load()
        transcript = yt[0].page_content
        response = langchain_helper.generate_sentence_and_dict(transcript)
        # sentences = response["sentence_list"].strip().split("/n")
        # menu_items = response["dict"].strip().split("/n/n")
        # st.write("sentences")
        # for item in menu_items:
        #     st.write("-", item)
        st.write(response)
