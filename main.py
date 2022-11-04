#!/usr/bin/python3
import numpy as np

# Définitions des portes quantiques
i_gate = np.array([[1,0],[0,1]])
x_gate = np.array([[0,1],[1,0]])
h_gate = np.sqrt(0.5) * np.array([[1,1],[1,-1]])
cx_gate = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])

#Produits tensoriels de portes quantiques
ih_gate = np.kron(i_gate, h_gate)

#Paire de Bell, état produit des portes quantiques cx_gate multiplié par ih_gate
b_circuit = cx_gate @ ih_gate

if __name__== "__main__":
    init_state = np.array([1,0,0,0]).T
    b_state = b_circuit @ init_state
    print(b_state)

