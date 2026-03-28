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

# Task 7
ads_shown = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(ads_shown)

# Task 8
ads_clicked = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
ads_clicked_pivot = ads_clicked.pivot(
    columns='is_click',
    index='experimental_group',
    values='user_id'
).reset_index()

ads_clicked_pivot['percent_clicked'] = ads_clicked_pivot[True] / (ads_clicked_pivot[True] + ads_clicked_pivot[False])
print(ads_clicked_pivot)

# Task 9
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# Task 10
a_daily_clicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
a_daily_clicks_pivot = a_daily_clicks.pivot(
    columns='is_click',
    index='day',
    values='user_id'
).reset_index()

b_daily_clicks = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_daily_clicks_pivot = b_daily_clicks.pivot(
    columns='is_click',
    index='day',
    values='user_id'
).reset_index()

a_daily_clicks_pivot['percent_clicked'] = a_daily_clicks_pivot[True] / (a_daily_clicks_pivot[True] + a_daily_clicks_pivot[False])
b_daily_clicks_pivot['percent_clicked'] = b_daily_clicks_pivot[True] / (b_daily_clicks_pivot[True] + b_daily_clicks_pivot[False])
print(a_daily_clicks_pivot)
print(b_daily_clicks_pivot)