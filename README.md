# 🌾 Agricultural Yield Prediction and Optimization

This project leverages machine learning techniques to predict agricultural crop yield based on various environmental and agronomic inputs. The goal is to assist farmers, agronomists, and policymakers in making data-driven decisions to improve crop productivity and optimize resource usage.

## 📌 Project Highlights

- 📊 Data preprocessing with outlier handling, encoding, and scaling
- 🧠 Model training using Linear Regression, Random Forest, and Gradient Boosting
- ✅ Final model selected: **Linear Regression** (best MAE & RMSE)
- 💾 Model and preprocessing tools saved using pickle
- 🌐 Interactive Streamlit  web app for real-time predictions

---

## 📁 Dataset

agriculture_dataset.csv 
Target Variable: Yield(tons)

### Key Features:

- Crop_Type ,Irrigation_Type, Soil_Type, Season
  - Farm_Area(acres), Fertilizer_Used(tons), Pesticide_Used(kg), Water_Usage(cubic meters)

---

## 🧪 EDA & Preprocessing

- **Missing values: Checked and handled
- **Outliers: Capped using IQR method
- **Categorical Encoding: Label Encoding for categorical variables
- **Scaling: StandardScaler for numeric columns

### Exploratory Visuals:

- Pair plots of numeric variables
- Heatmap of correlations

---

## 🤖 Model Training & Evaluation

### Algorithms Tested:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Evaluation Metrics:

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

``text
Linear Regression    - MAE: 10.63, RMSE: 12.63
Random Forest        - MAE: 11.05, RMSE: 13.51
Gradient Boosting    - MAE: 13.83, RMSE: 16.12
✅ Final Model Chosen: Linear Regression

💾 Model Deployment
Saved using pickle:

yield_model.pkl — Trained model

encoders_scaler.pkl — Label encoders and scaler

🌐 Streamlit Web App
Features:
Interactive UI to select crop, irrigation type, soil type, and season

Input numerical values like farm area, fertilizer, pesticide, and water usage

Predicts estimated yield in tons
🔮 Future Enhancements
Integrate real-time weather data for predictions

Incorporate geographic and satellite imagery

Expand to multi-crop and region-specific predictions

👨‍💻 Author
Govindev Eyyani Pradeesh
Data Analyst | Civil Engineer turned Data Enthusiast
🔗 LinkedIn (https://www.linkedin.com/in/govindev-eyyani-pradeesh-675b0426a/)
