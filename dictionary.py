# writing a Dictionary for student names
student_id_t0_name ={  # student_id_to_name is the dictionary and "{}" are oping and closing section.
101 : "shiva", # 101 = key and shiva = value
102: "ram",
103: "sharan",
104: "rajesh",
105: "pawan"
}
print(student_id_t0_name[102])
print(student_id_t0_name.get(105))
student_id_t0_name[106] = "kalyan" # it is used to add new key and vale
print(student_id_t0_name[106])

for key,value in student_id_t0_name.items():
    print(key) # for finding all the keys in the dictionary
    print(value) #for finding all the values in the dictionary
    print(key ,"=",value)
# for checking the information
if 107 in student_id_t0_name:
    print("is a student")
else:
    print("is not a student")

if 101 in student_id_t0_name:
    print("is a student")
else:
    print("is not a student")