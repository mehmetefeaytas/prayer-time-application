# Prayer Time Application

The Prayer Time Application is a Tkinter-based interface that allows users to obtain daily prayer times for a selected city. The app provides a user-friendly experience, enabling language and city selection.

## Features

- **Language Selection**: Choose between Turkish, English, and Arabic.
- **City Selection**: Enter the city name to receive prayer times.
- **Real-Time Data**: Fetches up-to-date prayer times using the Aladhan API.
- **User-Friendly Interface**: Offers a simple and intuitive GUI built with Tkinter.

## Requirements

### Software Requirements

- **Python 3.x**: The application is developed in Python.
- **Tkinter**: A GUI library that comes with Python.
- **Requests**: An HTTP library used for API calls.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mehmetefeaytas/prayer-time-application.git
   cd prayer-time-application

	2.	Install Required Libraries:

         pip install requests



Usage

	1.	Start the Application:
Run the following command in your terminal or command prompt:

python main.py


	2.	Select Language and City:
	•	In the opened window, select a language from the dropdown menu.
	•	Enter the name of the city for which you want to receive prayer times.
	3.	Fetch Prayer Times:
	•	Click the “Start Application” button to retrieve the prayer times.
	•	The application will print the fetched data to the console.

Code Explanation

Below is the core structure of the application code and its components:

Importing Libraries

import tkinter as tk
from tkinter import ttk
import requests
import json
from datetime import date

	•	tkinter: Used for creating the GUI (Graphical User Interface).
	•	requests: Used for making HTTP requests.
	•	json: Used for processing JSON data.
	•	date: Used for date handling.

Functions

get_prayer_times()

This function is called to fetch prayer times for the selected city.

def get_prayer_times():
    city = selected_city.get()
    today = date.today().strftime("%d-%m-%Y")
    api_url = f"https://api.aladhan.com/v1/timingsByAddress/{today}?address={city}"
    response = requests.get(api_url)
    
    try:
        data = response.json()
        print(data)  # Print prayer times to console
    except ValueError as e:
        print(f"Error parsing JSON: {e}")

	•	API Call: Sends a request to the API with the user’s selected city and today’s date.
	•	Error Handling: Prints an error message to the console if JSON parsing fails.

start_application()

This function manages the application’s startup processes.

def start_application():
    get_prayer_times()

main()

The main application function that creates GUI components and starts the application.

def main():
    global selected_language, selected_city

    root = tk.Tk()
    root.title("Prayer Time Application")
    
    # Language Selection
    tk.Label(root, text="Select Language / Dil Seçin / اختر اللغة:").grid(column=0, row=0, padx=10, pady=10)
    selected_language = tk.StringVar(value="tr")
    languages = {"Turkish": "tr", "English": "en", "Arabic": "ar"}
    language_combobox = ttk.Combobox(root, textvariable=selected_language, values=list(languages.keys()), state="readonly")
    language_combobox.grid(column=1, row=0, padx=10, pady=10)

    # City Selection
    tk.Label(root, text="Choose City / Şehir Seçin / اختر المدينة:").grid(column=0, row=1, padx=10, pady=10)
    selected_city = tk.StringVar()
    city_entry = tk.Entry(root, textvariable=selected_city)
    city_entry.grid(column=1, row=1, padx=10, pady=10)

    # Start Button
    start_button = tk.Button(root, text="Start Application / Uygulamayı Başlat / ابدأ التطبيق", command=start_application)
    start_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    root.mainloop()

	•	Tkinter Window: Creates the application window.
	•	Adding Components: Creates labels, entry fields, and buttons for language and city selection.
	•	Event Handling: Calls the start_application function when the button is clicked.

Contributing

If you would like to contribute, please follow these steps:

	1.	Fork the repository.
	2.	Make your changes.
	3.	Open a pull request.

License

This project is licensed under the MIT License. For more details, please check the LICENSE file.
