'''importing a view file'''
import View

#defining function to include all the actions
def Return_costume():
    #creating an empty list
    l=[]
    q=[]
    
    import datetime
    #library, class and methods
    date = str(datetime.datetime.now().year) + "-" +str(datetime.datetime.now()
    .month) + "-" + str(datetime.datetime.now().day)
    time = str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now()
    .minute) + "-" + str(datetime.datetime.now().second)
    date_time = str(date) + " " + str(time)

    print("")
    print("**"*20) 
    print("        Let's return a costume!!")
    print("**"*20) 
    print("")

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
            valid_id = int(input("Enter the ID of custome you want to return:"))  
            while valid_id <= 0 or valid_id > len(dictionary):
                print("\n")
                print("**"*20)
                print("               Invalid ID!!")
                print("**"*20)
                print("\n")
                View.view_costume()
                valid_id=int(input("Enter the ID of custome you want to return:"))
                print("\n")
                
        except:
            print()
            print("**"*20)
            print("          Invalid Input!!!")
            print("**"*20)
            print()
            View.view_costume()
            valid_id=int(input("Enter the ID of custome you want to return..Provide integer Value:"))
            #exception is handeled...
        return valid_id
        

    #defining function to decleare the quantity of costume you want to rent
    def custome_quantity():
        try:
            quantity=int(input("Enter the quantity of Costume you want to return:"))    
            while quantity <= 0:
                if quantity <= 0:
                    print("")
                    print("**"*20)
                    print("         Invalid Quantity!!!")
                    print("**"*20)
                    print("")
                quantity=int(input("Enter the quantity of Costume you want to return:"))
        except:
            print()
            print("**"*20)
            print("          Invalid Input!!!")
            print("**"*20)
            print()
            quantity=int(input("Enter the quantity of Costume you want to return...Provide integer value:"))
            #exception is handeled...
        return quantity

    #updating stocks of custome
    custome_dict= stock_dict()
    
    #creating loop
    do= True
    while do== True:
        valid_id= valid_ID(custome_dict)
        print("")
        print("**"*20)
        print("           You can Return!!")
        print("**"*20)
        print("")
        quantity=custome_quantity()
        print("")
        custome_dict[valid_id][3]=int(custome_dict[valid_id][3])+quantity
        print(custome_dict)
        print("")

        #appending values in a list
        l.append(custome_dict[valid_id][0])
        q.append(quantity)

        #asking user if they want to return more..
        Again= input("Do you want to return more? Press Yes to continue:")
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
            print("The name of costumer is: ",name)
            break
        else:
            print("")
            print("**"*20)
            print("    Name must be an alphabet!!!!!")
            print("**"*20)
            print("")

    email= input("Enter your Email: ")

    #creating loop
    bill2=True
    while bill2==True:
        #handeling exception
        try:
            day=True
            while day==True:
                days=int(input("For how many days did you rent this costume?"))
                if days>=0:
                        day=False    
                else:
                    print("")
                    print("**"*20)
                    print("    Days cannot be negative!!!!!")
                    print("**"*20)
                    print("")
                bill2=False
        except:
            print("")
            print("**"*20)
            print("The days must be entered in a numeric value!!!!!")
            print("**"*20)
            print("")
            #exception is handeled
            
    if days>5:
        days=days-5
    else:
        days=0
        
    #declearing fine
    Total_quantity= int(sum(q))    
    Fine= days*5*Total_quantity
    Total_Fine=Fine
    
    #creating a bill after renting a costume
    print("")
    print("--"*20)
    print("                INVOICE!")
    print("--"*20)
    print("**"*20)
    print("Name of the customer:"+str(name))
    print("Email:"+str(email))
    print("Date and time of Return:"+str(date_time))
    print("Items Returned:",l)
    print("Quantity of items Returned respectively:",q)
    print("The Total Fine is:$", str(Total_Fine))
    print("**"*20)
    print("")
    print("**"*35)
    print("           Thank you for returning....SEE YA SOON!!! ")
    print("**"*35)

    #creating a file to update stocks
    file=open("return_update.txt", "w")
    for values in custome_dict.values():
        file.write(str(values[0])+","+str(values[1])+","
                    +str(values[2])+","+str(values[3])+",")
        file.write("\n")
    file.close()

    #creating a file to create Invoice
    file = open("return_bills.txt","w")
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
    file.write("\nDate and time of Return:"+str(date_time))
    file.write("\nItems Return:"+ str(l))
    file.write("\nQuantity of items Returned respectively:"+str(q))
    file.write("\nThe Total Fine is:$"+ str(Total_Fine))
    file.write("\n")
    file.write("**"*20)
    file.write("\n")
    file.write("\n")
    file.write("**"*35)
    file.write("\n      Thank you for returning....SEE YA SOON!!")
    file.write("\n")
    file.write("**"*35)
    file.write("\n")
    #closing file
    file.close()

#Return_costume()
