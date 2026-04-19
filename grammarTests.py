"""
Author: Grezia Trujillo
Date: 28 April 2026
Project: Context free grammar automated tests.
Purpose of the project: Validate generated CFG with multiple tests of strings that will either work or not work to 
demonstrate the structure of the grammar.
"""

import nltk
from nltk import CFG

italian_grammar = CFG.fromstring("""
    S -> NPC VP Punct | VP Punct | NPC Punct
    
    NPC -> NP | NP PP | NP Conj NPC | Conj VP
    NP -> NPF | NPM
    NPM -> DetM NM
    NPF -> DetF NF
    
    VP -> V | V NPC | V PP
    PP -> P NPC
    
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

#generate different sentences to test the grammar
sentences = [
    #accepted
    'il bambino cerca il gatto di la bambina .',
    'il bambino cerca e corre .',
    'la bambina e il bambino .',
    'la bambina cerca il gatto e il fiore di il bambino .',
    'il fiore di la bambina !',
    'la bambina e la volpe .',
    'la volpe o il gatto .',
    'il cavallo corre o salta !',
    'la farfalla vola .',
    'la bicicletta di il bambino .',
    'il coniglio di il treno .',
    'la volpe con il coniglio !',
    'la volpe dipinge con il pennello .',
    'la bambina corre con il cavallo !',

    #not accepted due to mismatch in gender
    'la gatto corre .',
    'la bambino mangia e salta .',
    'la farfalla e il volpe !',

    #not accepted due to missing DetM or DetF
    'bambino cerca il gatto .',
    'farfalla vola !',
    'treno esce !',

    #not accepted due to missing NP or VP
    'la gatto corre con il !', 
    'la volpe cerca il .' 
]

#sentences are accepted or not accepted and categorized
accepted = []
notAccepted = []

#parse through the sentences and categorize
for sentence in sentences:
    sentence = sentence.split()
    trees = list(parser.parse(sentence))

    #if tree generates, sentence is accepted
    if trees:
        accepted.append(sentence)
        for tree in trees:
            tree.pretty_print()
    else:
        notAccepted.append(sentence)

#print the sentences that were not accepted each one in a new line
print("Sentences not accepted:")
for s in notAccepted:
    print(" ".join(s))
