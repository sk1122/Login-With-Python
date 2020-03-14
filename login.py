from getpass import getpass
import bcrypt
from database import Database

db = Database()
db.createTable()


class Login:

    """
        Class for Login
        @param username
        @param password
    """

    def __init__(self):
        self.username = input("\t\tEnter Your Username: ")
        self.password = getpass(prompt="\t\tEnter Your Password: ")

    def validate(self):
        data = (self.username,)
        inputData = (self.username, self.password,)
        if (db.validateData(data, inputData)):
            print("Logged In Successfully")
        else:
            print("Wrong Credentials")


class Register:

    """
        Class for Register
        @param username
        @param password
    """

    def __init__(self):
        self.username = input("\t\tEnter Your Username: ")
        self.password = getpass(prompt="\t\tEnter Your Password: ")
        self.salt = bcrypt.gensalt()
        self.hashed = bcrypt.hashpw(self.password.encode(), self.salt)

    def add(self):
        data = (self.username,)

        result = db.searchData(data)

        if result != 0:
            data = (self.username, self.hashed)
            db.insertData(data)
        else:
            print("Username already Exists")


print("\t\tWelcome to App")

while True:
    print("")
    print("\t\t1. Login")
    print("\t\t2. Register")

    option = int(input("\t\tEnter Your Option: "))

    if option == 1:
        login = Login()
        login.validate()

    elif option == 2:
        register = Register()
        register.add()

    else:
        print("\t\tWrong Input..\n\n")
