"""
PLAN:
lower characters
replace l with a
replace m with b
replace s with c
SORTING:
new sorted variable(llmmss), og variable(lmlmss)
while og variable is not equal to sorted variable:
swap?
"""
inputt=input("")
inputt_lower=inputt.lower()
imputSorted=inputt_lower.replace("l","a")
imputSorted=imputSorted.replace("m","b")
imputSorted=imputSorted.replace("s","c")
inputSorted=imputSorted.sort()
while inputt_lower!=inputSorted:
    #swap