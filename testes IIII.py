import time,threading
import statistics as st
listes=[]
def do(name,delay,loop):
    print(f"{name} running")
    time.sleep(delay)
    for i in range(loop):
        print(f"{name} at {i}")

class dodo:
    def __init__(self):
        global listes
    def DODO(self,thread_name,how_many):
        start=time.time()
        self.result=threading.Thread(target=do, args=(thread_name, 0, how_many))
        self.resulte = threading.Thread(target=do, args=(thread_name, 0, how_many))
        self.resultes = threading.Thread(target=do, args=(thread_name, 0, how_many))
        self.result.start()
        self.resulte.start()
        self.resultes.start()
        self.result.join()
        self.resulte.join()
        self.resultes.join()
        end=time.time()
        print(str(round(end-start,3))+" seconds elapsed")
        resul=str(round(end-start,3))
        listes.append(round(end-start,3))
        with open("testes IIII_results.txt","a") as e:
            e.write(f'\n{resul} secs    Name: {thread_name}    Threads: {how_many}')

'''
if __name__=="__main__":
    _1=threading.Thread(target=do,args=("1",0,50,))
    _2=threading.Thread(target=do,args=('2',0,50,))
    _3=threading.Thread(target=do,args=('3',0,50,))

    _1.start()
    _2.start()
    _3.start()

    _1.join()
    _2.join()
    _3.join()'''
d=dodo()
for i in range(1000000):
    d.DODO("1",10000)
print("Mean length: "+str(st.mean(listes)))
print("Median length: "+str(st.median(listes)))
print("Mode length: "+str(st.mode(listes)))