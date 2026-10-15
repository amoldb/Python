# records
bob = dict(name='Bob Smith', age=43, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=40, pay=40000, job='hdw')
tom = dict(name='Tom Hardy', age=53, pay=100000, job='Actor')

# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == "__main__":
    for key in db:
        print(key, '=> ', db[key])

