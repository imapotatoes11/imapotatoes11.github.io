t=input()
s=input()
found=False
for i in range(len(s)):
    s0=s[i:]+s[:i]
    if s0 in t:
        found=True
        break
if found:
    print("yes")
else:
    print("no")