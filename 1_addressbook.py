#Project : Basic Address Book 
#Version 0.01
#hikmetdevlet@gmail.com


adressbook=dict() # Empty Dictionary



def add_name(name,number): # Function to add names and numbers
	adressbook[name]=number

print("Press 'q' to quit") 

while True: # Loop to keep program alive until write 'q' 
	name=input("Write contact name: \n") 
	if name =='q': #Control if user text 'q' or not
		break # stop the loop
	number=input("Write the Contact Number: \n")
	add_name(name,number)#add names and numbers to the dict trough function
	


print(adressbook)#Show all names and numbers
