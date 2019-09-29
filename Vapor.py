def Vapor():
    print("Powered by Android Wear 2.0")
    print("Qualcomm Snapdragon Wear 2100 Processor")
    print("Virtual Bezel for Quick Navigation")
    print("1.39 Full Round AMOLED Display")
    print("Standalone Wireless Music Player")
    print("Connected GPS Location Services")
    print("Heart-Rate Tracking")
    print("Swimproof, Water Resistant Upto 50 m")
    print("Compatible with iPhone (iOS 9 and Above) and Android Phones (Android 4.3 and Above)")
    print("With Call Function")
    print("Touchscreen")
    print("Notifier, Fitness & Outdoor")

    print("                    Price: Rs.11,999                    ")
     
    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1":
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Misfit Vapor")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3":
        print("Returning")
    else:
        print("Incorrect input")
        Vapor()
Vapor()    
