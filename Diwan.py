def Diwan():
    print("Package Contents :1 SINGLE BED SHEET+ 5 CUSHION COVERS + 2 BOLSTER COVERS")
    print("Size (LxB): Bedsheet - 228 cm x 150 cm, Cushion cover - 38 cm x 38 cm, Bolster cover - 40 cm x 80 cm")
    print("Care Instructions :Soft Hand wash with cold water, No Machine wash, Do not bleach, Dry in Shade")
    print("Luxirious Look , Premium Quality , Attractive Print , Best For gifting Purpose")

    print("                    Price: Rs.399                    ")
     
    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1":
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Home Diwan Set (8 pc)")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3":
        print("Returning")
    else:
        print("Incorrect input")
        Diwan()
Diwan()    
