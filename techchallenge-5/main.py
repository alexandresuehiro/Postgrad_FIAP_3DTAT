import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Assume 'df' is your DataFrame loaded as in your provided code

st.title("Success Prediction App")

# 1. Feature Selection
features = st.multiselect(
    "Select Features (IPV, IPP, IPS, IDA, IAN, IEG, IAA):",
    ["IPV", "IPP", "IPS", "IDA", "IAN", "IEG", "IAA"],
)

# 2. Year Filtering
years = st.multiselect(
    "Select Years (2020, 2021, 2022):",
    [2020, 2021, 2022],
)

# 3. Target Selection
targets = st.multiselect(
    "Select Targets (PONTO_VIRADA_2020, PONTO_VIRADA_2021, PONTO_VIRADA_2022):",
    ["PONTO_VIRADA_2020", "PONTO_VIRADA_2021", "PONTO_VIRADA_2022"],
)

# 4. Model Selection
model_choice = st.selectbox(
    "Select Model:",
    ["Logistic Regression", "Decision Tree", "Random Forest"],
)
# Data Preprocessing (example)
if features and years and targets:
    selected_features = [f"{f}_{y}_NUM" for f in features for y in years]
    X = df[selected_features]
    y = df[targets[0]]  # Assuming you're using only one target for now

    # Model Training and Prediction
    if model_choice == "Logistic Regression":
        model = LogisticRegression()
    elif model_choice == "Decision Tree":
        model = DecisionTreeClassifier()
    elif model_choice == "Random Forest":
        model = RandomForestClassifier()

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
  
    # Display Results
    st.write("Predictions:", predictions)
