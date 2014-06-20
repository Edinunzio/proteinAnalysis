import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import itertools

def euclid_dist(x,y):
    # where do you intend to deploy this function?
    # what parameters are you trying to pass? what is x, and what is y?
    
    sumSq = 0.0 # what does this variable stand for? 

    for i in range(len(x)):  
        sumSq += (x[i] - y[i]) ** 2
    return(sqrt(sumSq)) 
    

df = pd.read_csv('dataset.csv', header = 0) 

AA_percents = {}


for row in df.index:
    key = df.ix[row, 'viral_protein_name'] + ' , ' + df.ix[row, 'virus_species']
    value = ProteinAnalysis(df.ix[row, 'viral_protein_AA_seq']).get_amino_acids_percent()
    AA_percents[key] = pd.DataFrame.from_dict(value, orient='index')
    
my_comb = []

for item in itertools.combinations(AA_percents, 2):

    my_comb.append(item)

print 'my_comb BEGINS***********************'
print my_comb[0][0]
print my_comb[0][1]

print my_comb[1][0]
print my_comb[1][1]
print 'my_comb ENDS***********************'

for x,y in my_comb:
    print '***********************'
    print 'x datatype: '+ str(type(x))
    print 'x: ' + x
    print 'y datatype: '+ str(type(y))
    print 'y: ' + y
    print '***********************'

#for x in my_comb:
    #for y in x:
        #print y

