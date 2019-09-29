def Nokia():
    print("16MP+5MP rear camera | 16MP front facing camera")
    print("14.732 centimeters (5.8-inch) with 1080 x 2280 pixels resolution")
    print("Memory, Storage and SIM: 6GB RAM | 64GB internal memory | Expandable to 400 GB |Dual SIM dual-standby (4G+4G)")
    print("Android v8 Oreo operating system with Qualcomm Snapdragon SD 636 quad core processor")
    print("3060mAH lithium-ion battery")
    print("1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories including batteries from the date of purchase")
    print("Box includes: Charger and Data cable")

    print("                    Price: Rs.10,999                    ")

    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1":
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Nokia 6.1 Plus")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3":
        print("Returning")
    else:
        print("Incorrect input")
        Nokia()
Nokia()    
