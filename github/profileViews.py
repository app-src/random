import requests,threading,time
import multiprocessing as mp
url = 'https://camo.githubusercontent.com/11c1169c761c0c8afd87228f6089ec2b4ef0ba38d59bb5498fc92323ceb4b7c5/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6170702d737263266c6162656c3d76697369746f7273253230'

# threads=20
# count=0
start = time.time()
# result = requests.get(url)
# print(result)
# print(time.time() -start)



# def run(th):
#     for i in range(10):
#         result = requests.get(url)
#         if time.time -start>=20:
#             th.join()
#         count+=1
#     print(count)

# for i in range(threads):
#     th = threading.Thread(target=run,args=[th]).start()
    
# print("Done")


def my_func(x):
    for i in range(x): 
        print(requests.get(url))

def main():
    pool = mp.Pool(mp.cpu_count())
    pool.map(my_func, range(0, 10))
    print(time.time() -start)
    
if __name__ == "__main__":

    main()