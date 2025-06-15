

# ☕ Coffee Price Predictor with Streamlit

This Streamlit web application analyzes coffee sales data and predicts coffee prices based on payment type and coffee name.

## 📊 Project Overview

This project was developed as part of the **Introduction to Data Science** course. It demonstrates a complete workflow from:

- Loading and cleaning real-world sales data
- Performing exploratory data analysis (EDA)
- Building a machine learning model
- Deploying a real-time prediction app using **Streamlit** on Hugging Face Spaces

---

## 📁 Dataset Information

The dataset contains 3,636 sales records with the following columns:

- `date`: Date of purchase
- `datetime`: Timestamp of purchase
- `cash_type`: Payment method (cash/card)
- `card`: Masked card number (or unknown)
- `money`: Amount spent
- `coffee_name`: Name of the coffee purchased

---

## 🚀 How It Works

### ✅ EDA Section:
- Summary statistics (mean, median, std)
- Histograms and boxplots of prices
- Correlation heatmap of encoded features

### ✅ Machine Learning:
- Model: `LinearRegression`
- Features: `cash_type`, `coffee_name`
- Target: `money`
- Evaluation: RMSE score

### ✅ Live Prediction:
- User selects payment type and coffee
- Model instantly predicts expected price

---

## 🖥 Technologies Used

- Python
- Streamlit
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

---

## 📦 Installation (Optional)

To run locally:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
