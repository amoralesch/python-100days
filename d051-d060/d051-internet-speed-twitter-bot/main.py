# Speed Tester And Twitter Reporter

# Create a bot to monitor my internet speed, and twit when the speed is
# less than promised
#
# Another project taken from the curse, because of the hassle to create
# fake Twitter accounts, this one is copied from the example.

from InternetSpeedTwitterBot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
