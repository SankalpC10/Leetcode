class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap ={}
        for i in s1.split():
            hashmap[i] = hashmap.get(i,0)+1
        for j in s2.split():
            hashmap[j] = hashmap.get(j,0)+1
        return [i for i in hashmap if hashmap[i]==1]
