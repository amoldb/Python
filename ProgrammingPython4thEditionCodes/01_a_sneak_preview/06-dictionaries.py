# Method 1 to create dictionary
bob = {'name': 'Bob Smith', 'age': 42, 'salary': 30000, 'work': 'Software'}
sue = {'name': 'Sue Jones', 'age': 45, 'salary': 40000, 'work': 'Hardware'}

print(bob['name'], sue['salary'])

# Method 2 to create dictionary
flash = dict(name='Barry Allen', age=22, ability='lightning fast')
batman = dict(name='Bruce Wayne', age=28, ability='Expert in tactics, detective')

print(flash['name'], batman['ability'])

# Method 3 to create dictionary
suphero = {}
suphero['name'] = "Spiderman"
suphero['age'] = 16
suphero['skill'] = "Throws a web"

print(suphero)

# Method 4 to create dictionary
names = ["name", "age", "pay", "job"]
values = ["Jerry Stacy", 52, 300000, "Executive"]

emp = dict(zip(names, values))
print(emp)

fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, None)

print(record)

print("List of dictionaries")
people = [bob, sue]
for person in people:
    print(person['name'], person['salary'], sep=", ")

names = [person['name'] for person in people]
print(names)

print(list(map((lambda x: x['name']), people)))

print([rec['name'] for rec in people if rec['age'] >= 45])

print([rec['age'] ** 2 if rec['age'] >= 45 else rec['age'] for rec in people])

G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

H = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(H.__next__())

print("Nested structures")
bob2 = {"name": {"first": "Bob", "last": "Smith"},
        "age": 42,
        "job": ["software", "writing"],
        "pay": (40000, 50000)}
print("We have to index twice")
print(bob2['name'])
print(bob2['name']['last'])
print(bob2['pay'][1])

for job in bob2['job']:
    print(job)

print("Add new job")
bob2['job'].append('janitor')
print(bob2)

