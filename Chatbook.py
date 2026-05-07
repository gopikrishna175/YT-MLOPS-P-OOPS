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
            pass
        elif ui=='2':
            pass
        elif ui=='3':
            pass
        else:
            exit()

obj=Chatbook()