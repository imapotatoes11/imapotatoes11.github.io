"""

!!!MUST READ!!!
YOU NEED TO HAVE ALL UNNECESSARY APPS CLOSED (GOOGLE CHROME) TO ALLOW THE PROGRAM TO HAVE ENOUGH RAM. IF THE FOR LOOP IN
THE "open_tab()" FUNCTION IS 500, YOU NEED 8GB OF RAM AND IT WILL OPEN 2000 TABS. EXERCISE CAUTION WHEN RUNNING
USE TASK MANAGER TO KILL BROWSER
IF TASK MANAGER BROKE, RESTART TASK MANAGER TO KILL BROWSER

"""
import time
import webbrowser
import threading
def open_tab(name,amount):
    print(f"{name} running")
    time.sleep(amount)
    for i in range(500):#500
        webbrowser.open_new(r"https://www.google.com/search?q=aa&rlz=1C1CHBF_enCA970CA970&oq=e&aqs=chrome..69i57j35i39j69i60j69i61j69i60l3j69i65.588j0j7&sourceid=chrome&ie=UTF-8")
        print(str(i)+name)
        time.sleep(0)
        print("LINE SEPARATOR")

if __name__=="__main__":
    one=threading.Thread(target=open_tab,args=("one",0,))
    two=threading.Thread(target=open_tab,args=("two",0,))
    thre=threading.Thread(target=open_tab,args=("thre",0,))
    four=threading.Thread(target=open_tab,args=("four",0,))
    #five=threading.Thread(target=open_tab,args=("Five",0,))

    one.start()
    two.start()
    thre.start()
    four.start()
    #five.start()

    one.join()
    two.join()
    thre.join()
    four.join()
    #five.join()
    print("done")