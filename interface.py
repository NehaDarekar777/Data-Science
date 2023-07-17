from Flask import Flask,jsonify,request,render_template
from utils import CaliforniaHouse
import config


app=Flask(__name__)



@app.route('/')
def home():
    return jsonify({"result":"Successfull"})


@app.route('/calhouseprice')
def home_api():
    print("California home API")
    return render_template('calhouseprice.html')


@app.route('/predicted price',methods=['GET','POST'])
def predicted_price():
    
    if request.method=='GET':
        data =request.args.get
        print('Data:',data)
        longitude             =float(data('longitude'))
        latitude              =float(data('latitude'))
        housing_median_age    =float(data('housing_median_age'))
        total_rooms           =float(data('total_rooms'))
        total_bedrooms        =float(data('total_bedrooms'))
        population            =float(data('population'))
        households            =float(data('households'))
        median_income         =float(data('median_income'))
        ocean_proximity       =data['ocean_proximity']



        # longitude             =int(data['longitude'])
        # latitude              =int(data['latitude'])
        # housing_median_age    =int(data['housing_median_age'])
        # total_rooms           =int(data['total_rooms'])
        # total_bedrooms        =int(data['total_bedrooms'])
        # population            =int(data['population'])
        # households            =int(data['households'])
        # median_income         =int(data['median_income'])
        # ocean_proximity       =data['ocean_proximity']

        obj=CaliforniaHouse(longitude, latitude, housing_median_age, total_rooms,total_bedrooms, population, households, 
                    median_income, ocean_proximity)

        pchp=obj.price_prediction()
        return render_template("calhouseprice.html",predict_price =pchp)
    
    elif request.method=='POST':
        data =request.args.get
        print('Data:',data)
        longitude             =int(data('longitude'))
        latitude              =int(data('latitude'))
        housing_median_age    =int(data('housing_median_age'))
        total_rooms           =int(data('total_rooms'))
        total_bedrooms        =int(data('total_bedrooms'))
        population            =int(data('population'))
        households            =int(data('households'))
        median_income         =int(data('median_income'))
        ocean_proximity       =data['ocean_proximity']

        obj=CaliforniaHouse(longitude, latitude, housing_median_age, total_rooms,total_bedrooms, population, households, 
                    median_income, ocean_proximity)

        pchp=obj.price_prediction()
        return render_template("calhouseprice.html",predict_price =pchp)

    return jsonify({"Message" : "Unsuccessful"})

if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)