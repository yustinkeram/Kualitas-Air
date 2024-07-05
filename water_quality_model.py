import numpy as np
import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Simpan model ke file .h5
filename = 'water_quality_model.h5'
model.save(filename)


# Unggah file model ke komputer Anda
files.download(filename)


#judul web
st.title('Prediksi Kualitas Air')

#membagi kolom
col1, col2,  = st.columns(2)

with col1 :
    ph = st.number_input ('Masukan nilai pH')

with col2 :
    Hardness = st.number_input ('Masukan nilai Hardeness')

with col1 :
    Solids = st.number_input ('Masukan nilai Solids')

with col2 :
    Chloramines = st.number_input ('Masukan nilai Chloramines')

with col1 :
    Sulfate = st.number_input ('Masukan nilai Sulfate')

with col2 :
    Conductivity = st.number_input ('Masukan nilai Conductivity')

with col1 :
    Organic_carbon = st.number_input ('Masukan nilai Organic carbon')

with col2 :
    Trihalomethanes= st.number_input ('Masukan nilai Trihalomethanes')

with col1 :
    Turbidity = st.number_input ('Masukan nilai Turbidity')

# Fungsi untuk prediksi
def predict_quality(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    scaler = MinMaxScaler()
    input_data_scaled = scaler.transform(input_data)
    prediction = water_quality.predict(input_data_scaled)
    return prediction[0]

#Prediksi
water_quality = ''

# tombol prediksi
if st.button('Test Prediksi Air'):
    water_quality = water_quality.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])

    if(water_quality <= 0.5):
        water_quality = 'Air dapat Diminum'
        st.success(water_quality)
    else :
        water_quality = 'Air Tidak dapat Diminum'
        st.error(water_quality)
    
