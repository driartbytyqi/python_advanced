from optparse import Option

import streamlit as  st


col1,col2,col3,col4,col5 = st.columns(5,gap="small",vertical_alignment='center')

with col1:
    st.header("Kolona 1")
    st.write("content for column 1")

with col2:
    st.header("kolona 2")
    st.write("kolona e 2")

with col3:
    st.header("kolona 3")
    st.write("content for column 3")

with col4:
    st.header("kolona 4")
    st.write("kontent for konon 4")

with col5:
    st.header("kolona 5")
    st.write("kontent for konon 5")

with st.container():
    st.header("this is inside the container")
    st.write("this is inside the container")

st.write("this is outside the container")


######side bar
st.sidebar.header("sidebar")

st.sidebar.write("this is the sidebar")

st.sidebar.selectbox("chose an option",["Option1","Option2","Option3"])

st.sidebar.radio("go to ",["home","data","settings"])