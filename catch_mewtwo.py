from selenium import webdriver
import time
import win32api

hasCaught = False

browser = webdriver.Chrome("path_to_your_webdriver") #eg -> C:\Program Files (x86)\Google\Chrome\chromedriver.exe
browser.implicitly_wait(10)

def pba_login():
    browser.get("https://www.pokemonbattlearena.net/")
    browser.find_element_by_id("txtUsername").send_keys("your_username") #Enter your username here
    browser.find_element_by_id("txtPassword").send_keys("your_password") #Enter your password here
    browser.find_element_by_id("btnLogin").click()

def home_page():
    home = browser.find_element_by_link_text("The Hollow Field") #Map that you want to open
    home.click()

def reaching_start():
    north = browser.find_element_by_xpath("//table/tbody/tr/td/table/tbody/tr[1]/td[2]")
    west = browser.find_element_by_xpath("//table/tbody/tr/td/table/tbody/tr[2]/td[1]")
    east = browser.find_element_by_xpath("//table/tbody/tr/td/table/tbody/tr[2]/td[3]")
    south = browser.find_element_by_id("south")


    time.sleep(5)
    south.click()

    time.sleep(2)
    south.click()

    time.sleep(2)
    south.click()

    time.sleep(2)
    west.click()

    time.sleep(2)
    west.click()
    
    time.sleep(2)
    west.click()

def nail_that_fucker():
    '''
    north = browser.find_element_by_xpath("//table/tbody/tr/td/table/tbody/tr[1]/td[2]")
    west = browser.find_element_by_xpath("//table/tbody/tr/td/table/tbody/tr[2]/td[1]")
    east = browser.find_element_by_xpath("//table/tbody/tr/td/table/tbody/tr[2]/td[3]")
    south = browser.find_element_by_id("south")'''
    
    for i in range(23):
        east = browser.find_element_by_xpath("//table/tbody/tr/td/table/tbody/tr[2]/td[3]")

        time.sleep(2)
        east.click()

        time.sleep(2)
        text = browser.find_element_by_id("battleframetext").text
        t = text.split()

        print(t[5])

        if t[5] == "Mewtwo" or t[5] == "Mew":
            hasCaught = True
            return hasCaught

    for i in range(23):
        west = browser.find_element_by_xpath("//table/tbody/tr/td/table/tbody/tr[2]/td[1]")

        time.sleep(2)
        west.click()

        time.sleep(2)
        text = browser.find_element_by_id("battleframetext").text
        t = text.split()
        
        if t[5] == "Mewtwo" or t[5] == "Mew":
            hasCaught = True
            return hasCaught
    
    return False


#to pass authentication
pba_login()

#to select the map
home_page()

#moving to a comfortable position to help us in the long run
reaching_start()

#infinite loop to be executed till Mewtwo is found
while hasCaught == False:
    hasCaught = nail_that_fucker()

#if found, an alert box pops up
if hasCaught == True:
    win32api.MessageBox(0, 'Pokemon Caught', 'PBA', 0x00001000)