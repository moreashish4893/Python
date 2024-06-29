friends = {
    "Ashish" : "1234567890",
    "Abhishek" : "2134567809",
    "Rajith" : "5432167809"
}

print("Current friends list:")
for name in sorted(friends):
    print(f"{name}:{friends[name]}")

name = input("Enter a friends name:")

if name in friends :
    print(f"{name}'s phone number is {friends[name]}")
else :
    friends[name] = input(f"Enter the phone number for {name}:")
    print(f"{name} has been added to the dictionary.")

    print("\nUpdated friends list:") 
    for name in sorted (friends):
        print(f"{name}:{friends[name]}")    