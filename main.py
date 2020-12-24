from internetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 400
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/home/rgoshen/Development/chromedriver"
TWITTER_EMAIL = "rick.goshen@gmail.com"
TWITTER_PW = "NitL10n$#1S"

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
