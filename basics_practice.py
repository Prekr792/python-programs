dict1 = {"apple": "Fruit",
         "Mango": "Fruit", "Banana" : "Fruit", "Carat": "Vegetable"}

dict1["Tomato"] = "Vegetable"
dict1["Other Fruits"] = ["Watermelon", "Jack fruit", "Kiwi", "Musk Melon"]
dict1["Other Vegetables"] = ["ladies finger", "Potato", "Raddish"]
print(dict1)

for i in dict1["Other Fruits"]:
    print(i)
    if "Kiwi" in i:
        print("Kiwi is present")


print("*" *40)
Computer_parts = [("Monitor", 5000), ("Speaker", 2000), ("CPU", 7500),
                    ("Mouse", 500), ("Keyboard", 700)]

for index, parts in enumerate(Computer_parts):
    print(f"{index+1} : {parts[0]}")
print("0 : Exit")
total = 0
choosen_parts = []
while True:
    choice = int(input("Choose a part: "))
    if choice == 0:
        print("Products purchased:")
        for index, parts in enumerate(choosen_parts):
            print(f"{index+1} : {parts[0]} - {parts[1]}")
        
        print(f"Total amount Rs.{total}")
        break
    choosen_parts.append(Computer_parts[choice-1])
    print(f"{Computer_parts[choice-1][0]} added to cart")
    total += Computer_parts[choice-1][1]






