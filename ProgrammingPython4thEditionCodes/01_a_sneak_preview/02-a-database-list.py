# The short story of Bob and Sue.

print("There are 2 characters in this story, Bob and Sue")
bob = ['Bob Smith', 42, 30000, 'Software']
sue = ['Sue Jones', 45, 40000, 'Hardware']

print("Put both the records in a list")
people = [bob, sue]

print("="*70)
print("Name\t\t|\tAge\t|\tSalary\t|\tField of work")
print("-"*70)
for person in people:
    print("\t|\t".join([str(info) for info in person]))
print("="*70)

print("Print sirnames of all people and give all people a 25% raise")
print("="*10)
print("Surname")
print("-"*10)
for person in people:
    person[2] *= 1.25
    print(person[0].split()[-1])
print("="*10)

print("Check the raised salary")
print("="*10)
print("Salary")
print("-"*10)
for person in people:
    print(person[2])
print("="*10)

print("Get all pays by list comprehension")
pays = [person[2] for person in people]
print(pays)

print("Get all pays by using map and lambda")
pays = map((lambda x: x[2]), people)
print(list(pays))

print("Use built-in sum method to get total pay")
print(sum(person[2] for person in people))

print("Use append, extend method to add a record")
people.append(['Tom riddle', 50, 0, 'Magician'])

ident = [1] 
for person in people:
    person.extend(ident)
    ident[0] += 1

print(people)
print("="*70)
print("Name\t\t|\tAge\t|\tSalary\t|\tField of work")
print("-"*70)
for person in people:
    print("\t|\t".join([str(info) for info in person]))
print("="*70)
