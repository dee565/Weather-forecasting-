# Weather Forecasting System

A beginner-friendly Python Flask project that displays current weather for a city using the OpenWeatherMap API.

## Requirements
- Python 3.10 or later
- VS Code
- Internet connection
- Free OpenWeatherMap API key: https://openweathermap.org/api

## Run in VS Code (Windows)

1. Extract the ZIP file.
2. Open the `Weather_Forecasting` folder in VS Code.
3. Open the VS Code terminal: **Terminal → New Terminal**.
4. Create a virtual environment:

   ```powershell
   py -m venv venv
   ```

5. Activate it:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt in VS Code and run:

   ```cmd
   venv\Scripts\activate.bat
   ```

6. Install the required packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. Create a free API key at https://openweathermap.org/api.
8. Open `app.py` and replace `YOUR_API_KEY_HERE` with your API key.
9. Start the project:

   ```powershell
   python app.py
   ```

10. Open this address in your browser: http://127.0.0.1:5000

## Features
- Search by city name
- Current temperature in Celsius
- Feels-like temperature
- Humidity
- Wind speed
- Weather description and icon

## Note
This starter project shows **current weather**, not a multi-day forecast. The API key is required for live results. Do not upload your API key to a public GitHub repository.
