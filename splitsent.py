s=input("enter the sentence:")
print(s)
wordlist=s.split()
print(wordlist)
for i in wordlist:
    print(f"{i}occuars{wordlist.count(i)}time")
