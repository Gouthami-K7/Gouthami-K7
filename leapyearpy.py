num=int(input("Enter Year: "))
if num%400 ==0:
    print("It is a Leap year ")
elif num%4==0 and num%100!=0:
    print("It is a leap year")
else:
    print("not a leap year")
for num in range(1800,1890):
    print("18th centuary")

for num in range(1900,1990):
    print("20th centuary")

for num in range(2000, 2090):
    print("21st centuary")


