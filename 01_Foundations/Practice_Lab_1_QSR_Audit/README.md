# Practice Lab 1: QSR Performance Audit
**Level:** 🟢 Foundations  
**Tools:** Microsoft Excel  
**Dataset:** 20 restaurant transactions · 5 employees · 4 product categories

---

## 🎯 Objective
An independent, self-directed practice lab. Applied all Excel formulas learned in Lab 1 — without assistance — to a mock Quick Service Restaurant (QSR) dataset to audit employee performance and product ratings.

---

## 📋 Requirements Completed

| # | Requirement | Formula Used | Answer |
|---|-------------|-------------|--------|
| 1 | How many unique employees worked today? | `COUNTA + UNIQUE` | **5** |
| 2 | How many unique product categories were sold? | `COUNTA + UNIQUE` | **4** |
| 3 | List of Employee IDs with matching Names | `XLOOKUP` | All 5 matched ✅ |
| 4 | How many orders did "Ali" handle? | `COUNTIF` (cross-sheet) | **5 orders** |
| 5 | Average customer rating for "Burgers" | `AVERAGEIF` | **3.83 / 5** |
| 6 | Top 3 employees by total revenue | Pivot Table + Top 10 filter | Ali · Bilal · Zain |

---

## 🔍 Key Findings

- **Ali** handled the most orders (5 out of 20) but **Bilal** generated more revenue per order due to higher Pizza sales.
- **Burgers** received the lowest average rating (3.83), while **Fries** received the highest (4.6).
- **Pizzas** drive the most revenue per transaction (avg. ~2,500 PKR) despite moderate ratings.

---

## 💡 Lessons Reinforced

- Cross-sheet references (`SheetName!Column:Column`) are essential when your data lives on a separate tab.
- **Absolute references (`$`)** must be used when dragging formulas down to prevent the "Moving Shopping List" bug.
- The `#DIV/0!` error always means Excel is trying to divide by zero — usually because the search range has slipped into empty rows.
