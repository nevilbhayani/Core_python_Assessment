def f_market():
    print("\n\n\t\t\t\n\t\t\t\t\t\t\t* * * *  WELCOM TO FRUIT MARKET  * * * *\n\n")
    print("\t\t\t\n\t\t\t\t\t\t\t\t 1] - Manager ")
    print("\t\t\t\n\t\t\t\t\t\t\t\t 2] - Customer \n\n\n")


    num1=int(input("Select Your Role :- "))
    x=(" 1} - Add Fruit Stock ")
    y=(" 2} - View Fruit Stock ")
    z=(" 3} - Update Fruit Stock \n\n")

    if num1 == 1:
        print("\n\n\t\t\t\n\t\t\t\t\t\t\t\t* FRUIT MARKET MANAGER *\n")
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",x)
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",y)
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",z)

        num2=int(input("\nEnter Your Choice :- "))
    
        if num2 == 1:
         print("\n   \t\t\t\t\t\t\t\t  ~ ADD FRUIT STOCK ~\n")
         name=str(input("\n Enter Fruit Name :- "))
         qty=int(input(" Enter Qty (in Kg) :- "))
         price=int(input("Enter Price :- "))
         print("\n")
         print("\n")

        a=str(input(" Do you want to perfoem more operations : press 'y' for yes and 'n' for no :- "))
        print("\n")
        print("\n")

        if a == "y" or a == "Y":
         name1=str(input("Enter Fruit Name :- "))
         qty1=int(input("Enter Qty (in Kg) :- "))
         price1=int(input("Enter Price :- "))

        elif a == "n" or a == "N":
              print("\n   \t\t\t\t\t\t\t\t * * Thank You * *\n\n")
    
        elif num2==2:
         print(name,"'",{"QTY:",qty,'PRICE',price,"\n\n"})

        else:
           print("\n   \t\t\t\t\t\t\t\t  * Thank you *")




        num2=int(input("\nEnter Your Choice :- "))
        if num2== 1:
         name3=str(input("Enter Fruit Name :- "))
         qty3=int(input("Enter Qty (in Kg) :- "))
         price3=int(input("Enter Price :- "))

         print("\n   \t\t\t\t\t\t\t\t  * Thank You *")
        
        elif num2==2:
         print(name,{"QTY:",qty,"PRICE:",price})
         print(name1,{"QTY:",qty1,"PRICE:",price1 })
         print(name3,{"QTY:",qty3,"PRICE:",price3 })


         print("\n\n\n   \t\t\t\t\t\t\t\t  * Thank You * ")



        num2=int(input("\nEnter Your Choice :- "))
        if num2== 1:
         print("\n   \t\t\t\t\t\t\t\t  * Sorry stock is full *")
        
        elif num2==2:
         print(name,{"QTY:",qty,"PRICE:",price})
         print(name1,{"QTY:",qty1,"PRICE:",price1 })
         print(name3,{"QTY:",qty3,"PRICE:",price3 })

         print("\n\n\n   \t\t\t\t\t\t\t\t  * Thank You * ")
         



    elif num1==2:
       print("\n\n\t\t\t\n\t\t\t\t\t\t\t\t* * * Customer * * *")



f_market()

