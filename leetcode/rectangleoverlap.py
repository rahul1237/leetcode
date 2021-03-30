class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1=rec1[0],rec1[1]
        x2,y2=rec1[2],rec1[3]
        x3,y3=rec2[0],rec2[1]
        x4,y4=rec2[2],rec2[3]

        x5,y5=max(x1,x3),max(y1,y3)
        x6,y6=min(x2,x4),min(y2,y4)

        nx1,ny1=x6,y5


        l=((x5-nx1)**2+(y5-ny1)**2)**(0.5)
        b=((x6-nx1)**2+(y6-ny1)**2)**(0.5)


        ans=l*b


        if(x5>x6 or y5>y6):
            ans=0

        if(ans > 0):
            return True
        else:
            return False