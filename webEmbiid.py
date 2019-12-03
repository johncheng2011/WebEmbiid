import tweepy
import keys #import keys and tokens
import datetime
import pytz
import requests
from bs4 import BeautifulSoup
from pyshorteners import Shortener 
def mainFun(event,context):
    tweetEmbiid()
    tweetReport()


def tweetReport():

    my_date = datetime.datetime.now(pytz.timezone('US/Eastern'))
    url = "https://ak-static.cms.nba.com/referee/injury/Injury-Report_"
    url += my_date.strftime("%Y-%m-%d") + "_01PM.pdf"
    if(requests.get(url)):
        auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        api = tweepy.API(auth)
        url_shortener = Shortener('Bitly', bitly_token = keys.ACCESS_TOKEN) 
        api.update_status("NBA Injury Report for "+my_date.strftime("%m/%d/%Y")+" "+url_shortener.short(url)+" #NBA")
    else:
        print("Couldn't get Injury Report")
    

def tweetEmbiid():
    result = requests.get('https://www.fantasybasketballnerd.com/service/injuries/')
    soup = BeautifulSoup(result.content,"html.parser")
    team = soup.find('team',attrs={'code': "PHI"})
    players = team.find_all('player')
    for player in players:
        #make this part better
        if(player.find('name').text == 'Joel Embiid'):
            auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
            auth.set_access_token(keys.access_token, keys.access_token_secret)
            api = tweepy.API(auth)
            api.update_status(player.find('name').text+" ("+player.find('injury').text+") "+player.find('notes').text+ " #JoelEmbiid")
            return
        if(player.find('name').text == 'Anthony Davis'):
            auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
            auth.set_access_token(keys.access_token, keys.access_token_secret)
            api = tweepy.API(auth)
            api.update_status(player.find('name').text+" ("+player.find('injury').text+") "+player.find('notes').text+ " #AnthonyDayToDavis")
            return