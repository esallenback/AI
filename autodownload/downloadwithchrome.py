import time
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : input('path to download: ')}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("chromedriver.exe",chrome_options=chromeOptions)  # Optional argument, if not specified will search path.
driver.get('https://www.opensubtitles.org/en/search/subs');
time.sleep(5) # Let the user actually see something!
startatf=open('downloadat.txt','+r')
startat=startatf.read()
startatf.close()
if startat == '':
    startat=0
else:
    startat=int(startat)
file=open('links.txt','r')
links=file.read()
links=links.split('\n')
for x in links[0+startat:(startat+10)]:
    driver.execute_script('window.location.replace("https://www.opensubtitles.org/en/subtitleserve/sub/{}")'.format(x))
    time.sleep(3)
    print(x)
time.sleep(10) # Let the user actually see something!
driver.quit()
file.close()
file=open('downloadat.txt','+w')
file.write(str(startat+10))
file.close()
