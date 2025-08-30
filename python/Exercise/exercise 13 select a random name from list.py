import random

names=input("Enter everbody's name separated by comma : ")
names_list=names.split(",")

print(names_list)

# length=len(names_list)

# random_choice=random.randint(0,length-1)
person=random.choice(names_list)

print(f"{person} will pay the bill.")

# print(f"{names_list[random_choice]} will pay the bill.")
 
