greeting = "Good Morning, "

#name = "Subash"

#print(name[-2])

#name = greeting + name

#print(name)

#print(len(name))

#print(name[1:3:2])

#practice


story = "My son was born in November."

print(len(story))

print(story.endswith("."))

print(story.count("o"))

print(story.find("born"))

print(story.replace("son", "daughter"))

name1 = input("Enter your name:\n")

print("Good afternoon, " + name1)


letter = """Dear <|NAME|>,
We are very pleased to announce you that 
You are selected!
Have a great day ahead!
Thanks and regards
Date: <|DATE|>

"""
name = input("Enter your name\n")
date = input("Enter Date\n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)


val = "This is a string with double  spaces"

doubleSpaces = val.find("  ")


print(doubleSpaces)









































print(letter)

