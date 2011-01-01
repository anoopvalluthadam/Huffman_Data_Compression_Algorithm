codes={}

def frequency(str):
	freq={}
	for ch in str:
		freq[ch]=freq.get(ch,0)+1
	return freq

var="abcddeee"
dic=frequency(var)
print var
print dic


def funcSort(dic):
	letters=dic.keys()
	tuples=[]
	for let in dic:
		tuples.append((dic[let],let))
	tuples.sort()
	return tuples

sorted=funcSort(dic)

print sorted


def treeMaking(tuples):
	while len(tuples) > 1:
		leastTwo = (tuples[0:2])
		theRest = tuples[2:]
		compFreq = leastTwo[0][0] + leastTwo[1][0]
		tuples = theRest + [(compFreq,leastTwo)]
		print "-----------",tuples
		tuples.sort()
	return tuples[0]

tree=treeMaking(sorted)
print tree

def treeTrim(tree):
	p=tree[1]
	print p
	if type(p)==type(""):
		return p
	else:
		return (treeTrim(p[0]),treeTrim(p[1]))
	
trimmed=treeTrim(tree)
print trimmed


def assignCodes(node,pat=''):
	global codes
	print "Assign Code----------->",node
	if type(node)==type(""):
		print "------------if----",node,"--pat---",pat
		codes[node]=pat
	else:
		assignCodes(node[0],pat+"0")
		print"-----------else------------",pat
		assignCodes(node[1],pat+"1")
assignCodes(trimmed)
print codes



def encode(str):
	global codes
	output=""
	for ch in str:
		output+=codes[ch]
	return output
simple=encode(var)
print simple	

def decode(tree,str):
	output=""
	p=tree
	for ch in str:
		if ch =='0':
			p=p[0]
		else:
			p=p[1]
		if type(p)==type(""):
			output+=p
			p=tree
			#print output
	return output

original=decode(trimmed,simple)
print "-----------",original
