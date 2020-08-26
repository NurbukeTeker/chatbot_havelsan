import numpy as np
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

class WordEmbedding():
    def __init__(self):
        self.num = 0
        #nobody does nothing 
        
    def w2vecCreation(self,corpus,min_Count):
        model = Word2Vec(corpus, size = 300, window = 5, min_count = min_Count, sg = 1)
        lenvocab = len(model.wv.vocab)  # get len() for use in name
        print(lenvocab)
        model.save(('./w2v_word{}_size300_({}).model'.format(min_Count,lenvocab))) ##load model !!Care Name of Model
        vocab = [word for word in model.wv.vocab] ###vocabulary for model
        file = open("w2v_word{}_size300_({}).txt".format(min_Count,lenvocab),"w") 
        for i in vocab:
            file.write(i)
            file.write("\n")
        file.close()
        return model  
        
        
   
        


    def closestwords_tsneplot(self,model, word):
        word_vectors = np.empty((0,300))
        word_labels = [word]
        
        close_words = model.wv.most_similar(word)
        
        word_vectors = np.append(word_vectors, np.array([model.wv[word]]), axis=0)
        
        for w, _ in close_words:
            word_labels.append(w)
            word_vectors = np.append(word_vectors, np.array([model.wv[w]]), axis=0)
            
        tsne = TSNE(random_state=0)
        Y = tsne.fit_transform(word_vectors)
        
        x_coords = Y[:, 0]
        y_coords = Y[:, 1]
        
        plt.scatter(x_coords, y_coords)
        
        for label, x, y in zip(word_labels, x_coords, y_coords):
            plt.annotate(label, xy=(x, y), xytext=(5, -2), textcoords='offset points')
            
        plt.show()
