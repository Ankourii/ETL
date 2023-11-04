# ETL
## Extract-Transform-Load

Project Duration: 3 Days 

This project consists in extracting information from 3 different sources, transforming it and loading it in a database. 

![ETL](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.informatica.com%2Fresources%2Farticles%2Fwhat-is-etl.html&psig=AOvVaw0tzzWQCEGy-dOgOa_k498r&ust=1699195514799000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMiLxdrKqoIDFQAAAAAdAAAAABAE)


For this project I decided to create a data-base with the number of births per day (in the U.S from 1994-2003), the public holidays and lunar phases for those days. I thought it would be interesting to see 

a) how many children are born on public holidays 

and 

b) which lunar phase is the most popular for births


![baby](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.healthline.com%2Fhealth%2Fpregnancy%2Fwater-birth&psig=AOvVaw0AqtzvTgQD0_X-c-nvxt1N&ust=1699195895192000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCIiGhJDMqoIDFQAAAAAdAAAAABAE)


**Sources:** 

[U.S births per day 1994-2003](https://www.kaggle.com/datasets/tunguz/us-births)
[Moon calendar](https://mooncalendar.astro-seek.com)
[U.S public holidays](https://date.nager.at/PublicHoliday/United-States) 


**Step 1**: I downloaded the data for the births 
**Step 2**: I downloaded the data for the public holidays from 1994 to 2003
**Step 3**: I found a moon calendar online
**Step 4**: I extracted the data from the moon calendar with web scraping using Selenium. You can see the process in notebooks/Extracting
**Step 5**: I transformed all of the data. Cleaned it and added it all together in one database. You can see the process in notebooks/Transforming
**Step 6**: I loaded the data in a data-base called "etl_project" in mySQL in a table "called births". You can see the process in notebooks/Loading


