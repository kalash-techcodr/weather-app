#required library
import tkinter as tk
import requests
import os



#UI
root = tk.Tk()
root.geometry("600x400")
root.title("Weather app")
tk.Label(root, text = "CITY", font = ("Jetbrains mono", 18 , "bold")).pack(pady = 10)
city_entry = tk.Entry(root, width=50)
city_entry.pack(pady = 10)


#your api key
api_key = "2e36dd0ff3fd44a5b32102012261901"



#main logic
def main_function():
    global api_key
    city_name = city_entry.get()
    print(city_name)
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current = data["current"]
        temp_c = current["temp_c"]
        temp_f = current["temp_f"]
        tk.Label(root, text = f'Tempreature in celcius: {temp_c}', font = ("Jetbrains mono", 16, "bold")).pack()
        tk.Label(root, text = f'Tempreature in farheneight: {temp_f}', font = ("Jetbrains mono", 16, "bold")).pack()
        

#get weather button
tk.Button(root, text = " Get Weather", command=main_function, width=10,height=2).pack()


#loop of window
root.mainloop()