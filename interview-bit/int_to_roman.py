A=30
t=['','M','MM','MMM']
h=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
te=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
s=['','I','II','III','IV','V','VI','VII','VIII','IX']

print(t[A//1000]+h[(A%1000)//100]+te[(A%100)//10]+s[A%10])