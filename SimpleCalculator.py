num1=int(input("Enter the 1st number"))
num2=int(input("Enter the second number"))

while True:
  print("1.Addition ")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Division")
  print("5.Remainder(Modulus)")
  print("6.Square")
  print("7.Exit")

  choice=input("Enter the choice")

  if choice=='1':
    print(num1+num2)
  elif choice=='2':
    print(num1-num2)
  elif choice=='3':
    print(num1*num2)
  elif choice=='4':
    if num2==0:
      print("num2 cannot be zero")
    else:
      print(num1/num2)
  elif choice=='5':
    print(num1%num2)
  elif choice=='6':
    print(num1**num2)
  elif choice=='7':
    print("Bye!")
    break
  else:
    print("Invalid choice")


