"""input a name and print alternative character"""
name= input("enter name")
#error check for the name to blank
while len(name)<=1:
    name=input("Enterthe name")

print(name::2)