# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: LADI SRAVANI

*INTERN ID*: CT04WP176

*DOMAIN*: PYTHON

*DURATION*:4 WEEKS

*MENTOR*: NEELA SANTOSH

# API Integration and Data Visualization: 
This solution demonstrates how to fetch real-time weather data from the **OpenWeatherMap API** and visualize it using **Python** with **Matplotlib**, **Seaborn**, and **Dash** for interactive dashboards. The implementation includes data fetching, processing, static visualizations, and an interactive dashboard.  
---
## **1. API Integration**  
The script connects to the **OpenWeatherMap API** to retrieve a **5-day weather forecast** for a specified city (e.g., London). Key steps include:  
- **API Request:** Uses the `requests` library to fetch JSON data.  
- **Data Parsing:** Extracts temperature, humidity, wind speed, and weather conditions.  
- **DataFrame Conversion:** Structures the data into a **Pandas DataFrame** for analysis.  
### **Key Features:**  
 **Error Handling** – Catches API request failures (e.g., invalid API key, network issues).  
 **Dynamic Parameters** – Allows changing the city and units (metric/imperial).  
 **Time Conversion** – Converts UNIX timestamps to readable datetime formats.  
---
## **2. Data Visualization**  
The script generates **static plots** (Matplotlib/Seaborn) and an **interactive dashboard** (Dash).  
### **Static Visualizations (Matplotlib & Seaborn)**  
1. **Temperature Trend Line Plot** – Shows hourly temperature changes over 5 days.  
2. **Humidity Distribution (Seaborn Histogram)** – Displays humidity frequency.  
3. **Weather Condition Pie Chart** – Breaks down forecast conditions (e.g., Rain, Clouds, Clear).  
### **Interactive Dashboard (Dash)**  
A **web-based dashboard** with:  
- **Dropdown Filter** – Select weather metrics (temp, humidity, wind speed).  
- **Interactive Line Chart** – Hover tooltips for detailed data.  
- **Multi-Plot Layout** – Combines line, bar, and pie charts dynamically.  
---
## **3. Technical Implementation**  
### **Libraries Used**  
- **`requests`** – API data fetching  
- **`pandas`** – Data structuring  
- **`matplotlib` & `seaborn`** – Static plots  
- **`dash` (Plotly)** – Interactive dashboard  
### **Execution Workflow**  
1. **Fetch Data** → 2. **Clean & Structure** → 3. **Generate Plots** → 4. **Launch Dashboard**  
---
## **4. Expected Output**  
- **Static Plots** (Saved as `.png` files)  
- **Interactive Dashboard** (Accessible via `http://127.0.0.1:8050`)  
---
## **Conclusion**  
This solution provides a **complete pipeline** from API integration to visualization, suitable for **real-time weather monitoring, analytics, and reporting**. The modular design allows easy adaptation for other APIs (e.g., financial, IoT, or social media data).  
**Enhancements Possible:**  
- **Live Data Updates** (Auto-refresh every hour)  
- **Geographical Maps** (Plotly for location-based weather)  
- **Predictive Analysis** (ML models for weather forecasting)  
By following this approach, users can **extract insights from API data efficiently** and present them in **static reports or dynamic dashboards**.  

#OUTPUT#:
![Image](https://github.com/user-attachments/assets/68fda8ce-9ac6-4313-afbf-ab64227d692e)

![Image](https://github.com/user-attachments/assets/1706fd11-ca3f-4ae9-9236-4ad80189cc2a)
