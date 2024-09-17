class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap ={}
        for i in s1.split():
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for j in s2.split():
            if j not in hashmap:
                hashmap[j]=1
            else:
                hashmap[j]+=1
        return [i for i in hashmap if hashmap[i]==1]
