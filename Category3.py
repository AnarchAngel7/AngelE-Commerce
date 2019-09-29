def Category3():

    print("Choose an option from the given list: ")
    Models = ["1. Grass Door Mat", "2 Solimo Microfibre Reversible Comforter", "3. Home Diwan Set of 8 Pc"]
    for b in Models:
        print(b)
    print()("Please choose a product from the given options or type 'Back' to return to Categories")
    print()
    Choice = input
    def FirstChoice():
        if Choice == "1." :
            import Door
        elif Choice == "2" :
            import Comfort
        elif Choice == "3" :
            import Diwan
        else:
            print("Choose an option from the list or type Back to return")
            print()
            Choice1 = input()
            if Choice1 == "1" or Choice1 == "2" or Choice1 == "3" :
                FirstChoice()
            elif Choice1 == "Back" :
                exit()
            else: 
                print("Incorrect Entry. Returning to Home Category")
                Category3()
    FirstChoice()
Category3()