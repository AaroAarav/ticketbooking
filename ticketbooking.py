#Ticket Booking System

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

while True:
    print("Seats: ")
   
    for i in range(len(l)):
        print(l[i], end=" ")

    print("\n\n")
    print("Choose ticket")
    ch=int(input("Ticket number: "))
    if l[ch-1]!="BKD":
        l[ch-1]="BKD"
        print("Booked! Thank You ")

    else:
        print("Unavailable, sorry")

    c=int(input("More tickets? \n1.Yes \n2.No \n\n"))
    if c==1:
        pass
    elif c==2:
        print("Thank You \n")
        break

