import streamlit as st
import pickle
from gensim.utils import simple_preprocess
import fitz

# Email Detection

Tf = pickle.load(open('tf_idf.pkl', 'rb'))
model = pickle.load(open('svc.pkl', 'rb'))



def main():
    st.title('Email Detection ')

    uploaded_email = st.file_uploader('Upload your Email : ', type=['.txt', '.pdf'])
    input_text = st.text_area('Enter your Email : ')

    # Prediction input text
    if st.button('Predict'):
        if input_text:
            text_preprocess = ' '.join(simple_preprocess(input_text))
            transform_text = Tf.transform([text_preprocess]).toarray()
            prediction_text = model.predict(transform_text)[0]
            result_input_text = 'SPAM' if prediction_text == 1 else 'NOT-SPAM'
            st.subheader('Input text prediction : ')
            st.header(result_input_text)
        else:
            st.warning('please enter some text : ')

    # Prediction uploaded file
    if uploaded_email is not None:
        file_type = uploaded_email.type
        if 'pdf' in file_type:
            email_data = fitz.open(stream=uploaded_email.read(), filetype='pdf')
            email_content = ''
            for page in email_data:
                email_content += page.get_text()
        else:
            email_content = uploaded_email.read().decode('utf-8', errors='ignore')


        filetext_preprocess = ' '.join(simple_preprocess(email_content))
        transform_file_text = Tf.transform([filetext_preprocess]).toarray()
        prediction_file_text = model.predict(transform_file_text)[0]
        result_file_text = 'SPAM' if prediction_file_text == 1 else 'NOT-SPAM'
        st.subheader('Upload file prediction : ')
        st.header(result_file_text)            
    


main()

