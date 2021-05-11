# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
n = ((10 ** 2) / 100) + (34 * 3) - 2.75
print(n)

# 5) Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
word = 'hello'
print(word[1])

# 6) Reverse the string 'hello' using slicing:
print(word[::-1])

# 7) Given the string hello, give two methods of producing the letter 'o' using indexing.
print(f'Método 1: {word[4]}')
print(f'Método 2: {word[-1]}')

# 8) Build this list [0,0,0] two separate ways.
method1 = [0] * 3
method2 = [row[0] for row in [[0, 1], [0, 2], [0, 3]]] # ou met = [0, 0, 0]
print(f'{method1} \n{method2}')

# 9) Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# 10) Sort the list below:
list4 = [5,3,4,6,1]
new_list = sorted(list4)
print(new_list)

# 11) Using keys and indexing, grab the 'hello' from the following dictionaries:
d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d4['k1'][2]['k2'][1]['tough'][2][0])

# 13)
tupla = tuple()
print(type(tupla))

# 14) Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

