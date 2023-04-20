# printing starting with a character
num=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
s=[]
for i in num:
    a=i.startswith('a')
    if a==True:
        s.append(i)
print(s)

#Write a Python program to check whether all dictionaries in a list are empty or not.

Sample= [{},{1,2},{3,4}]
for i in Sample:
    if i=={}:
        print('True')
    else:
        print('false')  

#2nd solution
my_list = [{},{},{}]
my_list1 = [{1:2},{},{}]
print(all(not d for d in my_list))


#3rd problem:

def flatten(Original):
    lst=[]
    for i in Original:
        if type(i) is list:
            for item in i:
                lst.append(item)
        else:
            lst.append(i)
    return lst
nested_list=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print(flatten(nested_list))

#remove duplicate from list
lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
s=[]
for i in lst:
    if i not in s:
        s.append(i)
print(s)

print(set(lst))

a=list(dict.fromkeys(lst))
print(a)
        
dicr={0: 10, 1: 20} 
for key,value in dicr.items():
    print(key,value)
dicr.update({"2":5})
print(dicr)
