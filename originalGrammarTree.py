"""
Author: Grezia Trujillo
Date: 28 April 2026
Project: Context free grammar final model
Purpose of the project: Represent final model of generated CFG with an
example input of a string.
"""

import nltk
from nltk import CFG

#the following two lines are to be uncommented and run ONCE for first time download of nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


#define grammar from Italian
italian_grammar = CFG.fromstring("""
    S -> NP VP Punct | VP Punct | NP Punct
    
    NP -> NPF | NPM | NP PP | NP Conj NP | Conj VP
    NPM -> DetM NM
    NPF -> DetF NF
    
    VP -> V | VP NP | VP PP
    PP -> P NP
    
    DetM -> 'il' | 'lo' | 'un'
    DetF -> 'la' | 'una'
    
    NM -> 'bambino' | 'gatto' | 'treno' | 'cavallo' | 'pennello' | 'fiore' | 'coniglio'
    NF -> 'bambina' | 'anatra' | 'bicicletta' | 'farfalla' | 'volpe'
    
    P -> 'con' | 'di' | 'per'
    V -> 'cammina' | 'nuota' | 'corre' | 'esce' | 'cerca' | 'mangia' | 'salta' | 'dipinge' | 'vola' | 'cresce'
    
    Conj -> 'e' | 'per' | 'ma' | 'o'
    Punct -> '.' | '!'
""")

#parser
parser = nltk.ChartParser(italian_grammar)

#test parser with a sample sentence (split sentence into words)
sentence = 'il bambino cerca il gatto di la bambina .'.split()

#generate and display tree(s)
trees = list(parser.parse(sentence))

for tree in parser.parse(sentence):
    tree.pretty_print()
