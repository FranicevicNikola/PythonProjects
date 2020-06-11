from tkinter import *
import requests
import sys
print(sys.version)
tk = Tk()
tk.title('Weather')


zip_code = StringVar()
country_code = StringVar()
temp = StringVar()
feels_like = StringVar()
description = StringVar()


def get_weather():
    result = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid=5e19fe7d8d441718a20d7adea3506f35&units=metric'.format(zip_code.get(), country_code.get()))
    temp = str(result.json()['main']['temp'])
    feels_like = str(result.json()['main']['feels_like'])
    icon = str(result.json()['weather'][0]['icon'])
    description = str(result.json()['weather'][0]['description'])
    label_description = Label(text=description).pack()
    label_temp = Label(text='temperature: ' + temp + '°C').pack()
    label_feels_like = Label(text='feels like: ' + feels_like + '°C').pack()
    label_country_code.configure(text='hi')


label_zip_code = Label(text='enter zip code:').pack()
entry_zip_code = Entry(textvariable=zip_code).pack()
label_country_code = Label(text='enter country code:').pack()
entry_country_code = Entry(textvariable=country_code).pack()
search_button = Button(
    text='get weather', command=get_weather).pack()


tk.mainloop()
