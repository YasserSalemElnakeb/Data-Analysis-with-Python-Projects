# Medical Data Visualizer 🩺📊

A Python data visualization project that analyzes medical examination data and explores relationships between health factors and cardiovascular disease.

This project is part of the **Data Analysis with Python Certification from freeCodeCamp**.

---

## 📌 Project Overview

The goal of this project is to analyze medical examination data and create visualizations that help understand the relationship between different health indicators.

The analysis focuses on exploring factors such as:

- Body Mass Index (BMI)
- Cholesterol Levels
- Glucose Levels
- Smoking Habits
- Physical Activity
- Cardiovascular Disease

---

## 📊 Visualizations Created

The project generates different types of charts to analyze the dataset.

### 1. Categorical Plot

A categorical visualization is created to compare health characteristics between people with and without cardiovascular disease.

Analyzed features include:

- Cholesterol
- Glucose
- Smoking
- Alcohol Consumption
- Physical Activity
- Overweight Category

---

### 2. Heatmap

A correlation heatmap is created to identify relationships between different medical variables.

The heatmap helps discover:

- Positive correlations
- Negative correlations
- Strong relationships between features

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
Medical-Data-Visualizer

│
├── medical_data_visualizer.py
├── medical_examination.csv
├── main.py
└── test_module.py
```

---

## 📄 Files Description

| File | Description |
|------|-------------|
| `medical_data_visualizer.py` | Contains functions for data processing and visualization |
| `medical_examination.csv` | Medical examination dataset used for analysis |
| `main.py` | Runs the project and displays generated charts |
| `test_module.py` | Contains unit tests to validate the solution |

---

## ⚙️ How It Works

The project follows these steps:

### 1. Data Loading

The medical dataset is loaded using Pandas:

```python
import pandas as pd
```

---

### 2. Data Processing

The data is prepared by:

- Adding calculated features
- Cleaning unnecessary values
- Transforming columns for visualization

Example:

Creating an overweight category based on BMI values.

---

### 3. Data Visualization

Using Matplotlib and Seaborn, the project creates:

- Categorical plots
- Correlation heatmaps

These visualizations help identify patterns and relationships in medical data.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YasserSalemElnakeb/Data-Analysis-with-Python-Projects.git
```

Navigate to the project folder:

```bash
cd Medical-Data-Visualizer
```

Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

---

## ▶️ How to Run

Run the main program:

```bash
python main.py
```

To run the tests:

```bash
python test_module.py
```

Expected result:

```text
.....
----------------------------------------------------------------------
Ran 5 tests

OK
```

---

## 🎯 Skills Demonstrated

Through this project, I practiced:

✅ Data Cleaning  
✅ Feature Engineering  
✅ Exploratory Data Analysis (EDA)  
✅ Data Visualization  
✅ Correlation Analysis  
✅ Working with Pandas DataFrames  
✅ Creating Visual Reports  

---

## 🎓 Certification

Completed as part of:

**freeCodeCamp - Data Analysis with Python Certification**

Topics Covered:

- Python Programming
- Pandas
- Matplotlib
- Seaborn
- Data Visualization

---

## 👨‍💻 Author

**Yasser Salem**

Data Analyst | Power BI Developer

GitHub:

https://github.com/YasserSalemElnakeb
