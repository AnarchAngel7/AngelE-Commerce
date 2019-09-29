def E_Commerce():
    import LoginTest
    def StartingPoint():
        print("Welcome to Angel Shopping")
        print("1.Categories                  2.Cart                  3.Exit")
        print("Please chose one of the options given above in a numeric manner or type in the option")
        print()
        Choice1 = input()
        if Choice1 == "Categories" or Choice1 == "1":
            Categories=["1. Computers", "2. Mobiles", "3. Home, Kitchen and Furniture"]
            for a in Categories:
                print(a)
            Opt1 = input("Please choose an option to proceed further: ")
            if Opt1 == "1" or Opt1 == "Computers":
                import Category1
            elif Opt1 == "2" or Opt1 == "Mobiles":
                import Category2
            elif Opt1 == "3" or Opt1 == "Home":
                import Category3
            else:
                choice = input("Please choose an option from the given list or type Back to return to login")
                if choice == "Back":
                    E_Commerce()
                else:
                    print("Incorrect entry. Returning to Home Screen")
                    StartingPoint()
        elif Choice1 == "Cart" or Choice1 == "2":
            file = open("D:\\Python Work\\E-Commerce\\Cart","r")
            contents = file.read()
            print(contents)
            file.close()
            StartingPoint()
        elif Choice1 == "Exit" or Choice1 == "3":
            exit()
        else:
            print("Please type one of the given choices")
            StartingPoint()
        StartingPoint()
    StartingPoint()
E_Commerce()

    

