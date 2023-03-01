import json

file = open('students.json', 'r')
data = json.load(file)
file.close()


subjects = []
for s in data['Students']:
    if s['Major'] not in subjects:
        subjects.append(s['Major'])

print(subjects)
