import sqlite3
import pandas as pd
class Customers():
    def __init__(self):
        pass
    def generateID(self):
        myconn = sqlite3.connect("newgenbank.db")
        query = pd.read_sql_query("SELECT CustomerID FROM ngbcustomers", myconn)
        last = int(query.last_valid_index())
        return last + 2
    def updateCustomer(self):
        global coltitle
        myconn = sqlite3.connect("newgenbank.db")
        query_sel_ID = pd.read_sql_query("SELECT CustomerID FROM ngbcustomers", myconn)
        cus_ids = query_sel_ID
        print(cus_ids['CustomerID'])
        print(type(cus_ids['CustomerID']))
        mycur = myconn.cursor()
        data = ['CustomerID', 'FirstName', 'LastName', 'AccountNumber',
                'AccountBalance', 'DateCreated', 'PhoneNumber']
        mycolumn = input("Select data you would like to update: ")
        myid = eval(input("Enter ID of Customer to proceed: "))
        newval = input("Enter new value: ")

        for index,d in enumerate(data):
            print(str(index+1)+". "+d+"\n")
            if data[index] == mycolumn:
                coltitle = data[index]
        recsquery = mycur.execute("SELECT {},{} FROM ngbcustomers".format(data[0],coltitle))
        records = recsquery.fetchall()
        print(records)
        for x in records:
            if x[0] == myid and x[0] in cus_ids['CustomerID']:
                mycur.execute(f"UPDATE ngbcustomers SET {mycolumn} = {newval} WHERE CustomerID = {myid}")
                myconn.commit()
                print("Updated !!!")
                recsquery = mycur.execute("SELECT {},{} FROM ngbcustomers".format(data[0], coltitle))
                records = recsquery.fetchall()
                print(records)
                myconn.close()


    def showCustomers(self):
        myconn = sqlite3.connect("newgenbank.db")
        query = pd.read_sql_query("SELECT * FROM ngbcustomers",myconn)
        query.index = query.index + 1
        print(query)

    def addCustomers(self,CustomerID,FirstName,LastName,AccountNumber,AccountBalance,DateCreated,PhoneNumber):
        myconn = sqlite3.connect("newgenbank.db")
        mycur = myconn.cursor()
        mycur.execute("INSERT INTO ngbcustomers VALUES (?,?,?,?,?,?,?)",
                      (CustomerID,FirstName,LastName,AccountNumber,AccountBalance,DateCreated,PhoneNumber))
        myconn.commit()

import sqlite3
import pandas as pd
class Customers():
    def __init__(self):
        pass
    def generateID(self):
        myconn = sqlite3.connect("newgenbank.db")
        query = pd.read_sql_query("SELECT CustomerID FROM ngbcustomers", myconn)
        last = int(query.last_valid_index())
        return last + 2
    def updateCustomer(self):
        global coltitle
        myconn = sqlite3.connect("newgenbank.db")
        query_sel_ID = pd.read_sql_query("SELECT CustomerID FROM ngbcustomers", myconn)
        cus_ids = query_sel_ID
        print(cus_ids['CustomerID'])
        print(type(cus_ids['CustomerID']))
        mycur = myconn.cursor()
        data = ['CustomerID', 'FirstName', 'LastName', 'AccountNumber',
                'AccountBalance', 'DateCreated', 'PhoneNumber']
        mycolumn = input("Select data you would like to update: ")
        myid = eval(input("Enter ID of Customer to proceed: "))
        newval = input("Enter new value: ")

        for index,d in enumerate(data):
            print(str(index+1)+". "+d+"\n")
            if data[index] == mycolumn:
                coltitle = data[index]
        recsquery = mycur.execute("SELECT {},{} FROM ngbcustomers".format(data[0],coltitle))
        records = recsquery.fetchall()
        print(records)
        for x in records:
            if x[0] == myid and x[0] in cus_ids['CustomerID']:
                mycur.execute(f"UPDATE ngbcustomers SET {mycolumn} = {newval} WHERE CustomerID = {myid}")
                myconn.commit()
                print("Updated !!!")
                recsquery = mycur.execute("SELECT {},{} FROM ngbcustomers".format(data[0], coltitle))
                records = recsquery.fetchall()
                print(records)
                myconn.close()


    def showCustomers(self):
        myconn = sqlite3.connect("newgenbank.db")
        query = pd.read_sql_query("SELECT * FROM ngbcustomers",myconn)
        query.index = query.index + 1
        print(query)

    def addCustomers(self,CustomerID,FirstName,LastName,AccountNumber,AccountBalance,DateCreated,PhoneNumber):
        myconn = sqlite3.connect("newgenbank.db")
        mycur = myconn.cursor()
        mycur.execute("INSERT INTO ngbcustomers VALUES (?,?,?,?,?,?,?)",
                      (CustomerID,FirstName,LastName,AccountNumber,AccountBalance,DateCreated,PhoneNumber))
        myconn.commit()

