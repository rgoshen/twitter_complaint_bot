from selenium import webdriver


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
        pass

    def tweet_at_provider(self):
        """
        Method to send tweet to Twitter.
        """
        pass
