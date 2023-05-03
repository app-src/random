import requests,threading
url = 'https://camo.githubusercontent.com/11c1169c761c0c8afd87228f6089ec2b4ef0ba38d59bb5498fc92323ceb4b7c5/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6170702d737263266c6162656c3d76697369746f7273253230'

threads=1000

def run():
    for i in range(1000):
        result = requests.get(url)

for i in range(threads):
    th = threading.Thread(target=run).start()
    run()
    
print("Done")
