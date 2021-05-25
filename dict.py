person = {}
s = "IVANOV IVAN Kazan KFU 5 4 5 3 4 4 5"
s = s.split()
person['lastname'] = s[0]
person['firstname'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(s)
print(person)