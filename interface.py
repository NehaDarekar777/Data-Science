from flask import Flask, jsonify, request, render_template
from utils import CaliforniaHouse
import config

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"result": "Successful"})

@app.route('/calhouseprice')
def home_api():
    print("California home API")
    return render_template('calhouseprice.html')

@app.route('/predicted_price', methods=['GET', 'POST'])
def predicted_price():
    data = request.args.get() if request.method == 'GET' else request.form

    longitude = float(data.get('longitude'))
    latitude = float(data.get('latitude'))
    housing_median_age = float(data.get('housing_median_age'))
    total_rooms = float(data.get('total_rooms'))
    total_bedrooms = float(data.get('total_bedrooms'))
    population = float(data.get('population'))
    households = float(data.get('households'))
    median_income = float(data.get('median_income'))
    ocean_proximity = data.get('ocean_proximity')

    obj = CaliforniaHouse(longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households,
                          median_income, ocean_proximity)

    pchp = obj.price_prediction()
    return render_template("calhouseprice.html", predict_price=pchp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
