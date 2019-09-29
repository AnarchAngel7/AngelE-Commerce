def loginForm():
    choose = input("Please choose an option: 1.Login / 2.Guest: ")
    if choose == "1" or choose == "Login" or choose == "login" or choose == "LOGIN":
        def log():
            user = input("Username: ")
            passw = input("Password: ")
            if user == "Angel":
                if passw =="Password":
                    print("Welcome Admin")
                else:
                    print("Incorrect Password")
                    log()
            else:
                print("New Login Successful")
        log()
    elif choose == "2" or choose == "Guest" or choose == "guest" or choose == "GUEST":
        print("Proceeding as Guest User")
    else:
        print("Please select a suitable option")
        loginForm()
loginForm()         
