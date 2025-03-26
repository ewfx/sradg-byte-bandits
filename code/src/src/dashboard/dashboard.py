%%writefile app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

df = pd.read_excel("bytebandits.xlsx")
# Save to a CSV file
csv_filename = "sample_data.csv"
df.to_csv(csv_filename, index=False)

# Function to detect anomalies
def detect_anomalies(data, contamination=0.05):
    mean_val = data.mean()
    std_val = data.std()

    # Isolation Forest
    iso_forest = IsolationForest(contamination=contamination, random_state=42)
    data['Anomaly_ML'] = iso_forest.fit_predict(data[['Balance Difference']])
    data['Anomaly_ML'] = data['Anomaly_ML'].apply(lambda x: True if x == -1 else False)

    return data

# Streamlit UI
st.title("Anomaly Detection in Reconciliation Process")
st.write("Upload a CSV file with a 'Balance Difference' column to detect anomalies.")

# File uploader
uploaded_file = st.file_uploader(csv_filename, type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if 'Balance Difference' not in df.columns:
        st.error("CSV must contain 'Balance Difference' column.")
    else:
        # Select contamination level
        contamination = st.slider("Set Contamination Level (for ML model)", 0.01, 0.1, 0.05)

        # Detect anomalies
        df = detect_anomalies(df[['Balance Difference']], contamination)

        # Display anomalies
        st.subheader("Detected Anomalies")
        st.dataframe(df[df['Anomaly_ML']])

        # Plot visualization
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.scatter(df.index, df['Balance Difference'], c=df['Anomaly_ML'], cmap='coolwarm', label="Anomalies")
        ax.axhline(df['Balance Difference'].mean() + 3 * df['Balance Difference'].std(), color='r', linestyle='dashed', label="Upper Threshold")
        ax.axhline(df['Balance Difference'].mean() - 3 * df['Balance Difference'].std(), color='r', linestyle='dashed', label="Lower Threshold")
        ax.set_xlabel("Diff Index")
        ax.set_ylabel("Diff Amount")
        ax.set_title("Anomaly Detection Visualization")
        ax.legend()
        st.pyplot(fig)


#To run the code
!streamlit run app.py & npx localtunnel --port 8501

#To get IP Password
!wget -q -O - ipv4.icanhazip.com

