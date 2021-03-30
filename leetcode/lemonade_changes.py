class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=[]
        t=[]
        ans=[]
        for _ in range(len(bills)):
            if(bills[_] == 5):
                f.append(bills[_])
            elif(bills[_] == 10):
                t.append(bills[_])
                if(len(f)==0):
                    ans.append(False)
                else:
                    f.pop()
            else:
                if(10 not in t):
                    if(len(f)<3):
                        ans.append(False)
                    else:
                        f.pop()
                        f.pop()
                        f.pop()
                elif(len(f)<1):
                    ans.append(False)
                else:
                    f.pop()
                    t.pop()

            if(bills[0]!=5):
                return False
                exit()

        if(False in ans):
            return False
        else:
            return True
