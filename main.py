my_name = input("what is your name?")
my_age = input("how old are you?")
print(f"my name is {my_name} and I am {my_age}")
first_number = int(input('first_number?'))
second_number = int(input('second_number?'))
operation = input("operation?")
if operation == "+" :
    print(first_number + second_number)
elif operation == "-" :
    print(first_number - second_number)
elif operation == "*" :
    print(first_number * second_number)
elif operation == "/" :
    print(first_number / second_number)
else :print('the operation is not valid')
bus_capacity = 45
people_inbus = int(input("people in bus?"))
people_tobeinbus = int(input("people to be in bus?"))
empty_seats = bus_capacity - people_inbus
if empty_seats > people_tobeinbus :
    print(f"there are free seats and there number is {empty_seats - people_tobeinbus}")
elif empty_seats < people_tobeinbus :
    print("the bus is full")
else:
    print("really?")