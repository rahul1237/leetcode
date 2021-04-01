A=6
B=9

def gc(a,b):
    if(b==0):
        return a
    else:
        return gc(b,a%b)

print(gc(6,9))