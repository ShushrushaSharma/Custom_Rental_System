'''importing a View file'''
import View

#defining function to include all the actions
def Rent_costume():
    #creating an empty list
    l=[]
    a=[]
    
    import datetime
    #library, class and methods
    date = str(datetime.datetime.now().year) + "-" +str(datetime.datetime.now()
    .month) + "-" + str(datetime.datetime.now().day)
    time = str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now()
    .minute) + "-" + str(datetime.datetime.now().second)
    date_time = str(date) + " " + str(time)

    print("")
    print("**"*20) 
    print("        Let's rent a costume!!")
    print("**"*20) 
    print("")
    View.view_costume()

    #defining function for the textfile
    def stock_dict():
        file=open("Stocks.txt", "r")
        custome_dict={}
        custome_id=1
        for i in file:
            i=i.replace("\n","")
            custome_dict.update({custome_id: i.split(",")})
            custome_id=custome_id + 1
        file.close()
        return custome_dict

    #defining function for checking valid ID
    def valid_ID(dictionary):
        #handling exception
        try:
            valid_id = int(input("Enter the ID of custome you want to rent:"))  
            while valid_id <= 0 or valid_id > len(dictionary):
                print("\n")
                print("**"*20)
                print("               Invalid ID!!")
                print("**"*20)
                print("\n")
                View.view_costume()
                valid_id=int(input("Enter the ID of custome you want to rent:"))
                print("\n")
                
        except:
            print()
            print("**"*20)
            print("          Invalid Input!!!")
            print("**"*20)
            print()
            View.view_costume()
            valid_id=int(input("Enter the ID of custome you want to rent..Provide integer Value:"))
            #exception is handeled
        return valid_id
        

    #defining function to decleare the quantity of costume you want to rent
    def custome_quantity():
        #exception handling
        try:
            quantity=int(input("Enter the quantity of Costume you want to rent:"))    
            while quantity <= 0 or quantity > int(custome_dict[valid_id][3]):
                if quantity <= 0:
                    print("")
                    print("**"*20)
                    print("         Invalid Quantity!!!")
                    print("**"*20)
                    print("")
                else:
                    print("")
                    print("**"*20)
                    print("         Out of the stock !!!")
                    print("**"*20)
                    print("")
                quantity=int(input("Enter the quantity of Costume you want to rent..:"))
        except:
            print()
            print("**"*20)
            print("          Invalid Input!!!")
            print("**"*20)
            print()
            quantity=int(input("Enter the quantity of Costume you want to rent...Provide integer value:"))
            #exception is handeled
        return quantity

    #updating stocks of custome
    custome_dict= stock_dict()
    
    #creating loop
    do= True
    while do== True:
        valid_id= valid_ID(custome_dict)
        print("")
        print("**"*20)
        print("       Costume is available!!")
        print("**"*20)
        print("")
        quantity=custome_quantity()
        print("")
        custome_dict[valid_id][3]=int(custome_dict[valid_id][3])-quantity
        print(custome_dict)
        print("")

        #appending values in a list
        a.append (int(custome_dict[valid_id][2].replace("$",""))*quantity)
        l.append(custome_dict[valid_id][0])

        #asking user if they want to rent more..
        Again= input("Do you want to rent more? Press Yes to continue:")
        if Again=="Yes":
            do=True      
        else:
             do=False
        
    #Asking name and email of costumer         
    bill=True
    while bill==True:
        name = input("Enter your Name: ")
        x=name.isalpha()
        if x==True:
            break
        else:
            print("")
            print("**"*20)
            print("    Name must be an alphabet!!!!!")
            print("**"*20)
            print("")
            
    email= input("Enter your Email: ")
    
    #creating a bill after renting a costume
    print("")
    print("--"*35)
    print("                               INVOICE!")
    print("--"*35)
    print("**"*20)
    print("Name of the customer:"+str(name))
    print("Email:"+str(email))
    print("Date and time of Rent:"+str(date_time))
    print("Items Rented:",l)
    print("The Grand Total is:$", str(sum(a)))
    print("**"*20)
    print("")
    print("**"*35)
    print("  Thank you for renting!!..Costume should be returned within 5 days! ")
    print("                  $5 will be charged per day....")
    print("**"*35)
    print("")

    #creating a file to update stocks
    file=open("rent_update.txt", "w")
    for values in custome_dict.values():
        file.write(str(values[0])+","+str(values[1])+","
                    +str(values[2])+","+str(values[3])+",")
        file.write("\n")
    #closing file
    file.close()

    #creating a file to create Invoice
    file = open("rent_bills.txt","w")
    file.write("")
    file.write("--"*35)
    file.write("\n")
    file.write("                               INVOICE!")
    file.write("\n")
    file.write("--"*35)
    file.write("\n")
    file.write("\n")
    file.write("**"*20)
    file.write("\nName of the customer:"+str(name))
    file.write("\nEmail:"+str(email))
    file.write("\nDate and time of Rent:"+str(date_time))
    file.write("\nItems Rented:"+ str(l))
    file.write("\nThe Grand Total is:$"+ str(sum(a)))
    file.write("\n")
    file.write("**"*20)
    file.write("\n")
    file.write("\n")
    file.write("**"*35)
    file.write("\n  Thank you for renting!!..Costume should be returned within 5 days! ")
    file.write("\n                  $5 will be charged per day....")
    file.write("\n")
    file.write("**"*35)
    file.write("\n")
    #closing file
    file.close()
    
#Rent_costume()
