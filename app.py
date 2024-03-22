import streamlit as st
import prediction_heart as pt

res = "" 

col1, col2 = st.columns(2)

with col1: 
    imgpath = "heart.jpg"
    st.image(imgpath)

with col2: 
    # Chest Pain Type
    st.markdown("## Chest Pain Type")
    cp_options = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non-Anginal Pain": 2,
        "Asymptomatic": 3
    }
    cp_selected = st.selectbox("Select Chest Pain Type", list(cp_options.keys()))
    cp_selected = int(cp_options[cp_selected])

    # Resting Blood Pressure
    st.markdown("## Resting Blood Pressure (in mm Hg)")
    trestbps = st.number_input("Enter Resting Blood Pressure", value=0)
    trestbps = int(trestbps)

    # Serum Cholestoral
    st.markdown("## Serum Cholestoral in mg/dl")
    chol = st.number_input("Enter Serum Cholestoral", value=0)
    chol = int(chol)

    # Fasting Blood Sugar
    st.markdown("## Fasting Blood Sugar")
    fbs_options = {
        "Fasting Blood Sugar < 120 mg/dl": 0,
        "Fasting Blood Sugar > 120 mg/dl": 1
    }
    fbs_selected = st.selectbox("Select Fasting Blood Sugar", list(fbs_options.keys()))
    fbs_selected = int(fbs_options[fbs_selected])
    

    # Resting Electro-cardiographic Result
    st.markdown("## Resting Electro-cardiographic Result")
    restecg_options = {
        "Normal": 0,
        "having ST-T wave abnormality": 1,
        "showing probable or definite left ventricular hypertrophy": 2
    }
    restecg_selected = st.selectbox("Select Resting Electro-cardiographic Result", list(restecg_options.keys()))
    restecg_selected = int(restecg_options[restecg_selected])

    # Maximum Heart Rate Achieved
    st.markdown("## Maximum Heart Rate Achieved")
    thalach = st.number_input("Enter Maximum Heart Rate Achieved", value=0)
    thalach = int(thalach)

    # Exercise Induced Angina
    st.markdown("## Exercise Induced Angina")
    exang_options = {
        "Yes": 1,
        "No": 0
    }
    exang_selected = st.selectbox("Select Exercise Induced Angina", list(exang_options.keys()))
    exang_selected = int(exang_options[exang_selected])
    print()

    # Prediction button
    if st.button("Predict"):
        # Your prediction code here
        res = pt.prepare(cp_selected, trestbps, chol, fbs_selected, restecg_selected, thalach, exang_selected)


result_1 = pt.prepare(cp=1, trestbps=120, chol=200, fbs=0, restecg=1, thalach=150, exang=0)
print(result_1)

result_2 = pt.prepare(cp=0, trestbps=140, chol=250, fbs=1, restecg=2, thalach=170, exang=1)
print(result_2)

result_3 = pt.prepare(cp=2, trestbps=130, chol=220, fbs=0, restecg=0, thalach=160, exang=1)
print(result_3)
        
st.text(res)
