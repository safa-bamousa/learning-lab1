#Variables
str_length = input("Please type Length: \n")
str_width = input("Please type width: \n")
str_cost = input("How much for 1 meter?: \n")
#Convert Types:
length = float(str_length)
width = float(str_width)
cost = float(str_cost)
#Calculate 
total_area = length * width
total_cost = total_area * cost
#print
print("The total area is:" , total_area)
print("Give the guy:" , total_cost ,"$")
