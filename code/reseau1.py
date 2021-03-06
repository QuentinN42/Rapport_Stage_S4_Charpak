# imports
from keras import Sequential, optimizers, layers
import numpy as np
from random import random

def f(X):                   # La fonction que l'on cherche
    W = np.array([0.2, 0.8])# Le vecteur poids
    return W @ X            # Produit scalaire

act = "linear"   # Fonction d'activation
n_input = 2      # Nombre de neurones
# generation des questions/reponses attendues
questions = np.array([np.array([random(), random()])
                    for i in range(10000)])
reponses  = np.array([f(q) for q in questions])

sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
neurones = layers.Dense(1, activation=act, input_dim=n_input, use_bias=False)  # Creation des neurones
model = Sequential()            # On cree un reseau
model.add(neurones)             # On lui ajoute des neurones
model.compile(optimizer=sgd,    # On compile le tout
              loss="mean_squared_error")
model.fit(questions, reponses)  # On essaye de coller aux données

for i, weight in enumerate(model.get_weights()[0]):
    # on affiche les poids
    print(f"w{i} : {weight[0]}")
