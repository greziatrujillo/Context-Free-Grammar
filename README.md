# E2 Generating and Cleaning a Restricted Context Free Grammar
## Description
In this project, a natural language has been chosen in order to create a context-free grammar (CFG). 

The language I have chosen for this project is Italian. Italian is a romantic language, therefore it not only deals with singular and plural versions, but also has feminine and masculine identifiers (Peyronel & Higgins, 2006). This makes the language a little more complex and extensive to work with, but it is necessary to find a way to work with these concepts in order to put together sentence structures that are in agreement. 

The Italian language works with the following sentence structure:

<ul>
<li>Subject: Who or what</li>
<li>Verb: action</li>
<li>Object: Who or what receives the action</li>
</ul>

All sentences will end with punctuation (period or exclamation point). It is possible to expand sentences by adding conjunctions or prepositions. Some examples of how sentences would work:

la bambina corre → The girl runs.<br>
il bambino cammina e nuota. → The boy walks and swims.<br>
il gatto dipinge con il pennello. → The cat paints with the brush.<br>
la farfalla e la bicicletta. → The butterfly and the bicycle.

### Context-free grammar 
Given a finite language, a CFG will be able to generate all possible patterns. These are typically used to design parsers, as it is a 4-tuple where (Sipser, 2006, pp. 99–115) :

<ul>
<li> V is a finite set called the variables, </li>
<li> Σ is a finite set, disjoint from V, called the terminals,</li>
<li> R a finite set of rules, with each rule being a variable and a</li>
string of variables and terminals, and
<li>S ∈ V is the start variable.</li>
</ul>

In our case, the variables, otherwise known as nonterminals, represent parts of speech and phrases, and the terminal symbols represent words or punctuation. The production rules will define the syntax or structure of my language using rules and symbols (Kumar, Kumar, Dubey, & Pathak, 2025, pp. 35–43) .


<b> Ambiguity </b>

Upon the creation of a CFG, it is common to encounter ambiguity, or strings that are derived ambiguously. This is specifically when a same string is able to be generated with different trees, or paths. Notably, this is because there are two parse trees, not two derivations (Sipser, 2006, pp. 99–115) (which will be explained later on). In the context of the grammar I am creating, ambiguity can be caused from verbs connecting directly to nouns or prepositions, among other possibilities. It is important to realize that upon working with a natural language, there are many complexities that result in a nonlinear process.

<b> Leftside recursion </b>

With derivation, every non-terminal will continuously be replaced until a terminal symbol is reached. This will create derivation trees, which are read left to right. Since I will be removing all left-side recursion in order to follow along with the push-down automata process, this will be considered a left most derivation (LMD). In this case, production rules are replaced from left to right (Kumar, Kumar, Dubey, & Pathak, 2025, pp. 35–43) .

## Models
In order to be able to analyze the syntax, it is necessary to correctly construct the grammar. This means the creation will go through three phases (eliminating ambiguity and left recursion) in order to reach the final result that will ultimately be implemented. This ensures clarity and efficiency in parsing the inputs (sentences) created to validate that they belong in the grammar.

### General grammar model
First, a general grammar is constructed to demonstrate the language’s syntax. Here, the basic syntactic rules and sentence structures are established. We start with non-terminals that trickle down into terminals that will lead into words or punctuation.

    S → NP VP Punct | VP Punct | NP Punct

    NP →  NPF | NPM | NP | NP PP | NP Conj NP | Conj VP
    NPM →  DetM NM
    NPF →  DetF NF
    
    VP →  V | VP NP | VP PP
    PP →  P NP
    
    DetM →  'il' | 'lo' | 'un'
    DetF →  'la' | 'una'
    
    NM →  'bambino' | 'gatto' | 'treno' | 'cavallo' | 'pennello' | 'fiore' | 'coniglio'
    NF →  'bambina' | 'anatra' | 'bicicletta' | 'farfalla' | 'volpe'
    
    P →  'con' | 'di' | 'per'
    V →  'cammina' | 'nuota' | 'corre' | 'esce' | 'cerca' | 'mangia' | 'salta' | 'dipinge' | 'vola' | 'cresce'
    
    Conj →  'e' | 'per' | 'ma' | 'o'
    Punct →  '.' | '!'

To ensure this model can be input into an LL(1) parser or pushdown automaton (PDA) , it must only create one tree. If it creates more than one, then it has ambiguity and is not eligible to be input into either method. 

For information about installing NLTK when importing does not work directly, head over to the implementation section. This library will be used to generate the trees.

The test sentence used that includes a preposition to test ambiguity is the following:
il bambino cerca il gatto di la bambina (the boy is looking for the girl's cat).

<img width="636" height="647" alt="generalGrammarTree" src="https://github.com/user-attachments/assets/24459aba-6a76-4031-8944-c1af90ef4aae" />
<br>
Notice how 2 trees are printed.

### Model without ambiguity
For the purposes of this project, eliminating ambiguity will simplify the productions in order to implement a PDA or LL(1).

In this situation, the VP production allows for multiple results since we are considering conjunctions and prepositions. Additionally, VP and NP productions are both simultaneously fighting for PP production, meaning there are other paths an input can take. I will be adding intermediate non-terminal productions in order to fix this issue.
    
    NPC → NP | NPC PP | NP Conj NPC | Conj VP
    NP →  NPF | NPM
    NPM →  DetM NM
    NPF →  DetF NF

Notice there is the addition of the NPC production that takes the possibility of adding a preposition or conjunction after a noun. It can also lead directly to NP, which will either identify a masculine or feminine noun.

    S → NPC VP Punct | VP Punct | NPC Punct

In order to account for this change, the S production gets the NP modified to NPC since it will lead to that level instead of straight to NP.
    
    VP →  V | VP NPC | V PP
    PP →  P NPC

Additionally, VP and PP productions get NP edited to NPC. VP PP has become V PP in order to directly flow into V and not recall VP. 

<img width="610" height="384" alt="unambiguousGrammarTree" src="https://github.com/user-attachments/assets/6158db67-7883-40e1-8169-3666eb92ae2d" />
<br>
Using the same sentence, the program only creates one tree now.

### Model without left recursion 
Now that only one tree is being produced, it still continues to expand both from the right and the left. Therefore, we must eliminate left recursion in order to be input into a pushdown automata. 
    
    NPC → NP | NP PP | NP Conj NPC | Conj VP

In the NPC production I have removed all loops that could occur on the left side. NPC can still recall itself as seen in NP Conj NPC, but it no longer recalls itself on the left side.
    
    VP →  V | V NPC | V PP

Similarly, in the VP production, it is no longer able to recall itself, as it goes directly to V. 

<img width="594" height="386" alt="finalGrammarTree" src="https://github.com/user-attachments/assets/eb3774c5-e158-402d-9f84-23effb67cbc8" />
<br>
With the same sentence as the previous two programs, this final grammar produces one tree and has no left side recursion.


### Final model

The final unambiguous without LMD model is the following:

    S → NPC VP Punct | VP Punct | NPC Punct

    NPC →  NP | NP PP | NP Conj NPC | Conj VP
    NP →  NPF | NPM
    NPM →  DetM NM
    NPF →  DetF NF
    
    VP →  V | V NPC | V PP
    PP →  P NPC
    
    DetM →  'il' | 'lo' | 'un'
    DetF →  'la' | 'una'
    
    NM →  'bambino' | 'gatto' | 'treno' | 'cavallo' | 'pennello' | 'fiore' | 'coniglio'
    NF →  'bambina' | 'anatra' | 'bicicletta' | 'farfalla' | 'volpe'
    
    P →  'con' | 'di' | 'per'
    V →  'cammina' | 'nuota' | 'corre' | 'esce' | 'cerca' | 'mangia' | 'salta' | 'dipinge' | 'vola' | 'cresce'
    
    Conj →  'e' | 'per' | 'ma' | 'o'
    Punct →  '.' | '!'
    
## Implementation
The tool used to validate strings that are accepted into the final grammar will be the Natural Language Toolkit (NLTK) in python. It is important to have NLTK installed in order to run the program. 

In the case the user does not have it installed, the user must run the command ```pip install NLTK``` in their terminal. Afterward, they must include the following lines in their code right after the import NLTK line:
```
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

These lines are only to be run <b>once</b>. Afterward, the lines can be deleted or commented (as shown in the test file). The tool will run just fine.

Once NLTK has been installed, the finalGrammar.py file includes the program that can run the validation of a string. In the file, there is a test string that is shown to be valid with the grammar presented.

## Tests
### Python tests 
The grammarTests.py file includes various tests of strings. This is to further demonstrate the implementation of the grammar and the different strings it can take. Very important note that there is a space between the final word and the punctuation so that the parser is able to identify the punctuation as a separate “word.”
Within the file are the following tests:

<b> Accepted strings:</b>
<ul>
<li>il bambino cerca il gatto di la bambina  . </li>
<li>il bambino cerca e corre . </li>
<li>la bambina e il bambino . </li>
<li>la bambina cerca il gatto e il fiore di il bambino . </li>
<li>il fiore di la bambina ! </li>
<li> la bambina e la volpe . </li>
<li>  la volpe o il gatto . </li>
<li>  il cavallo corre o salta ! </li>
<li>  la farfalla vola . </li>
 <li> la bicicletta di il bambino . </li>
<li>  il coniglio di il treno . </li>
<li>  la volpe con il coniglio !</li>
<li>  la volpe dipinge con il pennello . </li>
<li>  la bambina corre con il cavallo ! </li>
</ul>
<br>
<b>Unaccepted strings:</b>
#not accepted due to mismatch in gender
<ul>
<li> la gatto corre . </li>
<li> la bambino mangia e salta . </li>
<li> la farfalla e il volpe ! </li>
</ul>
<br>
#not accepted due to missing DetM or DetF
<ul>
<li> bambino cerca il gatto . </li>
<li> farfalla vola ! </li>
<li> treno esce !</li>
</ul>
<br>
#not accepted due to missing NP or VP
<ul>
<li> la gatto corre con il !</li>
<li> la volpe cerca il . </li>
</ul>

The program will print out the trees for all the accepted sentences and print out a list at the end of all the strings that were not accepted.

### Pushdown Automata 
In addition to the python automated NLTK test, I will be implementing a pushdown automata (PDA) to further prove this is a context-free grammar. As will be explained further on, a PDA is the tool that accepts a CFG. A PDA works well in this scenario considering it has further use of memory by using a stack since symbols will be pushed down into the stack, allowing them to be read later on and not discarded once moving on (Sipser, 2006, pp. 99–115).  Once the symbol is matched with the string, it is pushed out until we reach the end of an empty stack.

For the sake of keeping a simpler diagram, I will be using the example “il gatto corre .” (the cat runs). I first began constructing the sequence to get an idea of what the diagram would follow:

```
$, Z0/ $

S, $/ S

Punct VP NPC, S / NPC
NP, NPC/NP
NPM, NP/NPM
NM DetM, NPM/DetM

il, DetM/NM

gatto, NM/VP

V, VP/V
corre, V/ Punct

., Punct/ $

Z0, $/ Z0
```

These are all state transitions that follow the structure:
```
Input, Top of stack / new top of stack
```
Where Z0 represents an empty stack and $ represents the start of a stack. For example, <b>Punct VP NPC, S / NPC </b> means that Punct VP NPC will be pushed into the stack when the top of the stack is S, where the new top is now NPC.

Once I was able to establish the flow of the state transitions, I was able to create the diagram to visualize the state transitions:

<img width="1105" height="601" alt="PDA_diagram" src="https://github.com/user-attachments/assets/665c7315-1797-42e0-8b67-256c5b0dd4bb" />
<br>

Further showing the visualization is the following tree:

<img width="829" height="503" alt="PDA_tree" src="https://github.com/user-attachments/assets/95cdeedb-b088-4aa6-9372-7131eb1a6985" />
<br>

## Analysis
We can analyze the generated grammar using the Chomsky hierarchy. This concept is built on 4 levels (Type 0, 1, 2, 3) where Type 0 is recognized by a Turing machine and Type 3 is typically the most restricted grammar. 

<img width="624" height="434" alt="chomsky_hierarchy" src="https://github.com/user-attachments/assets/f2f26e96-49cc-4b78-a850-56c4427a0472" />


Figure: Chomsky Hierarchy (Prepbytes, 2023) 

In brief, each type is a level in the hierarchy and has its own name, as well as the restrictions and tools that can be implemented at each level. 

<b>Unrestricted (Type 0):</b> Unrestricted and typically encompassing all computational languages and accepted by a Turing machine. <br>
<b>Context sensitive (Type 1):</b> Take into account context of symbols and accepted by a linear-bound automata. Common to represent linguistic constructs. <br>
<b>Context free (Type 2):</b> Typically a mix of terminal and nonterminal sequences accepted by a pushdown automata. Common in syntax analysis. <br>
<b>Regular (Type 3):</b> Typically regular grammar that is accepted by a finite automata. Common in lexical analysis. 

As we move up in the hierarchy, the level and therefore grammar tends to become more powerful but simultaneously more complex

### General grammar model
With the creation of the original, general grammar model, we can conclude that it is a regular grammar (type 3). Since there is ambiguity, there are two trees generated, also seen as sharing a “forward set” (Hunter, 2020) with another string precisely because there is more than one path for a string. In fact, the lack of restrictions and broad scope of the grammar is what causes this to happen, leading to the least complex grammar that is type 3. 

### Unambiguous model
In the second grammar model generated, ambiguity has been eliminated which means there are some other restrictions and expansions. Despite this, I will continue to classify this as a Regular Grammar (type 3). While there have been modifications in the model, it is still not eligible to be input into a pushdown automata, meaning it has not yet reached the next level of the hierarchy. Since it cannot go directly to context-sensitive grammar level, not to mention the model does not yet handle all the context when it comes to certain words such as determinants that can change according to the rules of the Italian language, the model therefore continues to stay in the lowest level of the hierarchy. Luckily, it continues to follow the same ideas previously established for why it starts as a regular grammar. 

### Final model
Reaching the final grammar model, this model implies the lack of ambiguity and is based on an LMD model, meaning there is no left-side recursion. Therefore, it can be considered a Type 2 level grammar. As stated in the name of the level, it is a context-free grammar, which is what this project was based on creating. Additionally, type 2 in the Chomsky hierarchy works with a Pushdown Automata, the tool I have used to validate my grammar and the destination we were working towards. There is also a “mixture of terminal and nonterminal symbols” (Hunter, 2020)  in the model, further classifying it as a type 2 level grammar. 


## References
Hunter, T. (2020, February). The Chomsky Hierarchy. Retrieved from https://timhunter.humspace.ucla.edu/papers/blackwell-chomsky-hierarchy.pdf
<br>

Kumar, S., Kumar, J., Dubey, S. S., & Pathak, V. N. (2025). Theory of Automata and Its Applications in Science and Engineering (pp. 35–43). Deep Science Publishing.
<br>

Peyronel, S., & Higgins, I. (2006). BASIC ITALIAN: A GRAMMAR AND WORKBOOK. Routledge. Retrieved from Routledge website: https://ia600605.us.archive.org/17/items/BasicItalian/Basic%20Italian.pdf
<br>

Prepbytes. (2023, August 30). Chomsky Hierarchy in Theory of Computation. Retrieved April 19, 2026, from PrepBytes Blog website: https://prepbytes.com/blog/chomsky-hierarchy-in-theory-of-computation/
<br>

Sipser, M. (2006). Introduction to the Theory of Computation, Second Edition (pp. 99–115). Massachusetts: Thomson Course Technology.
<br>

Sterling, L., & Ehud Shapiro. (1997). The art of prolog : advanced programming techniques (pp. 382–387). Cambridge, Massachusetts: The Mit Press.

