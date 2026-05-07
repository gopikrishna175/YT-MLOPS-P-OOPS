class Chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.logedin=False
        self.menu()

    def menu(self):
        ui=input(""""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
                           
        if ui=="1":
            self.signup()
        elif ui=='2':
            self.signin()
        elif ui=='3':
            pass
        else:
            exit()

    def signup(self):
        email=input("Enter your email here-> ")
        pwd=input("Enter your password here-> ")
        self.username=email
        self.password=pwd
        print("Sign up completed")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("You need to signup")
        else:
            uname=input("Enter your email-> ")
            pwd=input("Enter your password")
            if self.username==uname and self.password==pwd:
                print("You have logged in")
            else:
                print("Enter details correctly")
        print("\n")
        self.menu()

obj=Chatbook()