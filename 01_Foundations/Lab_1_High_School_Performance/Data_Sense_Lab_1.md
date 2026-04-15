# Data Sense: Lab 1 — High School Performance

**The Goal:** Learn how to look at a raw dataset (5000+ rows) and figure out *what* to chart, *why* we chart it, and *how* to present the findings to a manager.

---

## 🏗️ The 4-Step Blueprint (How to think like an Analyst)

When handed a new, blank dataset, ask yourself these 4 questions before building anything in Power BI:

### 1. What is the "Hero Metric"?
Every dataset has one column that matters more than anything else. It’s the ultimate measure of success or failure.
*   **In this Lab:** The hero metric is **`result`** (the academic score).
*   **Action:** This goes into a Card visual (for the overall average) and forms the Y-axis or 'Values' box of almost every other chart.

### 2. What are the "Slicers"?
Look for categorical columns that group your data into buckets. You want to "slice" the hero metric up to see who is performing well and who isn't.
*   **Categories:** `academic_course` (Lets us slice scores by subject).
*   **Geography:** `address_student` (Lets us slice scores by city).
*   **Time/Demographics:** `birth_date_student` (Lets us slice scores by age/year).

### 3. Match the Slicer to the Chart Type
*   **Time/Dates?** → **Line Chart** (Shows trends over time).
*   **Categories?** → **Bar Chart** (Best for comparing different groups).
*   **Geography/Locations?** → **Map** or **Donut/Pie Chart** (Shows distribution by area).

### 4. The "So What?" (Writing your Findings)
Nobody cares about a chart if it doesn't solve a problem. Writing findings involves three steps:
1.  **Find the anomaly:** Look at your charts. Which bar is way lower than the others? Which year dropped off?
2.  **State the finding:** *"Students taking Mathematics IV have a significantly lower average (5.2) compared to the school average (7.4)."*
3.  **Give a recommendation:** *"Recommendation: Investigate the Math IV curriculum or teaching staff, and consider offering tutoring for this specific subject, as it is dragging down overall school performance."*

---

## 🛠️ Power BI Cross-Filtering (The "Secret Feature")

In Power BI, everything is connected. 
*   If you click on a single dot in a Line Chart (e.g., a student born on March 3, 2004), the **entire dashboard** filters to show the story for that specific dot.
*   Suddenly your total students card drops to `1`, and your bar chart only shows the courses that one student took.
*   **The Fix:** Click on any blank white space in the visual to un-filter and return to the global view.

---

## 📅 Fixing Dates in Power BI
If a line chart looks like a jagged mess of individual days, Power BI probably thinks your Date column is just "Text."
1. Go to the Data pane.
2. Select the date column.
3. In 'Column tools', change the **Data type** from Text to **Date**.
4. In your visual's Axis settings, ensure you select **Date Hierarchy** (Year, Quarter, Month, Day) instead of the raw date.
[[Analytics_Workspace_Context]]