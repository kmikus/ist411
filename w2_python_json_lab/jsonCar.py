# Project: Python and JSON Linux System Lab
# Purpose Details: To create a JSON file from a python object and read back in the results
# Course: IST 411
# Author: Kevin Mikus
# Date Developed: 9/1/17
# Last Date Changed: 9/1/17
# Rev: 0.1

import json


class Car:
    def __init__(self, make, model, year, color, features, licensePlateNum, mileage, underWarranty):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.features = features
        self.licensePlateNum = licensePlateNum
        self.mileage = mileage
        self.underWarranty = underWarranty

myCar = Car("mitsubishi", "eclipse", 2011, "black", ["sunroof", "heated seated", "bluetooth"], "AAA7AAA", 85000, False)

# json dump
with open("jsonCar.json", "w") as outFile:
    outFile.write(json.dumps(myCar.__dict__, indent=4))

# json load
with open("jsonCar.json", "r") as jsonStream:
    nextCar = json.load(jsonStream)
    print(repr(nextCar))
