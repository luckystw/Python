# Assignment 12 — Data Visualization with Seaborn

This assignment covers data visualization using the **Housing dataset** with Python, Seaborn, and Matplotlib.

## 📁 Folder Structure

```text
assignment-12/
├── Housing.csv
├── task-01/
│   └── relational-plot.ipynb
├── task-02/
│   └── line-plot-as-scatter-and-facet.ipynb
├── task-03/
│   └── distribution-plot.ipynb
├── task-04/
│   └── bivariate-distribution-plot.ipynb
├── task-05/
│   └── matrix-plot.ipynb
├── task-06/
│   └── categorical-plot.ipynb
├── task-07/
│   └── regression-plot.ipynb
├── task-08/
│   └── multi-and-figure-level-plots.ipynb
└── README.md
```

## 📋 Tasks

| Task | Topic | Plots Used |
|------|-------|-----------|
| Task 01 | Relational Plot | `relplot` (scatter, hue by furnishing status) |
| Task 02 | Line Plot as Scatter and Facet | `lineplot`, `scatterplot`, `relplot` with `col` facets |
| Task 03 | Distribution Plot | `histplot`, `kdeplot`, `rugplot`, histogram with KDE |
| Task 04 | Bivariate Distribution Plot | 2D `histplot`, 2D `kdeplot` |
| Task 05 | Matrix Plot | `pairplot`, correlation `heatmap` |
| Task 06 | Categorical Plot | `barplot`, `boxplot`, `violinplot`, `countplot` |
| Task 07 | Regression Plot | `regplot`, `lmplot` |
| Task 08 | Multi- and Figure-Level Plots | `FacetGrid`, `relplot`, `catplot`, `displot` |

## 🛠️ Technologies Used

- **Python**
- **Jupyter Notebook**
- **Pandas**
- **Seaborn**
- **Matplotlib**

## 🚀 How to Run

```bash
pip install jupyter pandas seaborn matplotlib
jupyter notebook
```

Open any task notebook. The notebooks load `Housing.csv` from this folder, so make sure the file path in the `pd.read_csv(...)` cell points to it (for example `../Housing.csv` from inside a task folder).
