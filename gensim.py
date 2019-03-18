# Gensim was developed and is maintained by the Czech natural language processing researcher Radim Řehůřek and his company RaRe Technologies.

#  https://machinelearningmastery.com/develop-word-embeddings-python-gensim/
# https://radimrehurek.com/gensim/models/word2vec.html

from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

# define training data
sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
			['this', 'is', 'the', 'second', 'sentence'],
			['yet', 'another', 'sentence'],
			['one', 'more', 'sentence'],
			['and', 'the', 'final', 'sentence']]
# train model
model = Word2Vec(sentences, min_count=1)
# summarize the loaded model
print(model)

# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# access vector for one word
#print(model['sentence'])
# save model
model.save('model.bin')
# load model
new_model = Word2Vec.load('model.bin')
print(new_model)

X = model[model.wv.vocab]

pca = PCA(n_components=2)
result = pca.fit_transform(X)
print(result)

pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()