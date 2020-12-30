try:
  x=int(input("Enter A Number eg: 5"))
  if x >=0 and x<=5:
    print("Small")
    print("Done")
  else:
    print("big")
    print("Done")
except ValueError:
  print("Done")