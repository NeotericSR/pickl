import pickle

def storeData():
     # initializing data to be stored in dbx
    Okoye = {'key' : 'Okoye', 'name' : 'Okoye Bilikha',
    'age' : 21, 'pay' : 40000}
    Kaljob = {'key' : 'Kaljob', 'name' : 'Kaljob Bilikha',
    'age' : 50, 'pay' : 50000}

    # database
    db = {}
    db['Okoye'] = Okoye
    db['Kaljob'] = Kaljob

    # Its important to use binary mode
    dbfile = open('examplePickle', 'ab')

    # source, destination
    pickle.dump(db, dbfile)

def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

if __name__ == '__main__':
    storeData()
    loadData()
