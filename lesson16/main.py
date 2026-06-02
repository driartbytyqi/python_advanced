import  streamlit as st
from watchdog.observers.fsevents2 import message


def main():
    st.title("hello,world")

    st.button("click me")

st.checkbox("check")

if st.checkbox("driart"):
    st.write("qiky tekst po shfaqet sepse ti e ke check katrorin e zbrazet")

if st.button("click"):
    st.write("button clicked")

name = st.text_input("enter your name")

st.write("your name is",name)


age =st.number_input("enter your age",min_value=0,max_value=100)
st.write("your age is",age)

message = st.text_area("enter text")

if st.button("suces"):
    st.success("operation was succesful")


if __name__=="__main__":
    main()