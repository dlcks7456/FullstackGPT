import streamlit as st

### 7.0 Introduction
# st.title("Hello world!")

# st.subheader("Welcome to Streamlit!")

# st.markdown('''
# #### I love it!
# ''')
### -------------------

### 7.1 Magic
# from langchain.prompts import PromptTemplate

# st.write('Hello')

# a = [1, 2, 3, 4]
# # st.write([1, 2, 3, 4])

# d = {"x": 1}
# # st.write({"x": 1})

# # st.write(PromptTemplate)
# # PromptTemplate

# # p = PromptTemplate.from_template("xxx")
# # st.write(p)
# a

# d
# # p # Steamlit은 이렇게 변수를 써두면 이것을 화면에 표기한다!

# st.selectbox(
#     "Choose your model", 
#     (
#         "GPT-3",
#         "GPT-4"
#     ))
### -------------------


### 7.2 Data Flow
# from datetime import datetime

# today = datetime.today().strftime("%H:%M:%S")

# st.title(today)

# model = st.selectbox(
#     "Choose your model", 
#     (
#         "GPT-3",
#         "GPT-4"
#     )
# )

# if model == "GPT-3" :
#     st.write("cheap")
# else :
#     st.write("not cheap")

#     st.write(model)

#     name = st.text_input("What is your name?")

#     st.write(name)

#     value = st.slider(
#         "temperature", 
#         min_value=0.1, 
#         max_value=1.0,
#         step=0.1
#     )

#     st.write(value)


### 7.3 Multi Page
# st.title("title")

# with st.sidebar :
#     st.title("sidebar title")
#     st.text_input("xxx")


# tab_one, tab_two, tab_three = st.tabs(["A", "B", "C"])
# with tab_one :
#     st.write('a')

# with tab_two :
#     st.write('b')

# with tab_three :
#     st.write('c')

st.set_page_config(
    page_title="FullstackGPT Home",
    page_icon="😎",
)

st.markdown(
'''
# Hello!

Welcome to my FullstackGPT Portfolio!

Here are the apps I made :
- [ ] [DocumentGPT](/DocumentGPT)
- [ ] [PrivateGPT](/PrivateGPT)
- [ ] [QuizGPT](/QuizGPT)
- [ ] [SiteGPT](/SiteGPT)
- [ ] [MeetingGPT](/MeetingGPT)
- [ ] [MeetingGPT](/MeetingGPT)
- [ ] [InvestorGPT](/InvestorGPT)
'''
)

### -------------------