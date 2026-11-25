# Assignment 09 — End-to-End Data Analysis Workflow

This assignment demonstrates an end-to-end data analysis workflow using Python and Jupyter Notebooks. It covers loading data from multiple sources, cleaning and preparing datasets, performing exploratory analysis, visualizing patterns, and summarizing insights.

## 📁 Folder Structure

```text
assignment-09/
├── supermarket_sales.csv
├── train.json
├── weather_forecast_data.csv
├── task-01/
│   └── load-data-csv.ipynb
├── task-02/
│   └── load-data-json.ipynb
├── task-03/
│   ├── load-data-sql.ipynb
│   └── sample.db
├── task-04/
│   ├── movie-data-collector.ipynb
│   ├── tmdb_movies.csv
│   └── tmdb_top_rated.csv
├── task-05/
│   └── understanding-the-data.ipynb
├── task-06/
│   └── data-cleaning.ipynb
├── task-07/
│   └── feature-preparation.ipynb
├── task-08/
│   └── univariate-analysis.ipynb
├── task-09/
│   └── bivariate-analysis.ipynb
├── task-10/
│   └── insights-and-observation.ipynb
└── README.md
```

## 📋 Tasks

| Task | Description | Dataset |
|------|-------------|---------|
| Task 01 | Load and inspect data from a CSV file | `weather_forecast_data.csv` |
| Task 02 | Load and inspect data from a JSON file | `train.json` |
| Task 03 | Query and load data from a SQL database | `sample.db` |
| Task 04 | Collect movie data through the TMDB API and export it to CSV | `tmdb_movies.csv`, `tmdb_top_rated.csv` |
| Task 05 | Understand dataset structure, data types, dimensions, and missing values | `supermarket_sales.csv` |
| Task 06 | Clean the data by handling missing and inconsistent values | `supermarket_sales.csv` |
| Task 07 | Prepare features using encoding and formatting techniques | `supermarket_sales.csv` |
| Task 08 | Univariate analysis: histograms, box plots, counts, pair plots, correlations | `supermarket_sales.csv` |
| Task 09 | Bivariate analysis: scatter plots, correlation heatmaps, category comparisons | `supermarket_sales.csv` |
| Task 10 | Compile observations and key insights from the analysis | — |

## 🛠️ Setup

1. Install Python 3.
2. Install Jupyter Notebook or JupyterLab.
3. Install the required libraries:

```bash
pip install pandas numpy requests matplotlib seaborn scikit-learn jupyter
```

4. Start Jupyter:

```bash
jupyter notebook
```

## ▶️ Run

Open the ten task notebooks in order and run all cells. Update dataset paths (for example `../supermarket_sales.csv`) and API credentials in the relevant notebook if needed.
