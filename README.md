# 📈 Large-Scale Stock Trend Forecasting and Analysis

🔗 **[Read Full Report](https://your-report-link-here.com)**  
*A research-oriented data engineering and analytics project using Apache Spark, Dash, MongoDB, and more.*

---

## ✅ How to Run

- **To run the project:** Run the jupyter notebook *Assignment-2.ipynb*
- **To run the visualization:** Run the python file *app.py* and use the IP address displayed in terminal.

---

## 🧠 Project Outcomes

### 1. 🔬 Research Prototype for Large-Scale Stock Trend Forecasting

This project demonstrates a robust and scalable pipeline for collecting, storing, processing, and modeling stock market data. The architecture integrates:

- **Data Sources:** Yahoo Finance, Reddit, Twitter (social and financial sentiment)
- **Storage Solutions:** 
  - **MongoDB (NoSQL)** for raw and unstructured data
  - **HDFS (Hadoop)** for large-scale structured historical stock data
- **Processing Engine:** Apache Spark used for PCA-based dimensionality reduction and parallelized ML workflows
- **Model Evaluation:** Comparative analysis between multiple regressors to find the best-fit predictive model
- **Visualization Tool:** Dash for interactive data visualization

![Flow](https://github.com/user-attachments/assets/ff8749c5-9505-4e80-82e9-f8ff1b61d506)

---

### 2. 🤖 Benchmarking Machine Learning Models vs. Traditional Statistical Methods

We evaluated and compared several ML and statistical models using RMSE and R² scores:

| Model                   | RMSE     | R² Score |
|------------------------|----------|----------|
| Isotonic Regression     | 105.1083 | -0.00042 |
| Decision Tree Regression| 10.4699  | 0.9901   |
| Gradient Boosting       | 9.3671   | 0.9921   |
| Linear Regression       | 5.8395   | 0.9969   |

**📌 Insight:**  
Linear Regression outperformed all models on RMSE and R² metrics, proving effective for time-series trend forecasting in this context.

---

### 3. 📊 Interactive Tool/Plugin for Stock Market Analytics

An interactive frontend dashboard was built using **Dash** (by Plotly), allowing users to:

- Select stocks to visualize historical and predicted trends
- View model performance comparison dynamically
- Analyze features using principal component analysis (PCA)

![Stocks](https://github.com/user-attachments/assets/dd2b519d-a4a5-428e-88bf-71b62e8b0182)

In addition, **Apache Hive** is integrated to enable SQL-like querying over the Hadoop-stored data for pattern discovery and ad hoc analysis.

---

## 🚀 Technologies Used

- Python, PySpark, Pandas, Scikit-learn
- MongoDB Atlas
- Apache Spark + Hive + Hadoop (HDFS)
- Dash for visualization
- yFinance, PRAW, Tweepy for data collection

---
