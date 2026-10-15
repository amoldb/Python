import pprint


bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=40, pay=40000, job='hdw')

db = {}
db['bob'] = bob
db['sue'] = sue

print(db['bob']['name'])
print("Increase Sue's pay")
db['sue']['pay'] = 50000
print(db['sue']['pay'])

print("Print without pretty-print")
print(db)

print("Print with pretty-print")
pprint.pprint(db)

print("Step through one record at a time")
for key in db:
    print(key, '~>', db[key]['name'])
    print(key, '~>', db[key]['pay'])

print("Step through dictionary's values to access records directly")
for values in db.values():
    print(values['pay'])

print("Get list of names")
x = [db[key]['name'] for key in db]
print(x)

print("Add new record")
db['tom'] = dict(name="Tom Hardy", age=50, job="Actor", pay=100000)
pprint.pprint(db)

