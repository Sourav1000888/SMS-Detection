import pickle
import re
import streamlit as st
import pandas as pd
from datetime import datetime

# # SMS Dectection

Tf = pickle.load(open('tff.pkl', 'rb'))
model = pickle.load(open('mnb.pkl', 'rb'))


# Text Preprocessing
def Text_preprocessing(txt):
    #url/links remove
    clean_text = re.sub(r'http\S+\s', ' ', txt)
    clean_text = re.sub(r'#\S+\s', ' ', clean_text)
    # remove sysmbols
    clean_text = re.sub(r'[^\w\s]', ' ', clean_text)
    # remove emoji's
    clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)
    # remove extra space's
    clean_text = re.sub(r'\s+', ' ', clean_text)
    # lower case
    clean_text = clean_text.lower()
    return clean_text



# prediction input text
def detect_text_sms(sms_text):
    text_preprocess = Text_preprocessing(sms_text)
    # text transfrom
    transform_text = Tf.transform([text_preprocess])
    # text prediction
    prediction_text = model.predict(transform_text)[0]
    result = "SPAM" if prediction_text == 1 else "NOT-SPAM"
    return result


# prediction file text
def dectec_file_sms(sms_text):
    try:
        decoded_sms = sms_text.read().decode('utf-8', errors='ignore')
    except UnicodeDecodeError:
        decoded_sms = sms_text.read().decode('latin-1', errors='ignore')

    text_preprocess = Text_preprocessing(decoded_sms)
    #text transform
    transform_text = Tf.transform([text_preprocess])
    # text prediction
    prediction_file_text = model.predict(transform_text)[0]
    result = "SPAM" if prediction_file_text == 1 else "NOT-SPAM"
    return result   

#display prediction
def Display_input_text_result():
    if sms_input:
        text = sms_input if sms_input else "Uploaded file content "
        text_result = detect_text_sms(text)
        if text_result == 'NOT-SPAM':
            st.success(f"Detection: {text_result}")
        else:
            st.error(f"Detection: {text_result}")

        #Add to history     
        if sms_input:
            st.session_state.history.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "message": sms_input[:10] + "..." ,             
                "detection": text_result,
                "type": 'input text'
            })
        else:
            st.error("Please provide SMS content.")

# input text reset function
def reset_text():
    st.session_state['sms'] = ''


# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []
if 'sms' not in st.session_state:
    st.session_state['sms'] = ''

# Header
st.title("SMS Detection Dashboard")
st.markdown("Analyze SMS messages for spam. ")

# Sidebar
st.sidebar.header("Quick Actions")
if st.sidebar.button("New Analysis"):
    st.rerun()

#Slider filter
st.sidebar.header("Filters")
detection_type = st.sidebar.selectbox("Detection Type", ["All", "Spam"])


# Main Content with Tabs
tab1, tab2 = st.tabs(["Analyze", "History"])

# Analyze tab
with tab1:
    st.header("SMS Analysis")

    # input data process
    sms_input = st.text_area("Paste SMS content here ", height=200, key='sms')
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Detect", use_container_width=True):
            Display_input_text_result()
    with col2:
        if st.button('Reset', on_click=reset_text, use_container_width=True):
            pass
       

    # upload file data process
    uploaded_sms = st.file_uploader("Or upload .txt file", type=["txt"])
    if uploaded_sms is not None:
        #Display result
        file_result = dectec_file_sms(uploaded_sms)
        if file_result == 'NOT-SPAM':
            st.success(f"Detection: {file_result}")
        else:
            st.error(f"Detection: {file_result}")

        
        # Add to history
        if file_result: 
            st.session_state.history.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "message": "......" ,
                "detection": file_result,
                "type": 'file text'
            })
        else:
            st.error("Please provide SMS content.")

#History tab
with tab2:
    st.header("Analysis History")
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df)
        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()
    else:
        st.write("No history yet.")

