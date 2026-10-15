# Don't remember the field numbers, let us label them

def get_field(records, label):
    for rec_name, rec_value in records:
        if rec_name == label:
            return rec_value

print("There are 2 characters in this story, Bob and Sue")
bob = [['name', 'Bob Smith'], ['age', 42], ['salary', 30000], ['work', 'Software']]
sue = [['name', 'Sue Jones'], ['age', 45], ['salary', 40000], ['work', 'Hardware']]

print("Put both the records in a list")
people = [bob, sue]

print("="*70)
print("Name\t\t|\tAge\t|\tSalary\t|\tField of work")
print("-"*70)
for person in people:
    print("\t|\t".join([str(info[1]) for info in person]))
print("="*70)

print("Print sirnames of all people and give all people a 25% raise")
print("="*10)
print("Surname")
print("-"*10)
print(get_field(people[0], "name").split()[-1])
print(get_field(people[1], "name").split()[-1])
print("="*10)

print("Check the raised salary")
print("="*10)
print("Salary")
print("-"*10)
for person in people:
    print(get_field(person, "salary"))
print("="*10)

print("Get all pays by list comprehension")
pays = [get_field(person, "salary") for person in people]
print(pays)

print("Get all pays by using map and lambda")
pays = map((lambda x: get_field(x, "salary")), people)
print(list(pays))

print("Use built-in sum method to get total pay")
print(sum(get_field(person, "salary") for person in people))

print("Use append, extend method to add a record")
people.append([['name', 'Tom riddle'], ['age', 50], ['salary', 0], ['work', 'Magician']])

print("="*70)
print("Name\t\t|\tAge\t|\tSalary\t|\tField of work")
print("-"*70)
for person in people:
    print("\t|\t".join([str(info[1]) for info in person]))
print("="*70)

