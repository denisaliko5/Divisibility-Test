print("This program can check if an integer is divisible by another integer\n")
dividend = int(input("Enter an integer: "))
divisor = int(input("Enter an divisor: "))
if float(dividend/divisor) - int(dividend/divisor) > 0:
  print(dividend, "is not divisible by", divisor)
else:
  print(dividend, "is divisible by", divisor)
  print("It's", str(int(dividend/divisor)) + ".")