def GearS3():
    print("1.3-inch 360x360 Super AMOLED capacitive touchscreen display")
    print("Corning Gorilla Glass SR+")
    print("Galaxy wearable app")
    print("Compatibiltiy with :Samsung Andrioid,Other Android,ios(Bluetooth) and ios(Stand alone)")
    print("Certified IP68 and MIL-STD-810G (temperatures and shock resistant)")
    print("Tizen based wearable OS")
    print("Specifications: Dual-core 1GHz CPU, 768MB RAM, 4GB internal memory")

    print("                    Price: Rs.19,600                    ")
     
    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1" :
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Samsung Gear S3 Frontier")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3" :
        print("Returning")
    else:
        print("Incorrect input")
        GearS3()
GearS3()    
