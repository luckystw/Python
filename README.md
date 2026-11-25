# Generative AI Assignments

A hands-on collection of Python and data-science exercises, organized by assignment and task. Each assignment is self-contained, so you can work through them in order or jump to any topic.

## Repository Structure

```text
GEN-AI-Assignments-GitHub/
├── assignment-01/   # Python collections
├── assignment-02/   # Control flow
├── assignment-03/   # Functions
├── assignment-04/   # File handling
├── assignment-05/   # Modules and packages
├── assignment-06/   # Exception handling
├── assignment-07/   # Object-oriented programming
├── assignment-08/   # Application exercises
├── assignment-09/   # NumPy
├── assignment-10/   # Pandas
├── assignment-11/   # Matplotlib
├── assignment-12/   # Seaborn
├── assignment-13/   # End-to-end data analysis workflow
├── README.md
└── .gitignore
```

## What's Covered

### Python Foundations

| # | Topic | Exercises |
|---|-------|-----------|
| 01 | Collections | Products, categories, pricing, combined operations |
| 02 | Control Flow | Discount rules, multi-order processing, user menu, loop control |
| 03 | Functions | Basic, recursive, and lambda functions; `map` and `filter`; utility functions; menu-driven programs |
| 04 | File Handling | Sales records, reading and appending data, summary reports, safe file reading, exporting discounted prices |
| 05 | Modules and Packages | Custom modules, utility modules, package imports, billing and discount modules |
| 06 | Exception Handling | Safe division, bill calculator, age validator, file reader, safe shopping cart |
| 07 | Object-Oriented Programming | Classes, encapsulation, inheritance, polymorphism, abstraction, magic methods, operator overloading, inventory system |
| 08 | Applications | Basic app, discount app, product form, dashboard |

### Data Analysis and Visualization

| # | Topic | Exercises |
|---|-------|-----------|
| 09 | NumPy | Arrays, math operations, aggregation, statistics, percentiles, sorting, sales analysis |
| 10 | Pandas | Series, DataFrames, filtering, grouping, plotting, sales data analysis |
| 11 | Matplotlib | Line, scatter, bar (grouped and stacked), histogram, and pie charts; sales data visualization |
| 12 | Seaborn | Relational, distribution, matrix, categorical, and regression plots; multi- and figure-level plots (uses `Housing.csv`) |
| 13 | Data Analysis Workflow | Loading data from CSV, JSON, SQL, and the TMDB API; cleaning, feature preparation, univariate and bivariate analysis, insights (uses `supermarket_sales.csv`) |

<details>
<summary>Assignment 12 task breakdown</summary>

- **Task 01:** Relational plot
- **Task 02:** Line plot as scatter and facet
- **Task 03:** Distribution plot
- **Task 04:** Bivariate distribution plot
- **Task 05:** Matrix plots (pair plot and correlation heatmap)
- **Task 06:** Categorical plot
- **Task 07:** Regression plot
- **Task 08:** Multi- and figure-level plots

</details>

<details>
<summary>Assignment 13 task breakdown</summary>

- **Task 01:** Load data from a CSV file
- **Task 02:** Load data from a JSON file
- **Task 03:** Query data from a SQL (SQLite) database
- **Task 04:** Collect movie data from the TMDB API and export to CSV
- **Task 05:** Understand the data (structure, types, dimensions, missing values)
- **Task 06:** Data cleaning
- **Task 07:** Feature preparation (encoding and formatting)
- **Task 08:** Univariate analysis
- **Task 09:** Bivariate analysis
- **Task 10:** Insights and observations

</details>

## Tech Stack

Python · Jupyter Notebook · NumPy · Pandas · Matplotlib · Seaborn · Requests · scikit-learn · SQLite

## Getting Started

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd GEN-AI-Assignments-GitHub
```

**2. (Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install jupyter numpy pandas matplotlib seaborn requests scikit-learn
```

**4. Launch Jupyter**

```bash
jupyter notebook
```

Open any `.ipynb` file from an assignment folder and run the cells in order.

> **Note:** Assignment 13, Task 04 calls the TMDB API. Set your own key as an environment variable (`TMDB_API_KEY`) instead of hard-coding it in the notebook.

## Naming Conventions

- Folders: `assignment-01`, `assignment-02`, …
- Tasks: `task-01`, `task-02`, …
- Files: lowercase kebab-case (e.g. `sales-analysis.ipynb`)
