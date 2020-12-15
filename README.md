# _Game Recommendation System using Collaborative Filtering with KNN_

## 2020-2 CAU BigData(#50648) Team Project

팀명 : _Big Cram_  
팀원 : 민준홍(팀장) 김경현 이수호 정영진 이혜성

## Dataset - _Steam Review_

- Steam game review 데이터를 직접 크롤링하여 사용
- [Google Drive]()

## Environment

- nltk
- scikit-learn
- pandas
- http-server

## Resources

- [**_Crawler_**](https://github.com/ddamddi/bigdata/tree/main/Crawler)
  - `steam-review-crawler.py` - Code to fetch reviews as html format from Steam
  - `steam-review-extractor.py` - Parse the Steam review files in html format and save them in csv format
  - `sentiments.ipynb` - Get comment sentiments using nltk library
- **_Recommender_**
  - `attempt_1_KNN_all_reviews.ipynb` - [???]
  - `attempt_2_KNN_with_sentiment_all_reviews.ipynb` - [???]
  - `attempt_3_KNN_with_sentiment_reviews_gt_1.ipynb` - [???]
  - `unused_KNN_reviews_gt_1.ipynb` - [???]
  - `user-based_knn_with_sentiment.ipynb` - User-based CF with KNN using comment sentiment
- [**_Visualization_**](https://github.com/ddamddi/bigdata/tree/main/Visualization)
  - `KNN_with_sentiment_add_visul1.ipynb` - Bubble chart generation code created by modifying Matplotlib unreleased code
  - `KNN_with_sentiment_add_visul2.ipynb` - Force-directed Graph Using D3.js to Visualize Recommended Results

## References

- [aesuli's Steam-Crawler](https://github.com/aesuli/steam-crawler)
- [Matplotlib Packed-bubble chart](https://matplotlib.org/devdocs/gallery/misc/packed_bubbles.html)
- [D3.js v4 Force Directed Graph with Labels](https://bl.ocks.org/heybignick/3faf257bbbbc7743bb72310d03b86ee8)
