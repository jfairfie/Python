#Selects all columns from Car 
def selectAllFromCar():
	return "SELECT vin, year, make, model, trim, color, interiorcolor, engine, drivetype, fuel, transmission, date FROM Car;"

#Returns all year, make, model, trim and prices for each car
def selectYearMakeModelPrice():
	return "SELECT year, make, model, trim, price FROM Car INNER JOIN Price ON Price.vin = Car.vin"

#Counts number of each make
def selectMakeCount():
	return "SELECT DISTINCT make, COUNT(vin) as Amount FROM Car GROUP BY make ORDER BY Amount DESC;"

#Counts number of each model
def selectModelCount():
	return "SELECT DISTINCT make, model, COUNT(vin) as Amount FROM Car GROUP BY model ORDER BY Amount DESC;"

#Returns amount of each make, where price > 45000
def selectMakeCountByPriceOver():
	return "SELECT DISTINCT make, COUNT(Car.vin) as Amount FROM Car INNER JOIN Price ON Price.vin = Car.vin WHERE price > 45000 GROUP BY make ORDER BY Amount DESC;"

#Returns amount by make, model with price over
def selectMakeModelCountByPriceOver():
	return "SELECT DISTINCT make, model, COUNT(Car.vin) AS Amount FROM Car INNER JOIN Price ON Price.vin = Car.vin WHERE price>45000 GROUP BY model ORDER BY Amount DESC;"

#Returns least expensive record 
def selectLeastExpensive():
	return "SELECT year, make, model, trim, price FROM Price INNER JOIN Car ON Car.vin = Price.vin ORDER BY price ASC LIMIT 1;"

#Returns most expensive record
def selectMostExpensive():
	return "SELECT year, make, model, trim, price FROM Price INNER JOIN Car ON Car.vin = Price.vin ORDER BY price DESC LIMIT 1;"

#Gets list of items from least to most expensive 
def selectOrderByPriceIncrease():
	return "SELECT year, make, model, trim, price FROM Car INNER JOIN Price ON Car.vin = Price.vin ORDER BY price ASC;"

#Gets list of items from most to least expensive
def selectOrderbyPriceDecrease():
	return "SELECT year, make, model, trim, price FROM Car INNER JOIN Price ON Car.vin = Price.vin ORDER BY price DESC;"

#Finds if a vin exists
def findVinByParameterVin():
	return "SELECT vin FROM Car WHERE vin = %s;"

#Insert Data into Car Table
def insertIntoCar():
	return "INSERT INTO Car   (vin, make, model, year, color, engine, drivetype, interiorcolor, date, trim, fuel, transmission) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

#Insert Data into Price Table
def insertIntoPrice():
	return "INSERT INTO Price VALUES (%s, %s, %s);"

#Insert Data into Miles Table
def insertIntoMiles():
	return "INSERT INTO Miles VALUES (%s, %s, %s);"


def insertIntoSeller():
	return "INSERT INTO Seller (vin, name, date, address) VALUES (%s, %s, %s, %s);"