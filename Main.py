import streamlit as st
import pandas as pd
from Email import SendEmail

st.title('Bulk Emailer')

file = st.file_uploader('Drop your Email\'s here')

if file:
    data = pd.read_csv(file)
    emails = list(data['Email'])

    for email in emails:
        user = SendEmail(email)
        user.sendMessage('This is a Test')
