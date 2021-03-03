from flask import Flask,render_template,url_for,request,redirect
import json, random
import pandas as pd 
import numpy as np

app = Flask(__name__)


#index page render
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

# Importing the dataset
dataset = pd.read_csv('final.csv')
dataset = dataset.dropna()


#Santanu Saha Segment 
#predict car price based on year,km, Fuel type

@app.route('/santanu', methods=["GET", "POST"])
def santanu():
    unique_fuel_type = list(set(dataset.iloc[:,5].values))
    return render_template('perdiction.html',option = unique_fuel_type , heading = "wise car sale",pred = "pred1",ln = len(unique_fuel_type))

@app.route('/pred1', methods=["GET", "POST"])
def main2():
    if request.method == 'POST':
        
        #HTML Elements
        year = int(request.form['year'])
        km = int(request.form['KM'])
        fuel = int(request.form['fuel'])
        
        #Predition code
        

        
#Soujatya Bhattacharya Segment
#Annalyse how many number of fuel type car had been brought in a specific year


#Distinct fuel types from dataset
Unique_fuel_type = list(set(dataset.iloc[:,5].values))

#import data fields
fuel_type = dataset.iloc[:,5].values
years = list(map(int,dataset.iloc[:,2].values))


@app.route('/rick', methods=["GET", "POST"])
def main3():
    unique_years = list(set(years))
    return render_template('analysis.html',option = unique_years, heading = "wise car sale",year = "year1")



@app.route('/year1', methods=["GET", "POST"])
def yr1():
    if request.method == 'POST':
        num = request.form['year']
        y_axis = []
        for check_fuel_type in Unique_fuel_type:
            count = 0
            for j in range(len(fuel_type)):
                if fuel_type[j] == check_fuel_type and years[j] == int(num):
                    count += 1
            y_axis.append(count)
        print(y_axis)
        return render_template('result.html', title=num, max=max(y_axis), labels=Unique_fuel_type, values=y_axis,link = "/rick")


#Satyajit Mallick Segment
#Annalyse which model of car were sale a pertculer year 


#Distinct fuel types from dataset
Unique_car_model = list(set(dataset.iloc[:,1].values))

#import data fields
car_model = dataset.iloc[:,1].values

@app.route('/satya', methods=["GET", "POST"])
def main4():
    unique_years = list(set(years))
    return render_template('analysis.html',option = unique_years, heading = "wise car band",year = "year2")

@app.route('/year2', methods=["GET", "POST"])
def yr2():
    if request.method == 'POST':
        num = request.form['year']
        y = []
        for check_car_model in Unique_car_model:
            count = 0
            for j in range(len(car_model)):
                if car_model[j] == check_car_model and years[j] == int(num):
                    count += 1
            y.append(count)
        return render_template('result.html', title=num, max=max(y), labels=Unique_car_model, values=y,link = "/satya")
       
if __name__ == "__main__":
    app.run(port = 3000)
