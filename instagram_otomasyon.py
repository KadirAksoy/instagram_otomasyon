from selenium import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.keys import*
import time


class Instagram_giris():                                    #fonksiyonlar içinde "self" ile kullanılır

    def __init__(self) :
        self.driver=webdriver.Chrome()                
        self.driver.get("https://www.instagram.com/")


    def login(self,user_name,password):
        self.user_name=user_name    
        self.password=password 
        
        time.sleep(2)
        us_nm=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")        #kullanıcı adı girer
        us_nm.send_keys(self.user_name)
        
        time.sleep(2)
        psw=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")           #şifreyi girer
        psw.send_keys(self.password)
        psw.send_keys(Keys.ENTER)



        

    def followers(self):
        time.sleep(3)
        self.profile=self.driver.get("https://www.instagram.com/"+self.user_name+"/")     #profile girdik 

        #time.sleep(3)
        #self.strnumber= self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text      #takipçi sayısına ulaştık
        #self.scrolling_range=int(self.strnumber)//5
        

        time.sleep(3)
        self.follewer=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()    #takipçiler listesine tıkladık


        #time.sleep(3)
        #self.action= webdriver.ActionChains(self.driver)                                                                  #scrollin özelliği
        #self.scrolling=self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/ul").click()       

        #time.sleep(3)  
        #for i in range(self.scrolling_range):                           #scrolling uzunlugu#
           #self.action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

        #self.file=open("takipçi_dosyası.txt","w")

        #for i in range(5):
        #with open ("takipçi_dosyası.txt","w") as dosya :
            #dosya.write()
        

    
        



    def followeds(self):
        time.sleep(3)
        self.profile=self.driver.get("https://www.instagram.com/"+self.user_name+"/")   #profile girdik

        time.sleep(3)
        self.strnumber=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text    #takip edilenler sayısına ulaştık
        self.scrolliing_range=int(self.strnumber)//5
        print(self.scrolliing_range)


        ##time.sleep(3)
        ##self.followed=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()  #takip edilenler listesine tıkladık

        ##time.sleep(3)                                                                                               #scrolling  özelliği
        ##self.action= webdriver.ActionChains(self.driver)
        ##self.scrolling=self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/ul").click()           

        ##time.sleep(3)
        ##for i in range(self.scrolling_range):                                    #scrolling uzunluğu
            ##self.action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()



        






a=Instagram_giris()
a.login("000000000","11111111")





