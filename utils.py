import json
import pickle
import numpy as np
import config

class CaliforniaHouse():
    def __init__(self,longitude, latitude, housing_median_age, total_rooms,total_bedrooms, population, households, 
                  median_income, ocean_proximity):
         self.longitude           =longitude
         self.latitude            =latitude
         self.housing_median_age  =housing_median_age
         self.total_rooms         =total_rooms
         self.total_bedrooms      =total_bedrooms
         self.population          =population
         self.households          =households
         self.median_income       =median_income
         self.ocean_proximity     =ocean_proximity
         return
        
    
    def load_data(self):
        # import config

        model_file_name=config.MODEL_FILE_PATH
        print("****************",model_file_name)

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model=pickle.load(f)
        

        with open(config.JSON_FILE_PATH,'r') as f:
             self.json_data=json.load(f)
        
             

    def price_prediction(self):
            self.load_data()

            ocean_proximity =self.json_data['ocean_proximity'][self.ocean_proximity]

            test_array = np.zeros([1,self.model.n_features_in_])

            test_array[0][0]=self.longitude
            test_array[0][1]=self.latitude
            test_array[0][2]=self.housing_median_age
            test_array[0][3]=self.total_rooms
            test_array[0][4]=self.total_bedrooms
            test_array[0][5]=self.population
            test_array[0][6]=self.households
            test_array[0][7]=self.median_income
            test_array[0][8]=ocean_proximity

            house_price=np.around(self.model.predict(test_array)[0],3)
            return house_price
        
