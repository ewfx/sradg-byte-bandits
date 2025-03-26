import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
def detect_anomalies(file_path):

    # Load historical data (replace with actual dataset)
    df = pd.read_excel(file_path, usecols=['Balance Difference'])

    # Define expected range (using standard deviation method)
    mean_val = df['Balance Difference'].mean()
    std_val = df['Balance Difference'].std()

    # Use Isolation Forest for anomaly detection
    iso_forest = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly_ML'] = iso_forest.fit_predict(df[['Balance Difference']])
    df['Anomaly_ML'] = df['Anomaly_ML'].apply(lambda x: True if x == -1 else False)

    # Visualizing anomalies
    plt.figure(figsize=(10, 5))
    plt.scatter(df.index, df['Balance Difference'], c=df['Anomaly_ML'], cmap='coolwarm', label="Anomalies")
    plt.axhline(mean_val + (1.5 * std_val), color='r', linestyle='dashed', label="Upper Threshold")
    plt.axhline(mean_val -  (1.5 * std_val), color='r', linestyle='dashed', label="Lower Threshold")
    plt.xlabel("Diff Index")
    plt.ylabel("Diff Amount")
    plt.title("Anomaly Detection in Reconciliation Process")
    plt.legend()
    plt.show()

    # Output anomalies
    anomalies = df[df['Anomaly_ML']]
    print("Detected Anomalies:\n", anomalies)



