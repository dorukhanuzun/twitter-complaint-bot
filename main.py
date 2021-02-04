from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 200
PROMISED_UP = 16
CHROME_DRIVER_PATH = "/Users/dorukhanuzun/chrome-driver/chromedriver"
TWITTER_EMAIL = "YOUR EMAIL HERE"
TWITTER_PASS = "YOUR PASSWORD HERE"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                      '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                    'div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(1)
        username = self.driver.find_element_by_name("session[username_or_email]")
        username.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        tweet_button_main = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/'
                                                       'div[1]/div[''3]/a')
        tweet_button_main.click()
        input_text = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div'
                                                       '/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div'
                                                       '/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweet = f"Hey @FidoSolutions, why is my internet speed {self.down}down/{self.up}up when I pay for " \
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
        input_text.send_keys(tweet)
        sending_tweet = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                          '/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div'
                                                          '[4]/div/div/div[2]/div[4]')
        sending_tweet.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
