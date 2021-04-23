"""
Write a Python program to split a given dictionary of lists into list of dictionaries.
Input :
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
, {'Science': 89, 'Language': 78},
{'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}
]
Output :
[
{'Science': 88, 'Language': 77},{'Science': 89, 'Language': 78},
{'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}
]"""
######################
#Written by Ali Rahmani
######################
"""
ask= {
    'Science': [88, 89, 62, 95],'Language': [77, 78, 84, 80]
      }
keys , values= ask.keys() , ask.values()
val=[]
for k in keys:
    val.append(ask[k])
ans=dict()
for v in values:
    ans.update([zip(keys , v)])

print(ans)
"""
################
#Written by ahmadreza: https://github.com/ahmadrezare2?tab=repositories
################
def list_of_dicts(marks):
    keys = marks.keys()
    vals = zip(*[marks[k] for k in keys])
    result = [dict(zip(keys, v)) for v in vals]
    return result

marks = {'Science': [88, 89, 62, 95],
         'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)
print("\nSplit said dictionary of lists into list of dictionaries:")
print(list_of_dicts(marks))





