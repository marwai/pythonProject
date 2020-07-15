import pyodbc
import os
import secretfile
import sys

class Databases:
    server = secretfile.server
    database = secretfile.database
    username = secretfile.username
    password = secretfile.password

    def __init__(self):
        try:
            self.connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server +
                                              ';DATABASE=' + self.database + ';UID=' + self.username +
                                              ';PWD=' + self.password)
            print("Connection Established")
            self.cursor = self.connections.cursor()
        except Exception:
            print("Did not connect")


# Instantiated class
d = Databases()

