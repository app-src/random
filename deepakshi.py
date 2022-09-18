import time
from selenium import webdriver
from bs4 import BeautifulSoup
  
# provide the url of the channel whose data you want to fetch
urls = [
    'https://www.youtube.com/c/GeeksforGeeksVideos/videos?view=0&sort=dd&shelf_id=0'
]
  
  
def main():
    times = 0
    driver = webdriver.Chrome()
    for url in urls:
        driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        while times < 50:
            time.sleep(1)   
            driver.execute_script(
                "window.scrollTo(0, document.documentElement.scrollHeight);")
            times += 1
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a', id='video-title')
        views = soup.findAll('span', class_='style-scope ytd-grid-video-renderer')
        duration = soup.findAll('span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer')
        print(len(titles))
        file = open('data.txt', 'w')
        for title, view, duration in zip(titles, views, duration):
            print(title.text, view.text, duration.text)
            file.write(title.text+" "+view.text+" "+duration.text)
        file.close()
        
        
main()