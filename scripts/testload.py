from recengine.RecEngine import RecEngine
import pickle
f = open("pickled.dat")
re = pickle.load(f)
#re.build()
#s = re.__items
print dir(re)
s = re.items()
for item in s:

    print "ITEM: " + item
    similar = re.find_similar(item)
    print "similar are:"
    for sim in similar:
        print sim[0]
    print "----"
        