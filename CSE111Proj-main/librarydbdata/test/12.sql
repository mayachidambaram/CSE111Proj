Select f_title as title, strftime('%Y-%m',f_publicationyear) as date
From Files
Where strftime('%Y',f_publicationyear) >= '2017' and strftime('%Y',f_publicationyear) <= '2018'
Group By strftime('%Y-%m',f_publicationyear) #revised for date range between 2017 and 2018 and edited the files dates to be year-month-day
