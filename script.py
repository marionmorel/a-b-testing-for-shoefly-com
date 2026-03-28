import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# Task 1
print(ad_clicks.head(10))

# Task 2
views_by_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views_by_source)

# Task 3
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

# Task 4
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

# Task 5
clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id'
).reset_index()

# Task 6
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) 
print(clicks_pivot)