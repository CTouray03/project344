import mysql.connector
from mysql.connector import Error
from datetime import datetime

class RestaurantDatabase():
    def __init__(self,
                 host="127.0.0.1",
                 port="3306",
                 database="resturant_reservation",
                 user='root',
                 password='Chomus0203'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None

    def addReservation(self, customerID, reservationTime, numberOfguests, specialRequests):
        ''' Method to insert a new reservation into the reservations table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO Reservation (customerID, reservationTime, numberOfGuests, specialRequests) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (customerID, reservationTime, numberOfguests, specialRequests))
            self.connection.commit()
            print("Reservation added successfully")
            return
    

    def getAllReservations(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM Reservation"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def addCustomer(self, customerName, contactInfo):
        ''' Method to add a new customer to the customers table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO customers (customer_name, contact_info) VALUES (%s, %s)"
            self.cursor.execute(query, (customer_name, contact_info))
            self.connection.commit()
            print("Customer added successfully")
            return

    def getCustomerPreferences(self, customerID):
        ''' Method to retrieve dining preferences for a specific customer '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM diningPreferences WHERE customerId = %s"
            self.cursor.execute(query, (customerID,))
            preferences = self.cursor.fetchall()
            return preferences


