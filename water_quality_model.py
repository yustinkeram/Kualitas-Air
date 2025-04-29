import numpy as np
import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import MinMaxScaler

# Dummy model untuk contoh (Anda bisa ganti dengan model hasil training Anda)
model = Sequential()
model.add(Dense(16, input_dim=9, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Simpan model ke file .h5
filename = 'water_quality_model.h5'
model.save(filename)

#judul web
st.title('Prediksi Kualitas Air')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    ph = st.number_input('Masukan nilai pH')

with col2:
    Hardness = st.number_input('Masukan nilai Hardeness')

with col1:
    Solids = st.number_input('Masukan nilai Solids')

with col2:
    Chloramines = st.number_input('Masukan nilai Chloramines')

with col1:
    Sulfate = st.number_input('Masukan nilai Sulfate')

with col2:
    Conductivity = st.number_input('Masukan nilai Conductivity')

with col1:
    Organic_carbon = st.number_input('Masukan nilai Organic carbon')

with col2:
    Trihalomethanes = st.number_input('Masukan nilai Trihalomethanes')

with col1:
    Turbidity = st.number_input('Masukan nilai Turbidity')

# Inisialisasi MinMaxScaler (dalam prakteknya, scaler seharusnya fit dari data training)
scaler = MinMaxScaler()
scaler.fit([[0,0,0,0,0,0,0,0,0], [100,100,100,100,100,100,100,100,100]])  # Dummy fitting

# tombol prediksi
if st.button('Test Prediksi Air'):
    input_data = np.array([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0][0]

    if prediction <= 0.5:
        st.success('Air dapat diminum')
    else:
        st.error('Air tidak dapat diminum')

# Tombol download model
st.download_button("Download Model", data=open(filename, "rb"), file_name=filename)
