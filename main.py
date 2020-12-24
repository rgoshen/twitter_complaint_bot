from internetSpeedTwitterBot import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = "/home/rgoshen/Development/chromedriver"


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
