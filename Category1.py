def Category1():

    subCategories = ["1. Laptops", "2. Wearables"]
    for a in subCategories:
        print(a)
    Choose = input("Choose an option from the given list: ")
    if Choose == "1" or Choose == "Laptops":
        def FirstChoice():
            Models = ["1. HP 15 Core i3 7th gen 15.6-inch Laptop", "2 Lenovo Ideapad 330 15.6-inch FHD Laptop", "3. Lenovo Legion Y530 Intel Core I5 8th Gen 15.6 inch FHD Laptop"]
            for b in Models:
                print(b)
            print("Please choose a Laptop from the given options or type 'Back' to return to Categories")
            print()
            Choice = input()
            if Choice == "1" :
                import HP15
            elif Choice == "2" :
                import IdeaPad 
            elif Choice == "3" :
                import Legion
            else:
                print("Choose an option from the list or type Back to return")
                print()
                Choice1 = input()
                if Choice1 == "1" or Choice1 == "2" or Choice1 == "3" :
                    FirstChoice()
                elif Choice1 == "Back" :
                    Category1()
                else: 
                    print("Incorrect Entry. Returning to Computers Category")
                    Category1()
        FirstChoice()
    elif Choose == "2" or Choose == "Wearables" :
        def SecondChoice():
            Models1 = ["1. Amazfit Bip Lite", "2 Samsung Gear S3", "3. Misfit Vapor"]
            for c in Models1:
                print(c)
            print("Please choose a Laptop from the given options or type 'Back' to return to Categories")
            print()
            Choice2 = input()
            if Choice2 == "1." :
                import AmazfitBip
            elif Choice2 == "2" :
                import GearS3
            elif Choice2 == "3" :
                import Vapor
            else:
                print("Choose an option from the list or type Back to return")
                print()
                Choice3 = input()
                if Choice3 == "1" or Choice3 == "2" or Choice3 == "3" or Choice3 == "4" or Choice3 == "5" :
                    SecondChoice()
                elif Choice3 == "Back" :
                    Category1()
                else: 
                    print("Incorrect Entry. Returning to Computers Category")
                    Category1()
        SecondChoice()

Category1()