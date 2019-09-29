def Comfort():
    print("Soft, cosy and light weight reversible comforter with 200 GSM hollow siliconized polyester filling")
    print("100 percent microfibre shell for a rich, luxurious feel")
    print("Hypoallergenic filling which protects against allergens")
    print("Machine stitched pattern to keep the filling in place for durability")
    print("Pack Contents: 1 Ash Grey & Deep Teal comforter (Double, 230 cm X 254 cm)")

    print("                    Price: Rs.1,849                    ")
     
    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1":
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Solimo Microfibre Comforter, Double")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3":
        print("Returning")
    else:
        print("Incorrect input")
        Comfort()
Comfort()    
