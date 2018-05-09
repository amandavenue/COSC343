from SRNClassifier import SRNClassifier
import pickle
import gzip

clf = SRNClassifier(alpha=1e-2, hidden_layer_size=32, activation='tanh', max_iter=100, verbose=True)

clf.fit(x, y)

with gzip.open("question1a.txt", 'w') as f:
    pickle.dump(clf, f)

