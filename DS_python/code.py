# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here

courses = {'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}
print(courses)
total = courses['Math']  + courses['English'] + courses['History'] + courses['French'] + courses['Science']
print(total)
percentage = (total * 100/500)
print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics = {'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Benji':50,
'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}
print(mathematics)              

max_marks_scored = max(mathematics, key = mathematics.get)
topper = max_marks_scored
print(topper)
# Code ends here    


# --------------
# Given string
topper = 'andrew ng'
print(topper)

# Code starts here
print('='*20)
#first_name,last_name = print(topper.split(" "))
first_name,last_name = topper.split(" ")
print("first name is : " + first_name)
print("last name is : " + last_name)

full_name = last_name + " " + first_name
print(full_name)
certificate_name = (full_name.upper())
print(certificate_name)
#print(certificate_name)
# Code ends here


