def Category2():

    print("Choose an option from the given list: ")
    Models = ["1. Samsung Galaxy M10 ", "2 Nokia 6.1 Plus", "3. Xiaomi Mi A3"]
    for b in Models:
        print(b)
    print("Please choose a Mobile from the given options or type 'Back' to return to Categories")
    print()
    Choice = input()
    def FirstChoice():
        if Choice == "1." :
            import M10
        elif Choice == "2" :
            import Nokia
        elif Choice == "3" :
            import Mi
        else:
            print("Choose an option from the list or type Back to return")
            print()
            Choice1 = input()
            if Choice1 == "1" or Choice1 == "2" or Choice1 == "3" :
                FirstChoice()
            elif Choice1 == "Back" :
                exit()
            else: 
                print("Incorrect Entry. Returning to Mobiles Category")
                Category2()
    FirstChoice()
Category2()