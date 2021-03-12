total=0
entry=""
while(entry != "exit"):
    entry=input("Enter a number to add it to the total value,enter exit to terminate program\n>>").lower()
    if entry.isdigit():
        total+=int(entry)
    print("total is:",total)
    
