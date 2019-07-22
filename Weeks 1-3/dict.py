names_list = ["Linda", "Susan", "Kristen"]
age_list = [18, 20, 21]
major_list = ["Art", "Nursing", "Physics"]
key_list = ["Name", "Age", "Major"]
student_stats = []
for i in range(3):
    tempDict = {}
    tempDict[key_list[0]] = names_list[i]
    tempDict[key_list[1]] = age_list[i]
    tempDict[key_list[2]] = major_list[i]
    student_stats.append(tempDict)
print(student_stats)
