class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=list(set(jewels))
        ans=[]
        for _ in c:
            ans.append(stones.count(_))
        return sum(ans)