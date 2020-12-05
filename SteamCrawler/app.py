from collections import deque
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import datetime

class GameReviewManager:
    def __init__(self, appId):
        self.appId = appId
        self.rootUrl = 'https://steamcommunity.com/app/{}'.format(appId)
        self.reviewUrl = self.rootUrl + '/homecontent/'
        self.currentPage = 1
        self.set_game_name()

    def set_game_name(self):
        req = requests.get(self.rootUrl)
        soup = BeautifulSoup(req.text, 'html.parser')
        self.game_name = soup.select_one('div.apphub_AppName').text

    def get_next_reviews(self):
        payload = {
            'userreviewsoffset': str(10*(1-self.currentPage)),
            'p': str(self.currentPage),
            'workshopitemspage': str(self.currentPage),
            'readytouseitemspage': str(self.currentPage),
            'mtxitemspage': str(self.currentPage),
            'itemspage': str(self.currentPage),
            'screenshotspage': str(self.currentPage),
            'videospage': str(self.currentPage),
            'artpage': str(self.currentPage),
            'allguidepage': str(self.currentPage),
            'webguidepage': str(self.currentPage),
            'integratedguidepage': str(self.currentPage),
            'discussionspage': str(self.currentPage),
            'numperpage': '10',
            'browsefilter': 'toprated',
            'browsefilter': 'toprated',
            'appid': str(self.appId),
            'appHubSubSection': '10',
            'l': 'english',
            'filterLanguage': 'default',
            'searchText': '',
            'forceanon': '1',
        }

        req = requests.get(self.reviewUrl, params=payload)
        soup = BeautifulSoup(req.text, 'html.parser')

        reviewCards = soup.select('#page{} > div'.format(self.currentPage))
        reviews = []

        for reviewCard in reviewCards:
            review = {}
            review['game_name'] = self.game_name
            review['profile_url'] = reviewCard.select_one('div.apphub_CardContentAuthorBlock.tall > div.apphub_friend_block_container > a')['href']
            review['user_name'] = review['profile_url'].split('/')[-2]
            review['rating'] = reviewCard.select_one('div.apphub_CardContentMain > div.apphub_UserReviewCardContent > div.vote_header > div.reviewInfo > div.title').text
            review['hrs on record'] = float(reviewCard.select_one('div.apphub_CardContentMain > div.apphub_UserReviewCardContent > div.vote_header > div.reviewInfo > div.hours').text.replace(',', '').split(' ')[0])
            review['content'] = reviewCard.select_one('div.apphub_CardContentMain > div.apphub_UserReviewCardContent > div.apphub_CardTextContent').text
            reviews.append(review)

        self.currentPage += 1

        return reviews

game_queue = deque([{'appId': 292030, 'review_count': 409666}]) #우리가 넣을 것

start = time.time()
while game_queue:
    game = game_queue.popleft()
    gR = GameReviewManager(game['appId'])
    print(gR.game_name)
    batch = []
    progress = 0
    for i in range(game['review_count']//10):#한번에 열개씩 받아오니까
        reviews = gR.get_next_reviews()
        print('{:.2f}%'.format(100*progress/game['review_count']), 'Time reamaining {:30s}'.format(str(datetime.timedelta(seconds=game['review_count']/(progress/(time.time()-start)) if progress >0 else 0))),  end="\r")
        if reviews:
            batch += reviews
            progress += len(reviews)
            if len(batch) >= 100: #100 열에 한번씩 파일 쓰기
                pd.DataFrame(batch).to_csv('{}.csv'.format(re.sub(r'\W+', '', gR.game_name)), mode='a', header=False)
                batch[:] = []

end = time.time()
print(end - start)
    
    