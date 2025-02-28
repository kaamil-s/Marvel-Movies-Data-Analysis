# -*- coding: utf-8 -*-
"""Marvel_Movie_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QGgJ6cigGK2qLVkVmJUm7v_vT9a1qdVY

## **Marvel Movies Data Analytics: Insights & Trends**

Analyzing budget, revenue, and profitability trends in the Marvel Cinematic Universe.  
Exploring audience ratings, revenue growth, and top-performing films with data visualization.

# Phase 1 : Data Acquisition

1.1 Upload and Load Dataset
"""

file_path = "/content/Marvel_Movies_Dataset.csv"
df = pd.read_csv(file_path)
df.head()

"""# Phase 2 : Data Preprocessing

**2.1 Check Data Types & Missing Values**
"""

print(df.info())  # Check data types
print(df.isnull().sum())  # Check for missing values

"""**2.2 Rename Columns for Easy Access**"""

df.rename(columns={
    'Index': 'Index',
    'Title': 'Title',
    'Director (1)': 'Director_1',
    'Director (2)': 'Director_2',
    'Release Date (DD-MM-YYYY)': 'Release_Date',
    'IMDb (scored out of 10)': 'IMDb',
    'IMDB Metascore (scored out of 100)': 'IMDB_Metascore',
    'Rotten Tomatoes - Critics (scored out of 100%)': 'Rotten_Tomatoes_Critics',
    'Rotten Tomatoes - Audience (scored out of 100%)': 'Rotten_Tomatoes_Audience',
    'Letterboxd (scored out of 5)': 'Letterboxd',
    'CinemaScore (grades A+ to F)': 'CinemaScore',
    'Budget (in million $)': 'Budget',
    'Domestic Gross (in million $)': 'Domestic_Gross',
    'Worldwide Gross (in million $)': 'Worldwide_Gross'
}, inplace=True)

# Print the new column names
print(df.columns)

"""**2.3 Convert Numeric Columns**
*   Convert Budget and Worldwide Gross to numeric values in dollars.
*   Convert Release Date to the proper datetime format.



"""

import pandas as pd

df['Budget'] = pd.to_numeric(df['Budget'], errors='coerce')
df['Worldwide_Gross'] = pd.to_numeric(df['Worldwide_Gross'], errors='coerce')

df['Release_Date'] = pd.to_datetime(df['Release_Date'], dayfirst=True, errors='coerce')

"""**2.4 Calculate Profit and Profit Margin**"""

df['Profit'] = df['Worldwide_Gross'] - df['Budget']
df['Profit_Margin'] = (df['Profit'] / df['Budget']) * 100

# Print the Profits and Profit Margins
print(df[['Profit', 'Profit_Margin']])

"""# Phase 3 : Exploratory Data Analysis & Visualization

"""

import matplotlib.pyplot as plt
import seaborn as sns

"""**3.1 Budget vs. Worldwide Gross**"""

# Create the grouped bar plot
ax = df.groupby('Title')[['Budget', 'Worldwide_Gross']].mean().plot(kind='bar', figsize=(14, 8), width=0.8, colormap='Set3')

# Add labels and title
ax.set_xlabel('Movie Title', fontsize=12)
ax.set_ylabel('Value (in millions)', fontsize=12)
ax.set_title('Average Budget and Worldwide Gross', fontsize=14)

# Rotate x-axis labels to avoid overlap (for long movie titles)
plt.xticks(rotation=90, ha="center", fontsize=10)

# Add gridlines for better readability
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

"""**3.2 Revenue Trends Over Time**"""

# Set the figure size for better clarity
plt.figure(figsize=(12, 6))

# Create the line plot
sns.lineplot(data=df, x="Release_Date", y ="Worldwide_Gross", marker='o')

# Set a plot title
plt.title("Worldwide Gross Revenue Over Time", fontsize=12)

# Rotate x-axis labels to prevent overlap (for date labels)
plt.xticks(rotation=45, ha="right", fontsize=10)

# Add gridlines for easier reading of the plot
plt.grid(True)

# Show the plot
plt.show()

"""**3.3 Ratings Comparison:**"""

# Create subplots for different platforms
# IMDb rating distribution (out of 10)
plt.subplot(2, 2, 1)
sns.histplot(df['IMDb'], kde=True, color='blue', bins=10)
plt.title('IMDb Rating Distribution')
plt.xlabel('IMDb Rating (Out of 10)')
plt.ylabel('Frequency')

# Rotten Tomatoes - Critics rating distribution (out of 100%)
plt.subplot(2, 2, 2)
sns.histplot(df['Rotten_Tomatoes_Critics'], kde=True, color='green', bins=10)
plt.title('Rotten Tomatoes - Critics Rating Distribution')
plt.xlabel('Rotten Tomatoes - Critics Rating (Out of 100%)')
plt.ylabel('Frequency')

# Letterboxd rating distribution (out of 5)
plt.subplot(2, 2, 3)
sns.histplot(df['Letterboxd'], kde=True, color='purple', bins=10)
plt.title('Letterboxd Rating Distribution')
plt.xlabel('Letterboxd Rating (Out of 5)')
plt.ylabel('Frequency')

# CinemaScore distribution (A+ to F grades)
plt.subplot(2, 2, 4)
sns.countplot(x='CinemaScore', data=df)
plt.title('CinemaScore Distribution')
plt.xlabel('CinemaScore')
plt.ylabel('Frequency')

# Show the plot
plt.tight_layout()
plt.show()

"""**3.4 Profitability Analysis**"""

# Create the bar plot for the top 5 profitable movies
top_profitable = df.nlargest(10, 'Profit')
plt.figure(figsize=(10, 6))

# Plot the bar plot
sns.barplot(data=top_profitable, x="Title", y="Profit", hue="Title", palette="viridis", legend=False)

# Add title and labels with enhanced font size
plt.title("Top 5 Most Profitable Movies", fontsize=16)
plt.xlabel('Movie Title', fontsize=12)
plt.ylabel('Profit (in millions)', fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha="right", fontsize=10)

# Add gridlines for better readability
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

"""# Phase 4 : Export Data for Power BI Dashboard"""

df.to_csv("/content/Marvel_Cleaned.csv", index=False)

"""# Phase 5 : Create Power BI Dashboard"""