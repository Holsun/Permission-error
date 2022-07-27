import mysql.connector as connection
mydb = connection.connect (host="localhost", user="root", passwd="", database="challenge")
cursor = mydb.cursor()

import pandas as pd

#cursor.execute("use ineuron")
#cursor.execute("show tables")
#a = cursor.fetchall()
#for i in a:
#    print(i)

#cursor.execute("create database challenge")
#cursor.execute("show databases")
#b = cursor.fetchall()
#for i in b:
#    print(i)

#cursor.execute("create table if not exists challenge.attribute_dataset "
#               "(Dress_ID INT(20), Style VARCHAR(10),Price VARCHAR(10),"
#               "Rating DECIMAL(2,1),Size VARCHAR(10),Season VARCHAR(10),"
#               "Neckline VARCHAR(20),Sleevelenth VARCHAR(20),Waiseline VARCHAR(20),"
#               "Material VARCHAR(20),FabricType VARCHAR(20),Decoration VARCHAR(20),"
#               "Pattern_Type VARCHAR(2),Recommendation INT(10))")


#df = pd.read_csv("/users/stanleysuen/Desktop/Attribute DataSet.csv")
#print(df)

#cursor.execute("show variables like 'secure_file_priv';")
#view = cursor.fetchall()
#for i in view:
#   print(i)

#file = open("/users/stanleysuen/Desktop/Attribute DataSet.csv", "r")
#content = file.read()
#print(content)
#file.close()

cursor.execute("load data infile 'Attribute DataSet.csv' into table attribute_dataset;")




