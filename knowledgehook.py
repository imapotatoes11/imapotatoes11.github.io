import requests as r
from datetime import datetime
noww=datetime.now(tz=None)
#datetime.strftime(format=noww)
print(noww)
print(type(noww))
def send_payload(loop):
    payload1={
        "access-control-allow-credentials":"true",
        "access-control-allow-origin":"https://app.knowledgehook.com",
        "content-length":"2164",
        "content-type":"application/json; charset=utf-8",
        "date":"Fri, 05 Nov 2021 18:04:14 GMT",
        "server":"Microsoft-IIS/10.0",
        "strict-transport-securiy":"max-age=31536000; includeSubDomains; preload",
        "x-powered-by":"ASP.NET"
    }
    payload2={
        ":authority":"core.knowledgehook.com",
        ":method":"POST",
        ":path":"/student/Gift/4e927425-d70f-eb11-974c-005068c42b6/GiftBack",
        ":scheme":"https",
        "accept":"application/json, text/plain, */*",
        "accept-encoding":"gzip, deflate, br",
        "accept-language":"en-US,en;q=0.9",
        "authorization":"Bearer fwsP_jgE5yYafRmt0NR12L33o4rZy1GRevF8BOG4CXueaLZ1tw4bbsNEFYzrwvY5WJSzHCbxDIMqyQv8RwkR_xxbG4Zlm5t35QPC7qg0etK_XgVcMAUqxgKXXbDDRLAllgGckpkIu6PkFOT5ArSekhiv_GdsCVRKdbqPR175kDyp_IVn5b3p5znW1xw7bHq5tB3KypEEGYpIhcR60NoD9M9vRKEHk2QX3y3MdIlS0mgVr8ERf7FzvWd8hRwz8nkhSLOB-toxdCGFevXgydRTKnrtK6VQgwVr8Eq0mhM0Rj0YQ1SUzmXq9A8Mj2AG_F0AiQFN-Hbh-xGfl-wKFFw9XCnWRdqi6M2ev_V-ZNNJFT1DjVJ3GTOGkkb01E4x-VMrLSQquV3rYQvRj-VSw3iEyRBPAUyOj9M_zEHEGRPJ5Io",
        "client":"Web",
        "content-length":"0",
        "origin":"https://app.knowledgehook.com",
        "referer":"https://app.knowledgehook.com/",
        "sec-ch-ua":r'"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"Windows",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-site",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    for i in range(loop):
        #https://core.knowledgehook.com/Student/Gift/4e927425-d70f-eb11-974c-0050568c42b6/GiftBack
        r.post(r"https://core.knowledgehook.com/Student/Gift/4e927425-d70f-eb11-974c-0050568c42b6/GiftBack",data=payload1)
        print(r.Response())
        r.post(r"https://core.knowledgehook.com/Student/Gift/4e927425-d70f-eb11-974c-0050568c42b6/GiftBack", data=payload2)
import threading
x = threading.Thread(target=send_payload, args=(1000,))
y = threading.Thread(target=send_payload, args=(1000,))
z = threading.Thread(target=send_payload, args=(1000,))
a=threading.Thread(target=send_payload,args=(1000,))
b=threading.Thread(target=send_payload,args=(1000,))
c=threading.Thread(target=send_payload,args=(1000,))

x.start()
y.start()
z.start()
a.start()
b.start()
c.start()

x.join()
y.join()
z.join()
a.join()
b.join()
c.join()

