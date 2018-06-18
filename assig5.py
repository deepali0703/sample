#ques 1

year=int(input("enter year"))
if((year%4)==0):
    print("this is a leap year")
else:
    print("this is not a leap year")

#ques 2

length=int(input("enter length"))
breadth=int(input("enter breadth"))
if(length==breadth):
    print("it is a square")
else:
    print("it is a rectangle")

#ques 3

a=int(input("enter age of a"))
b=int(input("enter age of b"))
c=int(input("enter age of c"))
if((a>b) and (a>c)):
    print("a is oldest")
elif((b>a) and (b>c)):
    print("b is oldest")
else:
    print("c is oldest")

a=int(input("enter age of a"))
b=int(input("enter age of b"))
c=int(input("enter age of c"))
if((a<b) and (a<c)):
    print("a is younger")
elif((b<a) and (b<c)):
    print("b is younger")
else:
    print("c is younger")

#ques 4

points=int(input("enter points"))
if((points>1) and (points<50)):
    print("sorry! No prize this time")
if((points>51) and (points<150)):
    print("Congratulations! You won a wooden dog")
if((points>151) and (points<180)):
    print("Congratulations! You won a book")
if((points>181) and (points<200)):
    print("Congratulations! You won a chocolates")
else:
    print("wrong input")

#ques 5

unit=int(input("enter unit"))
cost=unit*100
print("cost",cost)
if(cost>1000):
    print("amount",cost*0.10)
else:
    print("no discount")