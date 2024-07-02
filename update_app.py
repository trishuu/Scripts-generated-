import streamlit as st
import pickle

model = pickle.load(open('model_SVM.pkl', 'rb'))


st.title('Fake News AI')
input_news = st.text_area('Enter the News')

if st.button('Submit'):
    # 2. predict
    result = model.predict([input_news])[0]
    
    # 3. Display
    if result == 1:
        st.header("It is a genuine news")
    else:
        st.header("It is a fake news")
