import csv
import pandas as pd

reader = csv.DictReader(open("Test_Data.csv"))
a = [raw for raw in reader]
c = [ b['A'] for b in a if b['Class'] == 'A' ]
d = [ b['B'] for b in a if b['Class'] == 'A' ]
e = [ b['C'] for b in a if b['Class'] == 'A' ]
f = [ b['G'] for b in a if b['Class'] == 'A' ]
g = [ b['R'] for b in a if b['Class'] == 'A' ]
h = [ b['X6'] for b in a if b['Class'] == 'A' ]
i = [ b['X8'] for b in a if b['Class'] == 'A' ]
        
dict = {'A': c, 'B': d, 'C': e, 'G': f, 'R': g, 'X6': h, 'X8' :i}      
df = pd.DataFrame(dict)         
df.to_csv('ClassA.csv') 

l1 = [ b['A'] for b in a if b['Class'] == 'B' ]
l2 = [ b['B'] for b in a if b['Class'] == 'B' ]
l3 = [ b['C'] for b in a if b['Class'] == 'B' ]
l4 = [ b['G'] for b in a if b['Class'] == 'B' ]
l5 = [ b['R'] for b in a if b['Class'] == 'B' ]
l6 = [ b['X6'] for b in a if b['Class'] == 'B' ]
l7 = [ b['X8'] for b in a if b['Class'] == 'B' ]
        
dict = {'A': l1, 'B': l2, 'C': l3, 'G': l4, 'R': l5, 'X6': l6, 'X8' :l7}      
df = pd.DataFrame(dict)         
df.to_csv('ClassB.csv')


l8 = [ b['A'] for b in a if b['Class'] == 'C' ]
l9 = [ b['B'] for b in a if b['Class'] == 'C' ]
l10 = [ b['C'] for b in a if b['Class'] == 'C' ]
l11 = [ b['G'] for b in a if b['Class'] == 'C' ]
l12 = [ b['R'] for b in a if b['Class'] == 'C' ]
l13 = [ b['X6'] for b in a if b['Class'] == 'C' ]
l14 = [ b['X8'] for b in a if b['Class'] == 'C' ]
        
dict = {'A': l8, 'B': l9, 'C': l10, 'G': l11, 'R': l12, 'X6': l13, 'X8' :l14}      
df = pd.DataFrame(dict)         
df.to_csv('ClassC.csv')



l15 = [ b['A'] for b in a if b['Class'] == 'D' ]
l16 = [ b['B'] for b in a if b['Class'] == 'D' ]
l17 = [ b['C'] for b in a if b['Class'] == 'D' ]
l18 = [ b['G'] for b in a if b['Class'] == 'D' ]
l19 = [ b['R'] for b in a if b['Class'] == 'D' ]
l20 = [ b['X6'] for b in a if b['Class'] == 'D' ]
l21 = [ b['X8'] for b in a if b['Class'] == 'D' ]
        
dict = {'A': l15, 'B': l16, 'C': l17, 'G': l18, 'R': l19, 'X6': l20, 'X8' :l21}      
df = pd.DataFrame(dict)         
df.to_csv('ClassD.csv')


l22 = [ b['A'] for b in a if b['Class'] == 'E' ]
l23 = [ b['B'] for b in a if b['Class'] == 'E' ]
l24 = [ b['C'] for b in a if b['Class'] == 'E' ]
l25 = [ b['G'] for b in a if b['Class'] == 'E' ]
l26 = [ b['R'] for b in a if b['Class'] == 'E' ]
l27 = [ b['X6'] for b in a if b['Class'] == 'E' ]
l28 = [ b['X8'] for b in a if b['Class'] == 'E' ]
        
dict = {'A': l22, 'B': l23, 'C': l24, 'G': l25, 'R': l26, 'X6': l27, 'X8' :l28}      
df = pd.DataFrame(dict)         
df.to_csv('ClassE.csv')



l29 = [ b['A'] for b in a if b['Class'] == 'F' ]
l30 = [ b['B'] for b in a if b['Class'] == 'F' ]
l31 = [ b['C'] for b in a if b['Class'] == 'F' ]
l32 = [ b['G'] for b in a if b['Class'] == 'F' ]
l33 = [ b['R'] for b in a if b['Class'] == 'F' ]
l34 = [ b['X6'] for b in a if b['Class'] == 'F' ]
l35 = [ b['X8'] for b in a if b['Class'] == 'F' ]
        
dict = {'A': l29, 'B': l30, 'C': l31, 'G': l32, 'R': l33, 'X6': l34, 'X8' :l35}      
df = pd.DataFrame(dict)         
df.to_csv('ClassF.csv')




