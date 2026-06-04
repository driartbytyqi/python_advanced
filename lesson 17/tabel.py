import streamlit as st

tab1,tab2,tab3 = st.tabs(["tab1","tab 2","tab3"])

with tab1:
    st.header("content for tab1")
    st.write("this is the content of the first tab")


with tab2:
    st.header("content for tab2")
    st.write("this is the content of the first tab")

with tab3:
    st.header("content for tab3")
    st.write("this is the content of the first tab")


