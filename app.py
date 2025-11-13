import numpy as np
import pickle
import streamlit as st

# loading the saved model
with open("C:\\Users\\narma\\Downloads\\parkinsons_prediction-main\\parkinsons_prediction-main\\trained_model_logistic_regression.pkl", 'rb') as file:
    loaded_model = pickle.load(file)

# creating a function for Prediction
def parkinson_disease_prediction(input_data):
    # Convert input data to appropriate data types
    input_data = [float(value) for value in input_data]

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person does not have Parkinson\'s Disease.'
    else:
        return 'The person has Parkinson\'s Disease.'


def main():
    # giving a title
    st.title('Parkinson Disease Prediction Web App')

    # getting the input data from the user
    MDVP_Fo_Hz = st.number_input('MDVP Fo (Hz)')
    MDVP_Fhi_Hz = st.number_input('MDVP Fhi (Hz)')
    MDVP_Flo_Hz = st.number_input('MDVP Flo (Hz)')
    MDVP_Jitter_percent = st.number_input('MDVP Jitter (%)')
    MDVP_Jitter_Abs = st.number_input('MDVP Jitter (Abs)')
    MDVP_RAP = st.number_input('MDVP RAP')
    MDVP_PPQ = st.number_input('MDVP PPQ')
    Jitter_DDP = st.number_input('Jitter DDP')
    MDVP_Shimmer = st.number_input('MDVP Shimmer')
    MDVP_Shimmer_dB = st.number_input('MDVP Shimmer (dB)')
    Shimmer_APQ3 = st.number_input('Shimmer APQ3')
    Shimmer_APQ5 = st.number_input('Shimmer APQ5')
    MDVP_APQ = st.number_input('MDVP APQ')
    Shimmer_DDA = st.number_input('Shimmer DDA')
    NHR = st.number_input('NHR')
    HNR = st.number_input('HNR')
    RPDE = st.number_input('RPDE')
    DFA = st.number_input('DFA')
    spread2 = st.number_input('spread2')
    D2 = st.number_input('D2')
    PPE = st.number_input('PPE')

    diagnosis = ''

    if st.button('Predict Parkinson\'s Disease'):
        input_data = [MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread2, D2, PPE]

        if all(v == 0 for v in input_data):
            st.warning("Please enter valid input values before predicting.")
        else:
            diagnosis = parkinson_disease_prediction(input_data)

    st.success(diagnosis)

if __name__ == '__main__':
    main()
