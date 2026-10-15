# The short story of Bob and Sue.

print("There are 2 characters in this story, Bob and Sue")
bob = ['Bob Smith', 42, 30000, 'Software']
sue = ['Sue Jones', 45, 40000, 'Hardware']

print("="*70)
print("Name\t\t|\tAge\t|\tSalary\t|\tField of work")
print("-"*70)
print("\t|\t".join([str(info) for info in bob]))
print("\t|\t".join([str(info) for info in sue]))
print("="*70)

# The fields here simply gives a tuple as a result
print("The fields in both list gives a tuple as a result")
print(bob[0], sue[2])

print("Now give Sue a 25% raise")
# Give a raise to Sue by modifying the list element in-place.
print("="*70)
print("Name\t\t|\tAge\t|\tSalary\t|\tField of work")
print("-"*70)
sue[2] *= 1.25
print("\t|\t".join([str(info) for info in bob]))
print("\t|\t".join([str(info) for info in sue]))
print("="*70)

