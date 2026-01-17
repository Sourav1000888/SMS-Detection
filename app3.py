import pickle
import streamlit as st
import re

# SMS Dectection

Tf = pickle.load(open('tff.pkl', 'rb'))
model = pickle.load(open('mnb.pkl', 'rb'))


# Text Preprocessing
def Text_preprocessing(txt):
    clean_text = re.sub(r'http\S+\s', ' ', txt)
    clean_text = re.sub(r'RT|cc', ' ', clean_text)
    clean_text = re.sub(r'#\S+\s', ' ', clean_text)
    clean_text = re.sub(r'@\S+', ' ', clean_text)
    clean_text = re.sub(r'[^\w\s]', ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    clean_text = clean_text.lower()
    return clean_text


def main():
    st.title('SMS Detection')
    uploaded_sms = st.file_uploader('Upload your SMS : ', type=['.txt'])
    Input_text = st.text_area("Enter your message : ")

    if st.button("Predict"):
        Input_text_preprocess = Text_preprocessing(Input_text)
        transform_input_text = Tf.transform([Input_text_preprocess])
        prediction_input_text = model.predict(transform_input_text)[0]
        input_text_result = "🚨 SPAM" if prediction_input_text == 1 else "✅ SAFE (Not-Spam)"
        st.subheader('Input text prediction :')
        st.header(input_text_result)

    if uploaded_sms:
        try:
            decoded_sms = uploaded_sms.read().decode('utf-8')
        except UnicodeDecodeError:
            decoded_sms = uploaded_sms.read().decode('latin-1')

        file_text_preprocess = Text_preprocessing(decoded_sms)
        transform_file_text = Tf.transform([file_text_preprocess])
        prediction_file_text = model.predict(transform_file_text)[0]
        file_text_result = "🚨 SPAM" if prediction_file_text == 1 else "✅ SAFE (Not-Spam)"
        st.subheader('upload file prediction : ')
        st.header(file_text_result)       


main()