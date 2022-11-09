import os 


files = './MusicDictionary.csv'

f = open(files, 'r')
data = f.read()
f.close()
lst1 = data.split(',')
print(lst1)

os.chdir('data')
for file in lst1:
    os.makedirs(file, exist_ok=True)
    
os.chdir('..')
