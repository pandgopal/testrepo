fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('File cannot be found')
    quit()

counts = dict()
words = list()

#put the word and word count in the dictionary
for line in fh:
    words = line.rstrip().split()
    if 'From'in words:
        hours = words[5].split(':')
        counts[hours[0]] = counts.get(hours[0],0)+1

#create empty list for tuples
lst = list()

#put key/val pair in tuples and append it to list
for key, val in counts.items():
    newtup = (key,val)
    lst.append(newtup)

#sort the list of tuples
lst = sorted(lst,reverse=False)

#print the tuples in  list
for key, val in lst :
    print(key, val)