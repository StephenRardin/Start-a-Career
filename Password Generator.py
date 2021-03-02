import random
choice = "y"

while choice == "y":
  for n in range(10):
    password = ""
    for i in range(12):
      #rand = random.randint(33, 126)
      #new = chr(rand)
      password += chr(random.randint(33, 126))
    print("Pass",n+1, "is:", password)

  choice = input("\nWould you like to get another set of passwords? y/n: ").lower()
  if choice != "y" and choice != "n":
    print("\nsorry didn't understand that, let try that one last time.")
    choice = input("Would you like to get another set of passwords? y/n: ").lower()
print("\nOk, enjoy your passwords")

#Would it be better to append to List and print all at once?
#Print to external file?
