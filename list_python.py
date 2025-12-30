# lists in python
coding_languages = ["java" ,"python","html","css"]
print(coding_languages[0])
print(coding_languages[-2])
print(coding_languages[1:4])

number_1 = [1,2,3,4,5]
number_2 = [4,5,6,7,8]
print(number_1 + number_2)

number_3 = [3,5]
number_3.append(6) #it is used added an element to list
print(number_3)

number_4 = [22,33]
number_5 = [44,55]
number_4.extend(number_5) # its is used to add two list together
print(number_4)

number_6 = [123,789]
number_6.insert(1,456) #it is used to add the object in the list at any position
print(number_6)

number_7 = [12,15,14]
number_7.remove(15) # it is used to remove the elements from the list
print(number_7)

number_0 = [1,2,3,4,5]
number_0.clear() # it clear the whole list and make it empty
print(number_0)


number_8 = ["a","aa"]
number_new = number_8.copy() # it is used for coping from other list
print(number_new)

number_9 = [1,2,4,1,1,5,6]
number_9.sort() # Sorts the list in ascending order in place
print(number_9)

number_10 = [7,6,5,4]
number_10.reverse() #Reverses the order of the elements in the list in place.
print(number_10)

number_11 = [1,1,3,2,1,2,1,3,1]
number_12 = number_11.count(1) #Returns the number of times a specified element appears in the list.
print(number_12)