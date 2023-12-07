print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1. Add a product to the cart. ")
print("2. Search for a product. ")
print("3. Delete a product from the cart. ")
print("4. Display the contents of the cart. ")
print("5. Purchase items. ")
print("6. Quit. ")

cart={}
x=int(input("What do you wish to do? : "))
while(x!=6):
    if x==1:
        y=int(input("How many items u want to Add to your CART: "))
        total=0
        for y in range(0,5):
            i=(input("Please Enter Product Name & Brand: "))
            j=int(input("Please Enter its Price: "))
            cart.update({i:j})
            total=total+j
            y=y-1
        print("Your Cart contains the following items:")
        print(cart)
                
        print("Sorry your cart is full.")
    elif x==2:
        z=str(input("Which product do you want to search? : "))
        if z in cart:
            print(z)
            print(cart[z])
        else:
            print("NO product exists with this name.")
    elif x==3:
        d=(input("Which product do you want to Delete? : "))
        if len(cart)>0:
            if d in cart:
                del cart[d]
            else:
                print("Product not found in cart.")
        else:
            print("Cart is empty, no item is found.")
        print("Your Cart contains the following items:")
        print(cart)
    elif x==4:
        print("Your Cart contains the following items:")
        print(cart)
    elif x==5:
        pur=input("Do you wish to complete the purchase? (y/n): ").lower()
            
        while x==5:
            if pur=="y":
                print("Thank you for your business.")
                print("Your Total Amount is : ",total)
                cart={}
                break
            elif pur=="n":
                print("Please continue shopping.")
                break
            else:
                print("Please answer either Y or N.")
            pur=input("Do you wish to complete the purchase? (y/n): ").lower()
            
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add a product to the cart. ")
    print("2. Search for a product. ")
    print("3. Delete a product from the cart. ")
    print("4. Display the contents of the cart. ")
    print("5. Purchase items. ")
    print("6. Quit. ")              
    x=int(input("What do u wish to do? : "))
print("Thankyou")        
