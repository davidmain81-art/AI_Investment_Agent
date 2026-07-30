import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp{
        background-color:#0F172A;
    }

    h1,h2,h3,h4,p,div,label{
        color:white !important;
    }

    div[data-testid="metric-container"]{
        background:#1E293B;
        border-radius:18px;
        padding:20px;
        border:1px solid #334155;
        box-shadow:0px 10px 25px rgba(0,0,0,.35);
    }

    </style>
    """, unsafe_allow_html=True)