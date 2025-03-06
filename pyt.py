try:
    a=int(input("enter the row: "))
    print(a)
except ValueError:
    print("invalid")

print("the end")

try:
   a=int(input("enter the number: "))
   b=[3,4]
   print(b[a])

except IndexError:
    print("invalid")


print(" abcd")