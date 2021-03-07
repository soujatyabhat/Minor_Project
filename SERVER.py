from flask import Flask,render_template,request
import pandas as pd 


app = Flask(__name__)


#index page render
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

# Importing the dataset
dataset = pd.read_csv('csv/final.csv')
dataset = dataset.dropna()


#Pijush Segment
#Predict car price based on Model, Age
#-------------------------------------------------------------------------------------------------
unique_car_model = list(set(dataset.iloc[:,1].values))

@app.route('/pijush', methods=["GET", "POST"])
def main1():
    return render_template('prediction1.html',option =unique_car_model ,pred = "pred1" , result = 0.0,
    heading = "Price prediction based on brand & age")

@app.route('/pred1', methods=["GET", "POST"])
def pred1():
    if request.method == 'POST':
        
        #HTML Elements
        model = request.form['model']
        age = int(request.form['age'])
        
        #Price Prediction One
        import others.Carprice_Predict_Pijush as od
        return render_template('prediction1.html',option = unique_car_model ,pred = "pred1",result = float(od.excute(model,age)),
                               heading = "Price prediction based on brand & age")
        
        
#----------------------------------------------------------------------------------------------------
        
#Santanu Saha Segment 
#predict car price based on year,km, Fuel type
#----------------------------------------------------------------------------------------------------
unique_fuel_type = list(set(dataset.iloc[:,5].values))

@app.route('/santanu', methods=["GET", "POST"])
def main2():
    return render_template('prediction2.html',option = unique_fuel_type ,pred = "pred2",ln = len(unique_fuel_type),result = 0.0,
    heading = "Price prediction based on year, KMS Driven & Fuel Type")

@app.route('/pred2', methods=["GET", "POST"])
def pred2():
    if request.method == 'POST':
        
        #HTML Elements
        year = int(request.form['year'])
        km = int(request.form['KM'])
        fuel = int(request.form['fuel'])
        
        #Price Prediction Two
        import others.Carprice_Predict_Santanu as cp
        return render_template('prediction2.html',option = unique_fuel_type ,pred = "pred2",ln = len(unique_fuel_type),result = float(cp.execute(year,km,fuel)),
                               heading = "Price prediction based on year, KMS Driven & Fuel Type")
#----------------------------------------------------------------------------------------------------
        
    
    
#Soujatya Bhattacharya Segment
#Annalyse how many number of fuel type car had been brought in a specific year
#----------------------------------------------------------------------------------------------------
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
        for check_fuel_type in unique_fuel_type:
            count = 0
            for j in range(len(fuel_type)):
                if fuel_type[j] == check_fuel_type and years[j] == int(num):
                    count += 1
            y_axis.append(count)
        print(y_axis)
        return render_template('result.html', title=num, max=max(y_axis), labels=unique_fuel_type, values=y_axis,link = "/rick")
#--------------------------------------------------------------------------------------------------
        
    
#Satyajit Mallick Segment
#Annalyse which model of car were sale a pertculer year 
        
#----------------------------------------------------------------------------------------------------
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
        for check_car_model in unique_car_model:
            count = 0
            for j in range(len(car_model)):
                if car_model[j] == check_car_model and years[j] == int(num):
                    count += 1
            y.append(count)
        return render_template('result.html', title=num, max=max(y), labels = unique_car_model, values=y,link = "/satya")


#---------------------------------------------------------------------------------------     
#about 
@app.route('/about', methods=["GET", "POST"])
def about():
    thisdict = {
        "Pijush Kanti Lasker ": "Predict car price based on Brand Name,  Car Age",
        "Santanu Saha ": "Predict car price based  Year, KM Driven, Fuel Type",
        "Satyajit Mallick ": "Analyse Sailed Car VS Car Model based on specific year",
        "Soujatya Bhattacharya":"Analyse Sailed Car VS Fuel Type based on specific year & Web Application Interface Design"
     }
    return render_template('about.html', send = thisdict)


#Run Web Application
if __name__ == "__main__":
    app.run(port = 3000)
