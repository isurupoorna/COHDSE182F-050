import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db["login"]

user_name = input("Enter user name : ")
password = input("Enter password :")
for x in collection.find({},{"userName":1,"password":1}):
    name=str(x["userName"])
    Password=str(x["password"])
if user_name==name and password==Password:
    print("login successful")
else:
    print("login failed")


