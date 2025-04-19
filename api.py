import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.API_KEY = "5dedd37e05ac9740cf1c181a6a84fc35"  # Replace with your actual key
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"  # Changed to HTTPS
        self.CITY = "Vijayawada"
        self.UNITS = "metric"
        self.weather_data = None

    def fetch_weather_data(self):
        """Fetch 5-day weather forecast data from OpenWeatherMap API"""
        params = {
            'q': self.CITY,
            'appid': self.API_KEY,
            'units': self.UNITS,
            'cnt': 40  # 5 days with 3-hour intervals
        }

        try:
            print(f"Attempting to fetch data from: {self.BASE_URL}")
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            self.weather_data = response.json()

            # Debug print to verify API response
            print("\nAPI Response Sample:")
            print(f"City: {self.weather_data['city']['name']}")
            print(f"First forecast point:")
            print(f"Time: {datetime.fromtimestamp(self.weather_data['list'][0]['dt'])}")
            print(f"Temp: {self.weather_data['list'][0]['main']['temp']}°C")

            return True

        except requests.exceptions.RequestException as e:
            print(f"\nError fetching data: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"API Response Status: {e.response.status_code}")
                print(f"API Error Message: {e.response.text}")
            return False

    def process_data(self):
        """Process raw API data into a structured DataFrame"""
        if not self.weather_data or 'list' not in self.weather_data:
            print("No valid data available to process")
            return None

        processed_data = []

        for forecast in self.weather_data['list']:
            timestamp = datetime.fromtimestamp(forecast['dt'])
            processed_data.append({
                'datetime': timestamp,
                'date': timestamp.strftime('%Y-%m-%d'),
                'time': timestamp.strftime('%H:%M'),
                'temperature': forecast['main']['temp'],
                'feels_like': forecast['main']['feels_like'],
                'temp_min': forecast['main']['temp_min'],
                'temp_max': forecast['main']['temp_max'],
                'humidity': forecast['main']['humidity'],
                'pressure': forecast['main']['pressure'],
                'wind_speed': forecast['wind']['speed'],
                'wind_deg': forecast['wind']['deg'],
                'weather': forecast['weather'][0]['main'],
                'description': forecast['weather'][0]['description'],
                'cloudiness': forecast['clouds']['all'],
                'rain': forecast.get('rain', {}).get('3h', 0),
                'snow': forecast.get('snow', {}).get('3h', 0)
            })

        df = pd.DataFrame(processed_data)
        print("\nSample processed data:")
        print(df[['datetime', 'temperature', 'weather', 'wind_speed']].head())
        return df

    def create_dashboard(self, df):
        """Create a comprehensive weather visualization dashboard"""
        if df is None or df.empty:
            print("No data available for visualization")
            return

        # Set style and create figure
        sns.set_style("darkgrid")
        plt.figure(figsize=(18, 12))
        plt.suptitle(f'5-Day Weather Forecast for {self.CITY}', fontsize=16, y=1.02)

        # Plot 1: Temperature and Feels Like
        plt.subplot(2, 2, 1)
        sns.lineplot(data=df, x='datetime', y='temperature', label='Temperature', marker='o')
        sns.lineplot(data=df, x='datetime', y='feels_like', label='Feels Like', marker='o')
        plt.title('Temperature vs Feels Like')
        plt.xlabel('Date and Time')
        plt.ylabel('Temperature (°C)')
        plt.xticks(rotation=45)
        plt.legend()

        # Plot 2: Humidity and Pressure
        plt.subplot(2, 2, 2)
        ax2 = plt.gca()
        sns.lineplot(data=df, x='datetime', y='humidity', color='green', label='Humidity', ax=ax2)
        ax2.set_ylabel('Humidity (%)', color='green')
        ax2.tick_params(axis='y', labelcolor='green')

        ax2b = ax2.twinx()
        sns.lineplot(data=df, x='datetime', y='pressure', color='blue', label='Pressure', ax=ax2b)
        ax2b.set_ylabel('Pressure (hPa)', color='blue')
        ax2b.tick_params(axis='y', labelcolor='blue')

        plt.title('Humidity and Pressure')
        plt.xlabel('Date and Time')
        plt.xticks(rotation=45)
        lines1, labels1 = ax2.get_legend_handles_labels()
        lines2, labels2 = ax2b.get_legend_handles_labels()
        ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

        # Plot 3: Wind Speed and Direction
        plt.subplot(2, 2, 3)
        sns.scatterplot(data=df, x='datetime', y='wind_speed',
                       hue='wind_deg', size='wind_speed',
                       palette='coolwarm', sizes=(50, 200))
        plt.title('Wind Speed and Direction')
        plt.xlabel('Date and Time')
        plt.ylabel('Wind Speed (m/s)')
        plt.xticks(rotation=45)
        plt.legend(title='Wind Direction (°)')

        # Plot 4: Weather Conditions
        plt.subplot(2, 2, 4)
        weather_counts = df['weather'].value_counts()
        plt.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%',
                startangle=90, colors=sns.color_palette('pastel'))
        plt.title('Weather Conditions Distribution')

        # Adjust layout
        plt.tight_layout()

        # Save and show
        plt.savefig('weather_dashboard.png', bbox_inches='tight', dpi=300)
        print("\nDashboard saved as 'weather_dashboard.png'")
        plt.show()

    def run(self):
        """Run the complete workflow"""
        if not self.API_KEY or len(self.API_KEY) != 32:
            print("Invalid API key format. Please check your API key.")
            return

        print(f"\nStarting weather data fetch for {self.CITY}...")
        if self.fetch_weather_data():
            df = self.process_data()
            if df is not None:
                print("\nCreating visualization dashboard...")
                self.create_dashboard(df)

if __name__ == "__main__":
    print("Starting Weather Dashboard Application...")
    dashboard = WeatherDashboard()
    dashboard.run()
    print("Application completed.")
