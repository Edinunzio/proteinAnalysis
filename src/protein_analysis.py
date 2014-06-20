import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import itertools

def euclid_dist(x,y):
    # where do you intend to deploy this function?
    # what parameters are you trying to pass? what is x, and what is y?
    
    sumSq = 0.0 # what does this variable stand for? 

    for i in range(len(x)):  
        # is x supposed to represent AA_percents[key]?
        # if that is the case, you may need to reconsider 
        # the structure of this loop
        # however, I do not know what this is attempting to do.
        sumSq += (x[i] - y[i]) ** 2
        # sumSq now equals 0.0 + (x[i] - y[i]) to the power of 2
        # is that your intention?
    return(sqrt(sumSq)) # is this then taking the square root 
    #of the new value of sumSq that has just been raised to the power of 2?
    

df = pd.read_csv('dataset.csv', header = 0) 
# out of curiosity, what does df stand for?

AA_percents = {}


for row in df.index:
    key = df.ix[row, 'viral_protein_name'] + ' , ' + df.ix[row, 'virus_species']
    value = ProteinAnalysis(df.ix[row, 'viral_protein_AA_seq']).get_amino_acids_percent()
    
    # below are 2 sample values I logged just to see what is being passed
    # {'A': 0.06639004149377593, 'C': 0.0, 'E': 0.06224066390041494, 'D': 0.02074688796680498, 'G': 0.0912863070539419, 'F': 0.029045643153526972, 'I': 0.0912863070539419, 'H': 0.016597510373443983, 'K': 0.012448132780082987, 'M': 0.012448132780082987, 'L': 0.16182572614107885, 'N': 0.04979253112033195, 'Q': 0.06639004149377593, 'P': 0.024896265560165973, 'S': 0.1078838174273859, 'R': 0.024896265560165973, 'T': 0.07053941908713693, 'W': 0.016597510373443983, 'V': 0.06639004149377593, 'Y': 0.008298755186721992}
    # {'A': 0.04081632653061224, 'C': 0.0, 'E': 0.05102040816326531, 'D': 0.02040816326530612, 'G': 0.08673469387755102, 'F': 0.03571428571428571, 'I': 0.08163265306122448, 'H': 0.02040816326530612, 'K': 0.015306122448979591, 'M': 0.01020408163265306, 'L': 0.15816326530612246, 'N': 0.05612244897959184, 'Q': 0.08163265306122448, 'P': 0.030612244897959183, 'S': 0.11734693877551021, 'R': 0.030612244897959183, 'T': 0.05612244897959184, 'W': 0.02040816326530612, 'V': 0.07653061224489796, 'Y': 0.01020408163265306}
    
    AA_percents[key] = pd.DataFrame.from_dict(value, orient='index')
    
# see included my_comb.txt, AA_percents_key.txt and AA_percents.txt to see what this is
my_comb = []

for item in itertools.combinations(AA_percents, 2):

    my_comb.append(item)

#     print my_comb
# would you mind going over the next few lines and explain what it is doing?
for x in my_comb:
    for y in x:
        print y

# when executing this via unix based command line, I found it easier to 
# output this to a text file. that is how I created the included text files.
# in a terminal do something like:
# python protein_analysis.py > my_comb2.txt
# this may take awhile, but in the same folder as your python script is located, 
# will be an automatically created text file containing the output of the script.
# please feel free to comment on here, github, or in email if you have any questions.

