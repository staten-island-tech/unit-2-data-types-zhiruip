#x = 3
#y = float(3)
#print(x,y)

#values = [1,2.23,5,7,2,30,15,]
#print(values)
#for i in values:
#    print(values[7])


#x = "this is a thing"
#y= x.split( )
#z = y[0]
#print(y)
#print(z

#def ask(x):
   #x = input("enter a sentence: ")
   #y=x.split( )
   #print(f"the total numbers in the input is {len(y)}")
   
#ask(1)

#def oddeven(x):
    #number = int(input("Input your number: "))  # Make sure to cast input to an integer
    #if number % 2 == 0:
        #print(f"{number} is even")
    #else:  
        #print(f"{number} is odd")
#oddeven(1)


 
#global_bill = float(input("How much was your bill?: "))  # Global variable

#def tip_calc():
    #global global_bill  # Access the global variable
    #tip_percent = input("Enter tip (e.g., 0%, 15%, 20%, 25%): ")
    
    #if tip_percent == "0%":
        #bill = global_bill * 1  # Apply the tip percentage

   # if tip_percent == "15%":
        #bill = global_bill * 1.15  # Apply the tip percentage
    
    #if tip_percent == "20%":
        #bill = global_bill * 1.20  # Apply the tip percentage

    #if tip_percent == "25%":
        #bill = global_bill * 1.25  # Apply the tip percentage
    
    
    #print(f"Your meal costs {bill}")

#def tipping_service():
    #global global_bill  # Access the global variable
    #service = input("Was the service bad, okay, good, or great?: ")
    
    #if service == "bad":
        #print("Sorry! If it was bad, you don't need to tip!")
        #print("Would you like to tip 0%, 15%, 20%, or 25%?")
    
    #if service == "okay":
        #print("Alright, I recommend you tip 15%")
        #print("Would you like to tip 0%, 15%, 20%, or 25%?")

    #if service == "good":
        #print("Thanks, I recommend you tip 20%.")
        #print("Would you like to tip 0%, 15%, 20%, or 25%?")

    #if service == "great":
       # print("Thank you! I recommend tipping 25% ;D !!")
        #print("Would you like to tip 0%, 15%, 20%, or 25%?")
    
    #tip_calc()  # Call the tip calculation function
#tipping_service()

#def all_factors():
    #number=int(input("whats your number"))
    #for i in range(1, number + 1):
        #if number % i == 0:
            #print(f"the factors for {number} is {i}")
    
#all_factors()

def gcf(x, y):
    alfred= []
    for i in range(min(x, y) + 1, 0, -1):
        if x % i == 0 and y % 1 == 0:
            alfred.append(i)
            return alfred[0]
print(gcf(400,100))

