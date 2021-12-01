test=open("test.txt","r")
values=[]
for i in test.readlines():
    print(i)
    values.append(i)
test.close()
print(values)
test=None
test=open("test.txt","a")
test.write("\nseofiesdf")
test.close

test=open("ind.html","w")
test.write("<p>Hello!</p>")
for jj in range(5):
    test.write("\n<div> </div>")
test.write("\n<p>e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e </p>")
test.write("\n<form action=\"https://google.ca\">")
test.write("\n<input type=\"submit\" value=\"eeeee\" />")
test.write("\n</form>")
test.close()