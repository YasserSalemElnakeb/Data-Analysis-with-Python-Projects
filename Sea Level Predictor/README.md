# Sea Level Predictor 🌊📈

A Python data analysis and predictive modeling project that studies global sea level rise data and predicts future sea level changes using linear regression.

This project is part of the **Data Analysis with Python Certification from freeCodeCamp**.

---

## 📌 Project Overview

The goal of this project is to analyze historical sea level rise data and create a prediction model to estimate future sea level changes.

The dataset contains global sea level measurements collected between:

**1880 - 2014**

The project uses statistical analysis and machine learning techniques to predict the expected sea level rise by:

**2050**

---

## 📊 Analysis Performed

The project performs the following steps:

### 1. Data Loading

The historical sea level data is loaded using Pandas.

The dataset includes:

- Year
- Sea Level Rise Measurements

---

### 2. Data Visualization

A scatter plot is created to visualize:

- Historical sea level changes
- Long-term rising trends

---

### 3. Linear Regression Modeling

Two regression lines are created:

### First Line

A linear regression model using all available historical data.

### Second Line

A regression model using data from recent years to better represent the current acceleration trend.

---

### 4. Future Prediction

The regression models are extended to predict future sea level rise until:

**2050**

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- SciPy

---

## 📂 Project Structure

```
Sea Level Predictor

│
├── sea_level_predictor.py
├── epa-sea-level.csv
├── main.py
└── test_module.py
```

---

## 📄 Files Description

| File | Description |
|------|-------------|
| `sea_level_predictor.py` | Contains data analysis and regression prediction functions |
| `epa-sea-level.csv` | Historical sea level rise dataset |
| `main.py` | Runs the project and displays the prediction chart |
| `test_module.py` | Contains unit tests to verify the solution |

---

## ⚙️ How It Works

The project follows a predictive analysis workflow:

### 1. Data Preparation

The dataset is loaded and prepared using Pandas.

---

### 2. Exploratory Analysis

The historical data is visualized to understand the relationship between:

- Time
- Sea level changes

---

### 3. Regression Model

The project uses:

```python
scipy.stats.linregress()
```

to calculate:

- Slope
- Intercept
- Correlation values

---

### 4. Prediction

The regression model is used to estimate future sea level rise and visualize the expected trend.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YasserSalemElnakeb/Data-Analysis-with-Python-Projects.git
```

Navigate to the project folder:

```bash
cd "Sea Level Predictor"
```

Install the required libraries:

```bash
pip install pandas matplotlib scipy
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

✅ Data Analysis with Pandas  
✅ Data Visualization  
✅ Statistical Analysis  
✅ Linear Regression  
✅ Predictive Modeling  
✅ Working with Real-World Datasets  
✅ Data Storytelling

---

## 🎓 Certification

Completed as part of:

**freeCodeCamp - Data Analysis with Python Certification**

Topics Covered:

- Python Programming
- Pandas
- Matplotlib
- SciPy
- Data Visualization
- Statistical Modeling

---

## 👨‍💻 Author

**Yasser Salem**

Data Analyst | Power BI Developer

GitHub:

https://github.com/YasserSalemElnakeb
