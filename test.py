codes={}

def function(str):
	dec={}
	for ch in str:
		dec[ch]=dec.get(ch,0)+1
	return dec
var="abcddeee"
dec1=function(var);
print var
print dec1


def funcSort(str):
	keys=str.keys()	
	touple=[]
	for ch in str:
		touple.append((str[ch],ch))
	touple.sort()
	return touple


touple1=funcSort(dec1)

print touple1


def buildTree(tuples) :
     while len(tuples) > 1 :
         leastTwo = (tuples[0:2])
	 theRest  = tuples[2:]                          # all the others
         combFreq = leastTwo[0][0] + leastTwo[1][0]     # the branch points freq
	 tuples   = theRest + [(combFreq,leastTwo)]     # add branch point to the end
	 print "---------------------->",theRest
	 print "Touple --->",tuples
         tuples.sort()                                  # sort it into place
	 print "Sorted----------------->",tuples
     return tuples[0]  

tree=buildTree(touple1)

print tree


def treeTrim(tree):
	p=tree[1]
	print "===============>p===========",p
	if type(p)==type(""):
		print type(p)
		return p
	else:
		return (treeTrim(p[0]),treeTrim(p[1]))
trimmedtree=treeTrim(tree)
print trimmedtree

def assignCode(node,pat=''):
	global codes
	if type(node)==type(""):
		codes[node]=pat
	else:
		assignCode(node[0],pat+"0")
		assignCode(node[1],pat+"1")
	return codes

codes1=assignCode(trimmedtree)
print codes1



def encode(str):
	global codes
	output=""
	for ch in str:
		output+=codes[ch]
	return output

def decode(tree,str):
	output=""
	p=tree
	for bit in tree:
		if bit=='0':
			p=p[0]
		else:
			p=p[1]
		if type(p)==type(" "):
			output+=p
			p=tree
	return output


encrypted=encode(var)
print encrypted
decrypted=decode(trimmedtree,str)
print decrypted

	
