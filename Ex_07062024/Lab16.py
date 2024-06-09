#strings
#Bunch of Characters
# '',"",""" """
#string is immutable
#string is sequence of characters
#string is iterable
name = 'Sangram'
print(name)

name = "Sangram"
print(name)

name = """Sangram,is a Software Test Engineer
He loves to Learn new things"""
print(name)

#DIR
dir = "C:\newTheTestingAcademy\WorkSpace for Python Codes\PyLearning3xATB"
print(dir)

#prefix r(r is raw String) before directory
dir = r'C:\newTheTestingAcademy\WorkSpace for Python Codes\PyLearning3xATB'
print(dir)

#format of the string
First_Name = "Sangram"
Last_Name = "Patil"
print(First_Name,"",Last_Name)
print(First_Name+ " " +Last_Name)

#f is formatting and it will replace the values to the variables
#{} -- > Placeholders
print(f"Your Name is {First_Name} {Last_Name}")