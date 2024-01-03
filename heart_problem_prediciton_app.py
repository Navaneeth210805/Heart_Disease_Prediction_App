import streamlit as st
import pandas as pd
import numpy as np
import pickle
import subprocess
subprocess.call(["pip", "list"])
subprocess.call(["pip", "install", "scikit-learn==1.3.1"])
from sklearn import LogisticRegression
loaded_content=pickle.load(open('model.sav','rb'))

def prediction(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    df1 = pd.DataFrame(input_array, columns=['Age','Sex','Chest pain type','BP','Cholesterol','FBS over 120','EKG results','Max HR','Exercise angina','ST depression','Slope of ST','Number of vessels fluro','Thallium'])
    prediction_made=loaded_content.predict(df1)
    print(prediction_made)
    if(prediction_made[0]==1):
        return{"Person has heart disease"}
    else:
        return{"Person doesn't have heart disease"}
    
def main():
    st.title("Heart Problem Predicition App")

    age = st.text_input("Age",25)
    sex_type = st.radio('Sex',["Male","Female"])
    if(sex_type=="Male"):
        sex=1
    else:
        sex=0
    chest_pain = st.radio("Type of Chest Pain",["Stable Angina","Unstable Angina","Variant (Prinzmetal's) Angina","Microvascular Angina"])
    if chest_pain=="Stable Angina":
        chest_pain_type=1
    elif chest_pain=="Unstable Angina":
        chest_pain_type=2
    elif chest_pain=="Variant (Prinzmetal's) Angina":
        chest_pain_type=3
    else:
        chest_pain_type=4
    blood_pressure = st.text_input("Resting Blood Pressure",120)
    cholesterol = st.text_input("Serum Cholesterol in mg/dl",120)
    fbs_over_120 = st.radio("Fasting Blood Sugar over 120",["Yes","No"])
    if fbs_over_120=="Yes":
        fbs_over_120=1
    else:
        fbs_over_120=0
    ekg_results = st.text_input("ElectroCardiographic Results",0)
    max_hr = st.text_input("Max Heart Rate",130)
    exercise_angina = st.radio("Exercise induced Angina",[0,1])
    st_depression = st.text_input("ST Depression",0)
    slope_of_st = st.text_input("Slope of ST",0)
    num_vessels_fluro = st.radio("Number of vessels flourosopy",[0,1,2,3])
    thallium = st.radio("Thallium",["Normal","Fixed Defect","Reversable defect"])
    if thallium=="Normal":
        thallium=3
    elif thallium=="Fixed Defect":
        thallium=5
    else:
        thallium=7

    diagnosis=""
    if(st.button("Test Result")):
        try:
            diagnosis=prediction([age,sex,chest_pain_type,blood_pressure,cholesterol,fbs_over_120,ekg_results,max_hr,exercise_angina,st_depression,slope_of_st,num_vessels_fluro,thallium])
            st.success(diagnosis)
        except:
            st.error("Fill out every details")
    
    

if __name__=="__main__":
    main()
