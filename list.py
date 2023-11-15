'''l1=[2,4,-6,-8,9,7]
l2=[]
for i in l1:
    if i>0:
        l2.append(i)
print(f"possitive list={l2}")'''


        
word=input("enter the word:")
listvowel=[i for i in word if i in 'aeiouAEIOU']
print(f"vowels={listvowel}")

