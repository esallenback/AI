import time
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : input('path to download: ')}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("chromedriver.exe",chrome_options=chromeOptions)  # Optional argument, if not specified will search path.
driver.get('https://www.opensubtitles.org/en/search/subs');
time.sleep(5) # Let the user actually see something!
file=open('links.txt','r')
links=file.read()
links=links.split('\n')
for x in links:
    driver.execute_script('window.location.replace("https://www.opensubtitles.org/en/subtitleserve/sub/{}")'.format(x))
    time.sleep(30)
    print(x)
time.sleep(10) # Let the user actually see something!
driver.quit()
