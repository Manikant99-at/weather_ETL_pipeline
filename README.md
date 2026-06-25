# 🌦️ Weather ETL Pipeline with Apache Airflow

## 📌 Project Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline that automatically collects weather data, cleans and transforms it, and stores it in a PostgreSQL database using Apache Airflow.

The workflow is fully automated using Airflow DAGs and developed in Python.

---

## 🚀 Technologies Used

- Python 3
- Apache Airflow
- PostgreSQL
- SQLAlchemy
- Requests
- Pandas
- Git & GitHub

---

## 📂 Project Structure

```
weather_ETL_pipeline/
│
├── dags/
│   └── weather_etl_dag.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── README.md
└── .gitignore
```

---

## 🔄 ETL Workflow

### 1. Extract
- Fetches weather data from a weather API.
- Saves the raw data.

### 2. Transform
- Cleans and processes the extracted weather data.
- Creates a structured dataset ready for loading.

### 3. Load
- Loads the cleaned weather data into PostgreSQL.

---

## ⚙️ Airflow DAG

The pipeline is scheduled and automated using Apache Airflow.

Task Flow:

```
Extract Weather
       ↓
Transform Weather
       ↓
Load Weather
```

---

## ▶️ How to Run

1. Clone the repository

```
git clone https://github.com/Manikant99-at/weather_ETL_pipeline.git
```

2. Install required packages

```
pip install -r requirements.txt
```

3. Start PostgreSQL.

4. Start Apache Airflow.

5. Trigger the DAG from the Airflow UI.

---

## 📊 Output

The pipeline:

- Extracts weather information
- Cleans and transforms the data
- Loads the processed data into PostgreSQL
- Runs automatically through Apache Airflow

---

## 👨‍💻 Author

**Manikanta Narayandas**

MSc Business Analytics & Data Science

GitHub: https://github.com/Manikant99-at
