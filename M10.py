def M10():
    print("13MP+5MP ultra-wide angle dual camera | 5MP f2.0 front camera. The internet usage time is 15 hours for 3G as well as 19 hours for LTE.The video playback time is 17 hours and audio playback time is 84 hours")
    print("15.8cm (6.22-inch) HD+ Infinity V Display with 90% screen ratio")
    print("3GB RAM and 32GB internal memory expandable up to 512GB in a dedicated slot")
    print("Fast face unlock | 3400 mAh lithium-ion battery")
    print("Dual SIM (nano+nano) with dual standby and dual VoLTE")
    print("1.6GHz Exynos 7870 octa-core processor | Android Oreo v8.1 OS")
    print("1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories including batteries from the date of purchase")

    print("                    Price: Rs.8,090                    ")

    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1":
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Samsung M10")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3":
        print("Returning")
    else:
        print("Incorrect input")
        M10()
M10()    
