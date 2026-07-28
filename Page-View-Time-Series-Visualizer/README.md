# Page View Time Series Visualizer 📈

A Python data visualization project that analyzes daily page views from the **freeCodeCamp forum** using time series analysis techniques.

This project is part of the **Data Analysis with Python Certification from freeCodeCamp**.

---

## 📌 Project Overview

The goal of this project is to visualize and analyze the growth of daily page views over time.

The dataset contains daily page view counts from the freeCodeCamp forum between:

**May 2016 - December 2019**

The project focuses on discovering:

- Growth trends
- Yearly patterns
- Monthly seasonality
- Changes in user activity over time

---

## 📊 Visualizations Created

The project creates three different types of visualizations:

---

## 1. Line Chart

A line chart is created to display daily page views over the entire period.

It helps analyze:

- Overall growth trend
- Traffic changes over time
- Long-term patterns

---

## 2. Bar Chart

A yearly bar chart is created to show the average daily page views for each month grouped by year.

It helps compare:

- Monthly performance
- Yearly growth
- Seasonal differences

---

## 3. Box Plots

Two box plots are created to analyze:

### Yearly Data

Shows how page views changed each year.

### Monthly Data

Shows seasonal patterns and differences between months.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
Page-View-Time-Series-Visualizer

│
├── time_series_visualizer.py
├── fcc-forum-pageviews.csv
├── main.py
└── test_module.py
```

---

## 📄 Files Description

| File | Description |
|------|-------------|
| `time_series_visualizer.py` | Contains functions for creating charts and analyzing time series data |
| `fcc-forum-pageviews.csv` | Dataset containing daily forum page views |
| `main.py` | Runs the project and generates visualizations |
| `test_module.py` | Contains unit tests to verify the solution |

---

## ⚙️ How It Works

The project follows a time series analysis workflow:

### 1. Data Loading

The dataset is loaded using Pandas:

```python
import pandas as pd
```

---

### 2. Data Cleaning

The data is prepared by:

- Converting dates into the correct format
- Removing incorrect values
- Filtering extreme outliers

---

### 3. Data Visualization

The cleaned data is visualized using:

- Line charts
- Bar charts
- Box plots

These charts help identify trends and seasonal behavior.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YasserSalemElnakeb/Data-Analysis-with-Python-Projects.git
```

Navigate to the project folder:

```bash
cd Page-View-Time-Series-Visualizer
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

✅ Time Series Analysis  
✅ Data Cleaning  
✅ Date Manipulation with Pandas  
✅ Data Visualization  
✅ Trend Analysis  
✅ Seasonal Pattern Detection  
✅ Exploratory Data Analysis (EDA)

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
- Time Series Analysis

---

## 👨‍💻 Author

**Yasser Salem**

Data Analyst | Power BI Developer

GitHub:

https://github.com/YasserSalemElnakeb
