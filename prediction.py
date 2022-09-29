import streamlit as st
import numpy as np
from Model import model


def app():
    st.header("Welcome to prediction page")
    st.subheader("Select values:")

    hours = st.slider("Hours", 1.1, 24.5)
    hours = np.reshape(hours,(1,1))

    if (st.button("Predict")):
        my_model, acc = model()
        prediction = my_model.predict(hours)

        st.success("Predicted successfully")
        st.success(f"Score value is {round(prediction[0], 2 )}")
        st.info(f"Our model accuracy is {round(acc, 2)}")