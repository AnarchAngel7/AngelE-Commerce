def Door():
    print("Size: 15.75x23.63-inches")
    print("Easy to use")
    print("Make home beautiful")
    print("Amazing finish")
    print("Primarily made of polyester and polyester-blend") 

    print("                    Price: Rs.200                    ")

    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1":
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Aritificial Grass Door Mat")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3":
        print("Returning")
    else:
        print("Incorrect input")
        Door()
Door()    
