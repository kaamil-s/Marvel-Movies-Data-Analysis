# Marvel Movies Data Analytics: Insights & Trends  

## Project Overview  
This project analyzes the Marvel Cinematic Universe (MCU) movies, focusing on revenue trends, profitability, and ratings. The goal is to uncover insights into how budget, revenue, and audience reception impact the success of MCU movies.  

## Dataset Overview  
- **Total Movies:** 33  
- **Columns:** Title, Budget, Worldwide Gross, Profit, Ratings (IMDb, Rotten Tomatoes, Letterboxd, etc.)  
- **Time Period:** 2008 - 2024

## Methodology  
### Phase 1: Data Acquisition  
- Loaded dataset from CSV  
- Inspected missing values and inconsistencies  

### Phase 2: Data Preprocessing  
- Converted `Release Date` to DateTime format  
- Created new columns:  
   - `Profit = Worldwide Gross - Budget`  
   - `Profit Margin = (Profit / Budget) * 100`  
- Cleaned missing/incorrect data  

### Phase 3: Data Analysis & Visualization  
**Budget vs. Revenue:**  
   - Higher-budget movies tend to perform better financially  
   - Some low-budget films have exceptional profit margins  

**Revenue Trends Over Time:**  
   - The MCU has seen a consistent increase in revenue over the years  

**Ratings Analysis:**  
   - Audience scores vs. critics' ratings show divergence  
   - Critics rate some movies lower than audiences do  

### Phase 4: Exporting for Power BI  
- Saved the cleaned dataset as `Marvel_Cleaned.csv` for Power BI visualization  

### Phase 5: Power BI Dashboard  
- Created interactive charts and dashboards showcasing:  
   - Revenue trends over time  
   - Budget vs. earnings  
   - Profit margins of top MCU movies  
   - Comparison of audience vs. critic ratings  

## Key Insights  
- High-budget movies generate more revenue, but some low-budget films have better profit margins  
- Critics vs. audience ratings differ—some movies are fan favorites but have lower critic scores  
- MCU revenue growth has been exponential due to its global reach and franchise expansion  

## Conclusion  
This analysis provides valuable insights into MCU movie trends. The Power BI dashboard enables further exploration of financial and audience data, making it an interactive and data-driven approach to understanding Marvel's success.  

---

Project Files & Code: Available in [GitHub Repository](https://github.com/kaamil-s/Marvel-Movies-Data-Analysis).  
