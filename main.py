import tkinter as tk
from tkinter import ttk
import requests
import json
from datetime import date

def get_prayer_times():
    city = selected_city.get()
    today = date.today().strftime("%d-%m-%Y")
    api_url = f"https://api.aladhan.com/v1/timingsByAddress/{today}?address={city}"
    response = requests.get(api_url)
    
    try:
        data = response.json()
        # Process the prayer times data here
        print(data)
    except ValueError as e:
        print(f"Error parsing JSON: {e}")

def start_application():
    get_prayer_times()

def main():
    global selected_language, selected_city

    # Tkinter ile bir pencere oluşturuyoruz
    root = tk.Tk()
    root.title("Ezan Vakti Uygulaması")

    # Dil Seçimi
    tk.Label(root, text="Dil Seçin / Choose Language / اختر اللغة:").grid(column=0, row=0, padx=10, pady=10)
    selected_language = tk.StringVar(value="tr")
    languages = {"Türkçe": "tr", "English": "en", "العربية": "ar"}
    language_combobox = ttk.Combobox(root, textvariable=selected_language, values=list(languages.keys()), state="readonly")
    language_combobox.grid(column=1, row=0, padx=10, pady=10)

    # Şehir Seçimi
    tk.Label(root, text="Şehir Seçin / Choose City / اختر المدينة:").grid(column=0, row=1, padx=10, pady=10)
    selected_city = tk.StringVar()
    city_entry = tk.Entry(root, textvariable=selected_city)
    city_entry.grid(column=1, row=1, padx=10, pady=10)

    # Başlat Butonu
    start_button = tk.Button(root, text="Uygulamayı Başlat / Start Application / ابدأ التطبيق", command=start_application)
    start_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
