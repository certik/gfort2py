import sys
import numpy as np


def clean_list(l, idx):
	return [i for j, i in enumerate(l) if j not in idx]
	
def output(filename, *args):
    with open(filename, 'wb') as f:
        for i in args:
            pickle.dump(i, f, protocol=2)

def fpyname(filename):
    return filename.split('.')[0] + '.fpy'
	
#def split_brackets(value, remove_b=True):
    #'''
    #Split a string based on pairs of brackets, nested brackets are not split

    #Input:
        #'abc (def) (fgh () ())'

    #Outputs:
        #['abc (def')', '(fgh () ())']
    #'''
    #if remove_b:
        #if value.startswith('('):
            #value = value[1:]
        #if value.endswith(')'):
            #value = value[:-1]
    
    #res = []
    #start = False
    #count = 0
    #j = 0
    #for idx,i in enumerate(value):
        #if i == '(':
            #count = count + 1
            #start = True
        #if i == ')':
            #count = count - 1
        #if start:
            #if count == 0:
                #res.append(value[j:idx+1])
                #j=idx+1
                #start = False

    #return res

def hextofloat(s):
    # Given hex like parameter '0.12decde@9' returns 5065465344.0
    man, exp =s.split('@')
    exp=int(exp)
    decimal = man.index('.')
    man = man[decimal+1:]
    man = man.ljust(exp,'0')
    man = man[:exp]+'.'+man[exp:]
    man = man +'P0'
    return float.fromhex(man)
    
#def split_brackets(value, remove_b=False):
    #'''
    #Split a string based on pairs of brackets, nested brackets are not split

    #Input:
        #'abc (def) (fgh () ())'

    #Outputs:
        #['def', 'fgh () ()']
    #'''
    #if value.startswith('('):
        #value = value[1:]
    
    #if value.endswith(')'):
        #value = value[:-1]
    
    #res = []
    #token = ''
    #start = False
    #count = 0
    #for i in value:
        #if i == '(':
            #count = count + 1
            #start = True
        #if start:
            #token += i
        #if i == ')':
            #count = count - 1
        #if start and count == 0:
            #if remove_b:
                #res.append(token[1:-1])
            #else:
                #res.append(token)
            #start = False
            #token = ''
    #return res
