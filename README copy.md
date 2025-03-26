# 🚀 Project Name

## 📌 Table of Contents
- [Introduction]

   • Anomaly detection helps identify unusual patterns in financial transactions.
   • Uses statistical methods and machine learning to flag discrepancies.
   • Implemented using Python, leveraging Isolation Forest .

- [How We Built It]

   Methodology :

      . **Statistical Method**: Uses Standard deviation and mean.
      • **Machine Learning**: Isolation Forest identifies abnormal transactions.
      • **Visualization**: Scatter plots highlight flagged anomalies.
      • **Interactive UI**: Streamlit-based dashboard for user interaction.

   Implementation Steps :

      1. Load transaction data (CSV format).
      2. Compute statistical thresholds (mean, standard deviation).
      3. Apply Isolation Forest for anomaly detection.
      4. Visualize flagged anomalies.
      5. Deploy interactive UI using Streamlit.

   Visualization of Anomalies :

      • Scatter plot marks anomalies in red.
      • Dashed lines represent expected transaction range.
      • Interactive UI allows users to analyze flagged data.


  [How To Run]

   To run the dashboard execute dashboard.py file

   #To run the server
   !streamlit run app.py & npx localtunnel --port 8501

   #To get IP Password
   !wget -q -O - ipv4.icanhazip.com

   -------

   execute main.py to run model 


- [Tech Stack]

      • **Python Libraries**: pandas, numpy, scikit-learn, matplotlib, streamlit
      • **ML Algorithm**: Isolation Forest
      • **Statistical Analysis**: Standard deviation
      • **Deployment**: Streamlit for UI
      • **Data Input**: CSV file with transaction amounts

- [Team]
   Shaik Azharuddin (azrDevelopU)
   Himanshu Shekhar (himvid123)
   Subhranshu Kar 
   Naresh Pillamgolla (nareshp4080)
   Jaiprakash Yadav (jpnitp)

