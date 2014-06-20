import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import itertools

def euclid_dist(x,y):
    sumSq = 0.0
    for i in range(len(x)):
        sumSq += (x[i] - y[i]) ** 2
    return(sqrt(sumSq))

df = pd.read_csv('dataset.csv', header = 0)
AA_percents = {}

for row in df.index:
    key = df.ix[row, 'viral_protein_name'] + ' , ' + df.ix[row, 'virus_species']
    value = ProteinAnalysis(df.ix[row, 'viral_protein_AA_seq']).get_amino_acids_percent()
    AA_percents[key] = pd.DataFrame.from_dict(value, orient='index')
jarielle = []
for item in itertools.combinations(AA_percents, 2):
     my_comb.append(item)
#     print my_comb
for x in my_comb:
    for y in x:
        print type(y)

