from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class InstaBot:
    def __init__(self,username,pw):
        self.username = username
        self.password = pw

        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(1)
        #username and password, submit
        self.driver.find_element("xpath", "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element("xpath", "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(pw)
        self.driver.find_element("xpath", "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
        sleep(4)
        #not now
        self.driver.find_element("xpath", "/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(1)
        #not now
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
        sleep(1)

        
        
        

    def get_unfollowers(self):
        #click profile
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a").click()
        
        #followings
        sleep(2)
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a/div").click()
        
        following = self.get_followings()
        #print("\nPeople I follow:\n" + str(following))

        #Followers
        sleep(1)
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
        

        followers = self.get_followers()
        #print("\nPeople that follow me:\n" + str(followers))

        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        
        # Calls function to write to file
        #self.write_file(not_following_back)


    def get_followings(self):
        sleep(1)
        #select scroll box 
        scroll_box = self.driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")

        last_ht = 0
        ht = 1
        #loop to scroll
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '']
        
        #close box
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button").click()

        return names

    def get_followers(self):
        sleep(1)
        #select scroll box 
        scroll_box = self.driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")

        last_ht = 0
        ht = 1
        #loop to scroll
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '']
        

        #close box
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button").click()

        return names

    # Function to write unfollowers to a file
    #def write_file(self, unfollowers):
        #with open("unfollowers", "w+") as f:
            #for line in unfollowers:
                #f.write('%s\n' %line)  

        #print("written")
        #f.close
        #print("closed")

# Enter username and password as arguments
myBot = InstaBot("username","password")

myBot.get_unfollowers()

