import numpy as np
import pickle
import pandas as pd
import streamlit as st 

mod = open('model.pkl', 'rb')
model = pickle.load(mod)

def welcome():
    return "Welcome All"


def pred_bond(mm, mpa, gpa, p1, p2, p3):
    
    a = pd.DataFrame([[mm, mpa, gpa, p1, p2, p3]], columns=['(mm)', '(Mpa)', '(Gpa)', '(mm).1', '(mm).2', '(mm).3'])
    prediction = model.predict(a)
    print(prediction)
    return prediction

def main():
    st.title("FRP Bonding Strength Prediction")
    html_temp = """
    <div style="background-color:rgb(68, 65, 65);padding:10px">
    <h2 style="color:rgb(241, 153, 20);text-align:center;">WebApp for Bond Strength Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    mm = st.text_input('MM  :',150.00)
    mm = float(mm)

    mpa = st.text_input('Mpa  :',48.2)
    mpa = float(mpa)

    gpa = st.text_input('Gpa  :',230.48)
    gpa = float(gpa)

    p1 = st.text_input('P1  :',0.16)
    p1 = float(p1)

    p2 = st.text_input('P2  :', 50.00)
    p2 = float(p2)

    p3 = st.text_input('P3  :',100.00)
    p3 = float(p3)

    
  
  
    result=""
    if st.button("Predict"):
        result=pred_bond(mm, mpa, gpa, p1, p2, p3)
        #print(result)
        st.success('The Estimated Bond Strength for the given input is {} kN'.format(result))
    
    
    if st.button("About"):
        st.text("FRP - Concrete interfacial bonding strength prediction made using StreamLit")
        st.text("This model is built by Parthiv Akilesh A S")

if __name__ == '__main__':
    main()