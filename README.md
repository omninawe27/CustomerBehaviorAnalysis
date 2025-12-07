# CustomerBehaviorAnalysis

## Project Overview

**CustomerBehaviorAnalysis** leverages transactional data from 3,900 purchases to uncover actionable insights in spending patterns, customer segments, product preferences, and subscription behaviors. The repository contains Python scripts, SQL queries, and visualizations to help drive strategic decisions in retail and e-commerce.

---

## 📊 Dataset Description

- **Rows:** 3,900
- **Columns:** 18
- **Key Features:**
  - **Customer demographics:** Age, Gender, Location, Subscription Status
  - **Purchase details:** Item Purchased, Category, Purchase Amount, Season, Size, Color
  - **Shopping behavior:** Discount Applied, Promo Code Used, Previous Purchases, Frequency of Purchases, Review Rating, Shipping Type
- **Missing Data:** 37 values in `Review Rating` column (handled in preprocessing)

---

## 🛠️ Methodology

### 1. **Data Preparation (Python)**
- **Import & Exploration:** Dataset imported using `pandas`, structure examined using `.info()` and `.describe()`.
- **Missing Value Imputation:** Null values in `Review Rating` imputed using median rating per product category.
- **Standardization:** Columns renamed to snake_case for clarity.
- **Feature Engineering:** Created `age_group` bins and calculated `purchase_frequency_days`.
- **Consistency Checks:** Dropped redundant columns after correlation analysis.

### 2. **Relational Database Integration**
- Cleaned DataFrame loaded into PostgreSQL for advanced SQL analytics.

### 3. **Business Transaction Analysis (SQL)**
- **Revenue by Gender:** Compared total revenue from male vs. female customers.
- **High-Spending Discount Users:** Identified customers who used discounts but still spent above average.
- **Top Products:** Determined top 5 products with highest review ratings.
- **Shipping Type:** Benchmarked average purchase amount for Standard vs. Express shipping.
- **Subscriber Value:** Analyzed differences between subscribers and non-subscribers.
- **Discount Patterns:** Found products most dependent on discounts.
- **Segmentation:** Classified customers as New, Returning, or Loyal.
- **Top Products by Category:** Listed most purchased items in each category.
- **Repeat Buyers & Subscription Link:** Correlated high purchase frequency with subscriptions.
- **Age Group Revenue:** Calculated revenue contributions per age group.

### 4. **Interactive Dashboard (Power BI)**
- Power BI dashboard visualizes key KPIs:
  - Revenue, segmentation, product ratings
  - Filters by demographic, purchase features, and more
  - Drill-downs and visual summaries for strategic insights

---

## 📄 Enhanced PDF Report

`Customer Shopping Behavior Analysis.pdf` now includes:
- **Modern Fonts & Layout:** Improved clarity and professionalism
- **Bookmarks & Clickable Sections:** Easily navigate analysis questions and recommendations
- **Hyperlinked Insights:** Jump to dashboard or business conclusion of interest
- **Annotated Visuals:** Highlight Power BI interactive features

_**Tip:** Open the PDF in a full-featured reader (i.e., Adobe Acrobat) for clickable contents and bookmarks._

---

## 🎯 Key Business Recommendations

- **Boost Subscriptions:** Promote exclusive perks for yearly/monthly subscribers.
- **Loyalty Rewards:** Reward repeat purchasers with tiered loyalty benefits.
- **Optimize Discounts:** Adjust discounting strategy for margin control.
- **Campaign Focus:** Highlight best-rated and top-selling products in marketing.
- **Targeted Outreach:** Prioritize high-value age groups and users of Express shipping for campaigns.

---

## 📂 Repository Contents

- `Customer Shopping Behavior Analysis.pdf`: Interactive report and insights
- `scripts/`: Python notebooks for analysis
- `sql/`: PostgreSQL queries for business analysis
- `powerbi/`: Dashboard files and visualizations (if applicable)

---

## 🚀 Get Started

1. **Review the enhanced PDF** for project findings and recommendations.
2. **Explore scripts and SQL queries** for technical implementation.
3. **Run Power BI dashboard** to interact with data visuals (_see instructions in powerbi folder_).

---

## 📬 Contact & Contribution

Questions, suggestions, or contributions? Open an issue or submit a pull request!

---