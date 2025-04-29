import numpy as np
import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler

# ———— Inisialisasi / Load Model ————
if 'model' not in st.session_state:
    # 1) Bikin model (atau load dari file .h5 jika sudah ada)
    model = Sequential(name='water_quality_model')
    model.add(Dense(16, input_dim=9, activation='relu', name='dense_1'))
    model.add(Dense(8, activation='relu',         name='dense_2'))
    model.add(Dense(1, activation='sigmoid',      name='output'))
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    # 2) Simpan model sekali saja
    model.save('water_quality_model.h5')
    st.session_state['model'] = model
else:
    model = st.session_state['model']
# ——————————————————————————————

# ———— Load / Fit Scaler ————
# Contoh dummy, ganti dengan load scaler asli kalau ada:
scaler = MinMaxScaler()
scaler.fit([[0]*9, [1]*9])
# ————————————————————

# ———— UI Streamlit ————
st.title('Prediksi Kualitas Air')

col1, col2 = st.columns(2)
with col1:
    ph              = st.number_input('pH',              value=7.0)
    Solids          = st.number_input('Solids',          value=10000.0)
    Sulfate         = st.number_input('Sulfate',         value=333.0)
    Organic_carbon  = st.number_input('Organic Carbon',  value=10.0)
    Turbidity       = st.number_input('Turbidity',       value=3.0)
with col2:
    Hardness        = st.number_input('Hardness',        value=150.0)
    Chloramines     = st.number_input('Chloramines',     value=7.0)
    Conductivity    = st.number_input('Conductivity',    value=400.0)
    Trihalomethanes = st.number_input('Trihalomethanes', value=66.0)

# Kemas input ke list
data = [ph, Hardness, Solids, Chloramines,
        Sulfate, Conductivity, Organic_carbon,
        Trihalomethanes, Turbidity]

# Tombol prediksi
if st.button('Test Prediksi Air'):
    arr    = np.array([data])
    scaled = scaler.transform(arr)
    pred   = model.predict(scaled)[0][0]

    if pred <= 0.5:
        st.success('✅ Air dapat diminum')
    else:
        st.error('❌ Air tidak dapat diminum')
