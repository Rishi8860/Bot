from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Edge(executable_path=r"C:\Users\rishi\Desktop\Data science\Web scrapping\webdriver\msedgedriver.exe")
class instabot:
    def __init__(self):
        self.post=0
        self.followers=0
    def __Login(self,Username,Password):
        username=driver.find_element(By.NAME,'username')
        password=driver.find_element(By.NAME,'password')
        username.send_keys(Username)
        password.send_keys(Password)
        btn=driver.find_elements(By.TAG_NAME,'button')
        for i in btn:
            if i.get_attribute('type') == 'submit':
                login=i
                break
        login.click()
        num=len(driver.find_elements(By.ID,'slfErrorAlert'))
        return driver
    def login(self):
        website=driver.get('https://www.instagram.com') 
        driver.find_element(By.NAME,'username').send_keys(Keys.CONTROL + "a")
        driver.find_element(By.NAME,'username').send_keys(Keys.DELETE)
        driver.find_element(By.NAME,'password').send_keys(Keys.CONTROL + "a")
        driver.find_element(By.NAME,'password').send_keys(Keys.DELETE)
        a=input('Username: ')
        b=input('password: ')
        c=self.__Login(a,b)
        time.sleep(7)
        if(driver.current_url=='https://www.instagram.com/'):
            err=input('Wrong ID or Password: Do you want to try again Y(Yes) or N(No) : ')
            err=err.lower()
            if err=='y' or err=='yes':
                ans=login()
                return ans
            else:
                return 0
        else:
            return 1
    def SearchPerson(self,Name):
        driver.get(f'https://www.instagram.com/{Name}/')
    def BasicInfo(self,Name):
        driver.get(f'https://www.instagram.com/{Name}/')
        data=driver.find_elements(By.CLASS_NAME,'g47SY ')
        temp=['Posts','Followers','Following']
        #a=driver.find_element(By.CSS_SELECTOR,'[class="_7UhW9   xLCgt      MMzan   KV-D4           uL8Hv        T0kll "]')
        Data={}
        for i in range(len(data)):
            Data[temp[i]]=int(data[i].get_attribute('innerHTML'))
        #Data['Bio']=''.join(a.get_attribute('innerHTML').split('<br>'))
        self.post=Data['Posts']
        return Data
    def images(self,name):
        k=self.BasicInfo(name)
        temp=driver.current_url
        driver.get(temp)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(120)
        a=driver.find_elements(By.CSS_SELECTOR,'[class="v1Nh3 kIKUG _bz0w"]')
        b=[]
        c=[]
        k=[]
        print(len(a))
        Data={}
        for i in a:
            b.append(i.find_element(By.TAG_NAME,'a').get_attribute('href'))
            c.append(i.find_element(By.CLASS_NAME,'KL4Bh').find_element(By.TAG_NAME,'img').get_attribute('alt'))
        for i in b:
            driver.get(i)
            k.append(int(driver.find_elements(By.CSS_SELECTOR,'[class="_7UhW9   xLCgt        qyrsm KV-D4               fDxYl    T0kll "]')[1].find_element(By.TAG_NAME,'span').get_attribute('innerHTML'))+1)
        Data['Images']=b
        Data['Captions']=c
        Data['Likes']=k
        driver.get(temp)
        return Data
    def signout(self):
        btn=driver.find_element(By.CLASS_NAME,'EforU')
        btn.click()
        time.sleep(2)
        sign=driver.find_elements(By.CLASS_NAME,'-qQT3')
        sign[-1].click()
        return 1