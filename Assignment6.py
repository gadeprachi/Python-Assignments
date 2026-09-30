from io import StringIO
import pandas as pd


# ========from========================================================
# 1. DATA INITIALIZATION
# Creating structured employee dataset containing department, role,
# salary, and performance metrics.
# ================================================================

raw_csv_data = """
EmployeeID,Name,Department,Role,Salary,Bonus,Performance_Rating,Projects_Completed
101,Alice,Engineering,Developer,95000,12000,4.5,8
102,Bob,Engineering,Developer,78000,10000,3.8,6
103,Charlie,Engineering,Manager,120000,20000,4.8,9
104,David,Data,Executive,68000,15000,4.2,12
105,Eve,Data,Executive,65000,11000,3.9,10
106,Frank,Sales,Manager,90000,18000,4.1,7
107,Grace,Marketing,Specialist,48000,5000,4.0,5
108,Hannah,Marketing,Specialist,46000,4500,3.6,4
109,Ivy,Marketing,Manager,102000,16000,4.7,8
"""

# Load CSV string into Pandas DataFrame
df = pd.read_csv(StringIO(raw_csv_data.strip()))

print("--- Original Employee Dataset ---")
print(df)
print("\n" + "=" * 80 + "\n")


# ================================================================
# 2. BASIC GROUPING & SINGLE AGGREGATION
# Grouping by a single categorical column ('Department') and
# calculating average metrics.
# ================================================================

print("--- Concept 1: Basic Grouping (Average Salary & Bonus per Department) ---")

# Group by Department and compute the mean
dept_means = df.groupby("Department")[["Salary", "Bonus"]].mean()

# Formatting output values for clarity
dept_means_formatted = dept_means.round(2)
print(dept_means_formatted)

print("\n" + "=" * 80 + "\n")


# ================================================================
# 3. MULTI-COLUMN GROUPING
# Grouping by multiple categorical variables ('Department' and
# 'Role') to analyze metrics at a finer hierarchy level.
# ================================================================

print("--- Concept 2: Multi-Column Grouping (Average Salary by Dept & Role) ---")

# Multi-level grouping
role_hierarchy = (
    df.groupby(["Department", "Role"])[["Salary", "Performance_Rating"]]
    .mean()
    .round(2)
)

print(role_hierarchy)
print("\n" + "=" * 80 + "\n")


# ================================================================
# 4. ADVANCED AGGREGATION USING .agg()
# Applying multiple aggregation functions (sum, mean, max)
# to different columns simultaneously.
# ================================================================

print("--- Concept 3: Advanced Aggregation using .agg() ---")

# Dictionary mapping specific columns to desired statistical operations
agg_operations = {
    "Salary": ["mean", "min", "max"],
    "Bonus": "sum",
    "Projects_Completed": "sum",
    "Performance_Rating": "mean"
}

dept_summary = df.groupby("Department").agg(agg_operations).round(2)

print(dept_summary)

print("\n" + "=" * 80 + "\n")
