# By Alexandros Panagiotakopoulos - alexandrospanag.github.io

# *is a container of single items - **is a a keyword of pair
def func(*args, **keywords):
	for a in args:print(a)
	for k,v in keywords.items():print(k,v)

func(1,2,3, x=10, y=20)
