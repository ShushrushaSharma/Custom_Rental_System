#creating an empty dictionary for storing stocks
dict={}

#defining a function to view stocks of costume
def view_costume():
    print("-----------------------------------------------")
    print("SN\tName(Dress)\tCompany\t Price\tQuality")
    print("-----------------------------------------------")

    #reading a txt file
    file=open("Stocks.txt","r")
    costume_data= file.read()
    costume_data= costume_data.split("\n")

    '''creating a list'''
    for i in range(len(costume_data)):
        # 1d list
        dict[i+1]=costume_data[i].split(",")

    '''storing values in dictionary'''
    for key,value in dict.items():
        print(key,end="\t")
        for i in value:
            print(i,end="\t")
        print("\n")
        print("-----------------------------------------------")
        
#view_costume()        

  

