import pickle
data = [1, 1, 1]

with open('data.pickle', 'wb') as f:
    pickle.dump([], f)

with open('data.pickle', 'rb') as f:
    f_enw = pickle.load(f)

    print(f_enw)