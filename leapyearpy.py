num=int(input("Enter Year: "))
if num%400 ==0:
    print("It is a Leap year ")
elif num%4==0 and num%100!=0:
    print("It is a leap year")
else:
    print("not a leap year")
if 1800 <= num <= 1899:
    print("It is the 19th century")
elif 1900 <= num <= 1999:
    print("It is the 20th century")
elif 2000 <= num <= 2099:
    print("It is the 21st century")
else:
    print("Year is out of the specified century range")


