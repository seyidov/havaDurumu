from tkinter import *
from PIL import ImageTk,Image
import requests

url= "https://api.openweathermap.org/data/2.5/weather"
apiKey="6ecdf9e6617dadfcbf12cf71699f7ccd"
iconUrl="http://openweathermap.org/img/wn/{}@2x.png"

def getWeather(city):
    params={'q':city,'appid':apiKey,'lang':'tr'}
    data=requests.get(url,params=params).json()
    if data:
        city=data['name'].capitalize()
        country=data['sys']['country']
        temp=int(data['main']['temp']-273)
        icon=data['weather'][0]['icon']
        condiditon=data['weather'][0]['description']
        return (city,country,temp,icon,condiditon)

def main():
    city=cityEntry.get()
    weather=getWeather(city)
    locationLabel['text']='{},{}'.format(weather[0],weather[1])
    tempLabel['text']='{} C'.format(weather[2])
    conditionLabel['text']=weather[4]
    icon =ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
    iconLabel.configure(image=icon)
    iconLabel.image=icon

app=Tk()
app.geometry('450x450')
app.title('Hava Durumu')
app.configure(background="lightgreen")

cityEntry=Entry(app,justify="center",background="lightblue")
cityEntry.pack(fill=BOTH,ipady=10,padx=10,pady=10)
cityEntry.focus()
cityEntry.configure(font=("Arial",25))

searchButton=Button(app,text="Arama",font=('Arial',15),background="lightblue",command=main)
searchButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel=Label(app,background="lightgreen")
iconLabel.pack()

locationLabel=Label(app,font=('Arial',40),background="lightgreen")
locationLabel.pack()

tempLabel=Label(app,font=('Arial',40,'bold'),background="lightgreen")
tempLabel.pack()

conditionLabel=Label(app,font=('Arial',20,),background="lightgreen")
conditionLabel.pack()

app.mainloop()
