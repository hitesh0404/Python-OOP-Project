from mammals import Person
n=0
while(n!=5):
    print("1. Create a Person object")
    print("2. Get the details of a Person object")
    print("3. Buy a Car")
    print("4. Details of Cars")
    print("5. Exit")
    n=int(input("Enter your choice:"))
    if(n==1):
        name=str(input("Enter your name:"))
        age=int(input("Enter your age:"))
        species= str(input('Enter your Species'))
        society_name = str(input("Enter your Society_name"))
        location =str(input("Enter your Location"))
        net_worth =float(input("Enter your Net_Worth"))
        person=Person(name=name,age=age,species=species,society_name=society_name,location=location,net_worth=net_worth)
        print(person.__dict__)
    elif (n==2):
        name=input("Enter your name:")
        if Person.persons:
            for i in Person.persons:
                print(i.__dict__)
                if i.name==name:
                    print(i.__dict__)
                else:
                    print("Person not found")
        else:
            print("No persons created")
            
    elif(n==3):
        name=input("Enter your name:")
        for i in Person.persons:
            if i.name==name:
                print("You can buy a car")
                make = input('Enter the car make: ')
                model = input('Enter the car model: ')
                year = input('Enter the car year: ')
                engine_size = input('Enter the engine size: ')
                num_doors = input('Enter the number of doors: ')
                seats = input('Enter the number of seats: ')
                i.buy_car(make, model, year, engine_size, num_doors,seats)
                print("Car bought successfully")
                break
            else:
                print("Person not found")
    elif(n==4):
        name=input("Enter your name:")
        for i in Person.persons:
            if i.name==name:
                for j in i.cars:
                    print(j.__dict__)
                break
            else:
                print("Person not found")
    

