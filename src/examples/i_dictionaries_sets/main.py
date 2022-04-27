#main program
import dictionaries
import sets

print(sets.get_a_set())

myset = set('abc')

print(myset)

myset = set(['one', 'two', 'three'])
print(len(myset))

myset.add('four')
myset.add('five')
print(myset)

myset.update(['six', 'seven', 'eight'])
print(myset)
myset.update([1,2,3])

for e in myset:
    print(e)

if 'ninety' not in myset:
    print('not in the set')

myset.clear()
print(myset)

# bdaydictionary = {}

# dictionaries.add_friend('Joe', '10231995', bdaydictionary)
# dictionaries.add_friend('Mary', '01011990', bdaydictionary)
# dictionaries.add_friend('Jane', '01311980', bdaydictionary)

# print(bdaydictionary)

# dictionaries.update_friend('Joe', '10201995', bdaydictionary)

# print(bdaydictionary)

# dictionaries.del_friend('Joe', bdaydictionary)


#phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}

# print(phonebook['Katie'])

# phonebook['Katie'] = '555-4444'

# if 'katie' in phonebook:
#     print(phonebook['katie'])
# else:
#     print('katie is not a valid key')

# phonebook['Joe'] = '555-5555'

# print(phonebook)

# del phonebook['Katie']

# print(len(phonebook))

# mixed_up = {'abc':1, 999:'yada yada', (3, 6, 9):[3, 6, 9]}

# print(mixed_up[999])
# print(mixed_up[(3,6,9)])

# #loop over the keys
# for key in mixed_up:
#     print(key, mixed_up[key])

# print(phonebook.get('Chris'))

# for key, value in phonebook.items():
#     phonebook[key] = '555-9999'
#     print(key, value)

# print(phonebook)

# for key in phonebook.keys():
#     print(key)

# for v in phonebook.values():
#     print(v)    

# k,v =  phonebook.popitem()

# print(k, v)

# print(phonebook)