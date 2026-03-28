# A/B Testing for ShoeFly.com

## Data Scientist: Analytics - Codecademy

Our favorite online shoe store, ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. Help them analyze the data using aggregate measures.

### Tasks

#### Analyzing Ad Sources

1. Examine the first few rows of <code>ad_clicks</code>.

2. Your manager wants to know which ad platform is getting you the most views.
How many views (i.e., rows of the table) came from each <code>utm_source</code>?

3. If the column <code>ad_click_timestamp</code> is not null, then someone actually clicked on the ad that was displayed.
Create a new column called <code>is_click</code>, which is <code>True</code> if <code>ad_click_timestamp</code> is not null and <code>False</code> otherwise.

4. We want to know the percent of people who clicked on ads from each <code>utm_source</code>.
Start by grouping by <code>utm_source</code> and <code>is_click</code> and counting the number of <code>user_id</code>‘s in each of those groups. Save your answer to the variable <code>clicks_by_source</code>.

5. Now let’s pivot the data so that the columns are <code>is_click</code> (either <code>True</code> or <code>False</code>), the index is <code>utm_source</code>, and the values are <code>user_id</code>.
Save your results to the variable <code>clicks_pivot</code>.

6. Create a new column in <code>clicks_pivot</code> called <code>percent_clicked</code> which is equal to the percent of users who clicked on the ad from each <code>utm_source</code>.
Was there a difference in click rates for each source?

#### Analyzing an A/B Test

7. The column <code>experimental_group</code> tells us whether the user was shown Ad A or Ad B.
Were approximately the same number of people shown both ads?

8. Using the column <code>is_click</code> that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.

9. The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.
Start by creating two DataFrames: <code>a_clicks</code> and <code>b_clicks</code>, which contain only the results for <code>A</code> group and <code>B</code> group, respectively.

10. For each group (<code>a_clicks</code> and <code>b_clicks</code>), calculate the percent of users who clicked on the ad by day.

11. Compare the results for <code>A</code> and <code>B</code>. What happened over the course of the week?
Do you recommend that your company use Ad A or Ad B?