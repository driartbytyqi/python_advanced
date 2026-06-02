import streamlit as st


def kalkulo(num1,num2,operation):
    if operation=="mbledhje":
        result = num1+num2
    elif operation=="zbritje":
        result=num1-num2

    return result

def main():
    st.title("simple calculator")


num1 = st.number_input("enter the first number", step=1)

num2 = st.number_input("enter the second number", step=1)



operation= st.radio("select operation",["mbledhje","zbritje","shumzim","pjestim"])

result = kalkulo(num1,num2,operation)

st.write(result)