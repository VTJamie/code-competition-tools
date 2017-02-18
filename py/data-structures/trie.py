import json

__word__ = "__word__"
__count__ = "__count__"

class Trie:
    def __init__(self):
        self.rootnode = {}

    def addWord(self, word):

        return self.addWordInternal(word.lower(), self.rootnode, 0)
    def addWordInternal(self, word, curnode, curidx):
        if len(word) == curidx:
            curnode[__word__] = True
        else:
            if word[curidx] not in curnode:
                curnode[word[curidx]] = {}
                curnode[word[curidx]][__count__] = 0
            curnode[word[curidx]][__count__] += 1
            self.addWordInternal(word, curnode[word[curidx]], curidx+1)    
    
    def getAllWords(self):
        return self.getAllWordsInternal(self, self.rootnode, '')
    def getAllWordsInternal(self, curnode, prefix):
        retlist = []
        if __word__ in curnode:
            retlist.append(prefix)
        for c in curnode.keys():
            if c != __count__ and c != __word__:
                retlist += self.getAllWordsInternal(curnode[c], ''.join([prefix, c]))

        return retlist
    def getWordCount(self):
        return self.getWordCountInternal(self.rootnode)
    def getWordCountInternal(self, curnode):
        return curnode[__count__]
    def countWordsThatStartWith(self, prefix):
        return self.countPhoneWordsStartingWith(*prefix)

    def countPhoneWordsStartingWith(self, *prefixList):
        return self.countPhoneWordsStartingWithInternal(self.rootnode, prefixList, 0)
    def countPhoneWordsStartingWithInternal(self, curnode, prefixList, curidx):        
        if len(prefixList) == curidx:
            return self.getWordCountInternal(curnode)
        else:
            total = 0
            for c in prefixList[curidx]:
                if c in curnode:
                    total += self.countPhoneWordsStartingWithInternal(curnode[c], prefixList, curidx+1)

            return total

    def phoneWordsStartingWith(self, *prefixList):        
        return self.phoneWordsStartingWithInternal(self.rootnode, prefixList, 0, '')
    def phoneWordsStartingWithInternal(self, curnode, prefixList, curidx, prefix):
        retlist = []
        
        if curidx < len(prefixList):
            cword = prefixList[curidx].lower()            
            for c in cword:                                
                curprefix = ''.join([prefix, c])                
                if c in curnode:                    
                    retlist += self.phoneWordsStartingWithInternal(curnode[c], prefixList, curidx+1, curprefix)                     
        else:
            retlist += self.getAllWordsInternal(curnode, prefix)
        return retlist
    def debug(self):
        print(json.dumps(self.rootnode, indent=2))        

if __name__ == "__main__":
    t = Trie()
    t.addWord("Add")
    t.addWord("Adder")
    t.addWord("Addicted")
    t.addWord("additive")
    t.addWord("adidas")
    t.addWord("Blue")
    print(t.phoneWordsStartingWith('A'))
    print(t.countPhoneWordsStartingWith('a'))
    print(t.getWordCount())
    #t.debug()