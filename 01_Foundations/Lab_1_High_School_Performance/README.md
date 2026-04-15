# Lab 1: High School Performance Analysis
**Level:** 🟢 Foundations  
**Tools:** Microsoft Excel · Power BI  
**Dataset:** 4,921 rows · Academic performance records from a Brazilian high school

---

## 🎯 Objective
Perform exploratory data analysis on a high school dataset to uncover patterns in student performance, course enrollment, and score distributions.

---

## 📋 Requirements Completed

| # | Requirement | Formula / Tool Used |
|---|-------------|---------------------|
| 1 | Total number of unique courses | `=COUNTA(UNIQUE(...))` |
| 2 | Total number of unique students | `=COUNTA(UNIQUE(...))` on Student ID column |
| 3 | Students enrolled in multiple courses | `COUNTIF` with `>1` condition |
| 4 | Average score per course & per student | `AVERAGEIF` |
| 5 | Top 5 students per course | Pivot Table with Top 10 filter (changed to 5) |
| 6 | Interactive visualisations | Power BI — 4 visuals (Bar, Donut, Line, Cards) |

---

## 🔍 Key Findings

- **56** unique courses and **115** unique students identified.
- All 115 students are enrolled in **39 courses simultaneously** — a significant course load that likely contributes to score variation.
- **Social Sciences IV** has the highest average score among all courses.
- Students from **Porto Alegre** slightly outperform those from **Viamao** on average.
- Average school-wide score: **7.48 / 10**

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `high_school_performance.xlsx` | Main Excel workbook with all analysis sheets |
| `generate_cheat_sheet.py` | Python script that generates the Excel Concepts CSV |
| `Excel_Concepts_Cheat_Sheet.csv` | Summary of all formulas learned during this lab |

---

## 💡 Lessons Learned

- Always use **whole columns** (e.g., `C:C`) in AVERAGEIF to prevent `#DIV/0!` errors when dragging formulas down.
- Power BI **cross-filtering** automatically isolates data when you click any visual — a feature, not a bug!
- Date columns must be set to **Date data type** in Power BI before they can be grouped by Year on a Line Chart.
