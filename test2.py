usernames = ["james", "jBlank", "JACK"]
queries = ["j", "jm", "jbl", "JB"]
class prefix(object):
    def __init__(self, words):
        self.index = [(w) for w in words ]
    def trie(self, prefix):
        list1 = []
        prefix = prefix.lower()
        for i in range(0,len(self.index)):
            found = self.index[i]
            if found.startswith(prefix):
                list1.append(found)
        if(len(list1) > 0):
            return list1
        else:
            return '-1'
names = prefix(usernames)
for q in queries:
    list = names.trie(q)
    #list = list[1:] + list[:1]
    print (' '.join(list))

