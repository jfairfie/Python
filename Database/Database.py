import mysql.connector
import configparser

class DatabaseManager:
	def __init__(self):
		self.configparser = configparser.ConfigParser()
		self.configparser.read('config.ini')

	#Opens connection to a database
	def __open__(self):
		#self.connector = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
		self.connector = mysql.connector.connect(host=self.configparser['MySQL']['host'], 
												user=self.configparser['MySQL']['username'], 
												password=self.configparser['MySQL']['password'], 
												database=self.configparser['MySQL']['database'])
		self.cursor = self.connector.cursor()

	#Gets Connection to database
	def __close__(self):
		self.cursor.close()
		self.connector.close()

	#Reads query and prints out information
	def getQuery(self, sql):
		self.__open__()
		self.cursor.execute(sql)

		row = self.cursor.fetchone()
		while (row is not None):
			print(row)
			row = self.cursor.fetchone()

		self.__close__()

	#Inserts items, does not return or print anything.
	def insertQuery(self, sql, data):
		self.__open__()
		self.cursor.execute(sql, data)
		self.connector.commit()
		self.__close__()

	#Does not print query but rather returns the rows
	def returnQuery(self, sql):
		self.__open__()

		self.cursor.execute(sql)
		rows = self.cursor.fetchall()

		self.__close__()

		if (len(rows) > 0):
			return rows
		else:
			return None

	#Performs a parameterized query
	def parameterizedQuery(self, sql, parameter):
		self.__open__()

		self.cursor.execute(sql, [parameter])
		
		rows = self.cursor.fetchall()

		self.__close__()
		return rows