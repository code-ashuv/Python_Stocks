# this is to test python skills

# Program to get input 5 numbers and show there sum
# handle all scenarios

################
count = 1
while count < 6:
    try:
        Input_number = input("Please enter number %f: "%count)
        count += 1
    except:
        print ("Failed")
print (Input_number)
