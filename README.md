**Project: Parkinson’s Disease Prediction**

**Project Type: Health Prediction**

**Technology Used: Jupyter Notebook, Python, Streamlit**

**Deployment: Streamlit Web App**

**Objective :**
To develop a machine learning model that predicts whether a patient has Parkinson’s disease based on biomedical voice measurements.

**Dataset Information :**
The dataset used in this project is the **Parkinson’s Disease dataset** from the UCI Machine Learning Repository.  
It contains biomedical voice measurements from patients with Parkinson’s and healthy controls.  

**Columns :**
- `patient_id`: Unique identifier for each patient
- `MDVP_Fo_Hz`: Average vocal fundamental frequency (Hz)
- `MDVP_Fhi_Hz`: Maximum vocal fundamental frequency (Hz)
- `MDVP_Flo_Hz`: Minimum vocal fundamental frequency (Hz)
- `MDVP_Jitter_percent`: Frequency variation (%)
- `MDVP_Jitter_Abs`: Absolute jitter
- `MDVP_RAP`: Relative average perturbation
- `MDVP_PPQ`: Pitch period perturbation quotient
- `Jitter_DDP`: Difference of differences in jitter
- `MDVP_Shimmer`: Amplitude variation
- `MDVP_Shimmer_Db`: Shimmer in decibels
- `Shimmer_APQ3`: 3-point amplitude perturbation quotient
- `Shimmer_APQ5`: 5-point amplitude perturbation quotient
- `MDVP_APQ`: Amplitude perturbation quotient
- `Shimmer_DDA`: Average absolute amplitude difference
- `NHR`: Noise-to-Harmonics Ratio
- `HNR`: Harmonics-to-Noise Ratio
- `status`: Target variable → (1 = Parkinson’s, 0 = Healthy)
- `RPDE`: Recurrence Period Density Entropy
- `DFA`: Detrended Fluctuation Analysis
- `spread1, spread2`: Frequency variation measures
- `D2`: Signal complexity (correlation dimension)
- `PPE`: Pitch Period Entropy

