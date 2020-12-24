from selenium import webdriver
import time


class InternetSpeedTwitterBot():
    """
    Class to setup the bot.
    """

    def __init__(self, driver_path):
        """
        InternetSpeedTwitterBot constructor.
        """
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """
        Method to get internet speed from site.
        """
        self.driver.get("https://www.speedtest.net/")

        time.sleep(60)
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        """
        Method to send tweet to Twitter.
        """
        pass
