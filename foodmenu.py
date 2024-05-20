type1=input("Which type of food are you looking for Veg/Non-veg : ")
if type1=="Veg":
    print("\n1. panner-masala \n2. paneer-tikka \n3. mushroom-masala")
    food=input("Which dish would you like to order :")
    if "paneer-masala"==food:
        print("\n paneer-masala \n price :300 \n butter roti:4")
    elif "paneer-tikka"==food:
                    print("\n paneer-tikka \n price :250 \n butter roti:4")
    elif type1=="Non-veg":
                        print("\n1. Chicken-lapeta \n2. Chicken-biryani \n3. Mutton-biryani")
                        food=input("Which dish would you like to order :")
                        if "Mutton-biryani"==food:
                           print("\n Mutton-biryani \n price:400")
