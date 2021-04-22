"""
[7:30 PM, 4/22/2021] Navid Filsaraee: yesterday, David and John went bank robbery and managed to steal bank's vault.
At home they want to know 📃 type of things in the vault.
help them do the job fast, so they don't get caught by police.
input:
( "gold", 1000, ("navid check", 3542),["neda watch",500],
{"sanad khone" :"felan ja"}, {"name" :"navid", "pass" :"qwerty 1234"} )
output:
{str : 1,dict:2,list:1,tuple:1,set:0,}
"""
x= ( "gold", 1000, ("navid check", 3542),["neda watch",500],{"sanad khone" :"felan ja"}, {"name" :"navid", "pass" :"qwerty 1234"} )
number,string,lists,tuples,sets,dicts=0,0,0,0,0,0
r=dict()
for i in x:
    #print(i)
    if type(i)== str :
        string += 1
        r.update(str=string)
    elif type(i)== dict :
        dicts+=1
        r.update(dicts=dicts)
    elif type(i)== list :
        lists+=1
        r.update(lists=lists)
    elif type(i)== set :
        sets+=1
        r.update(sets=sets)
    elif type(i)== tuple :
        tuples+=1
        r.update(tuples=tuples)
    elif type(i)== int :
        number+=1
        r.update(number=number)

print(string,dicts,lists,tuples,sets,number)
print(r)