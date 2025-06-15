
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Set page config
st.set_page_config(page_title="☕ Coffee Price Estimator", layout="centered")

# Aesthetic styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f5f0;
        }
        h1 {
            color: #6b4f2c;
            text-align: center;
        }
        .stButton button {
            background-color: #6b4f2c;
            color: white;
            font-weight: bold;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("☕ Coffee Price Estimator")

# Load Data
df = pd.read_csv("src/index_1.csv")

# Fill missing
df['card'].fillna("Unknown", inplace=True)

# Encode categorical features

le_coffee = LabelEncoder()
le_cash = LabelEncoder()

df['coffee_name_encoded'] = le_coffee.fit_transform(df['coffee_name'])
df['cash_type_encoded'] = le_cash.fit_transform(df['cash_type'])

# Train model
X = df[['cash_type_encoded', 'coffee_name_encoded']]
y = df['money']
model = LinearRegression()
model.fit(X, y)

# User Input Form
st.markdown("### 🎯 Enter Order Details Below")

with st.form("prediction_form"):
    cash = st.selectbox("💳 Payment Method", df['cash_type'].unique())
    coffee = st.selectbox("☕ Coffee Type", df['coffee_name'].unique())
    submit = st.form_submit_button("🔍 Predict Price")

    if submit:
        x_cash = le_cash.transform([cash])[0]
        x_coffee = le_coffee.transform([coffee])[0]
        input_features = np.array([[x_cash, x_coffee]])
        pred_price = model.predict(input_features)[0]

        st.success(f"✅ Predicted Price: Rs. {pred_price:.2f}")
        st.markdown(f"""
            <div style='padding: 10px; background-color: #f4e9dc; border-radius: 10px;'>
                <h4 style='color: #6b4f2c;'>Prediction Summary:</h4>
                <ul>
                    <li><strong>Payment Method:</strong> {cash}</li>
                    <li><strong>Coffee Name:</strong> {coffee}</li>
                    <li><strong>Expected Price:</strong> Rs. {pred_price:.2f}</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
