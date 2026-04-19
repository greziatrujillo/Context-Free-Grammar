import nltk
from nltk import CFG

#the following two lines are to be uncommented and run ONCE for first time download of nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


#unambiguous CFG
italian_grammar = CFG.fromstring("""
    S -> NPC VP Punct | VP Punct | NPC Punct
    
    NPC -> NP | NPC PP | NP Conj NPC | Conj VP
    NP -> NPF | NPM
    NPM -> DetM NM
    NPF -> DetF NF
    
    VP -> V | VP NPC | V PP
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

#test parser with a sample sentence (split sentence into words)
sentence = 'il bambino cerca il gatto di la bambina .'.split()

#generate and display tree(s)
trees = list(parser.parse(sentence))

for tree in parser.parse(sentence):
    tree.pretty_print()