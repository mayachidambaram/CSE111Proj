Select f_title as title, strftime('%Y-%m',f_publicationYear) as date
From Files
Where strftime('%Y',f_publicationYear) >= '2017' and strftime('%Y',f_publicationYear) <= '2018'
Group By strftime('%Y-%m',f_publicationYear)
