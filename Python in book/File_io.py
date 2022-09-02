fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith('From:'):
        print(line)
    if line.startswith('Subject:'):
        print(line)

#Letting the user choose the file name
print("---")
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print("Can not find","'",fname,"'","in your folder")
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
