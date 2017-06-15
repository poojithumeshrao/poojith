import cPickle

f = open("opdataset.p","rb")
a = cPickle.load(f)
print a[0]
