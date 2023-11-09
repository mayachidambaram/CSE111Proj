select f_title as title, f_author as author
from files
where f_filekey = (
    select a_book_id
    from AddedBooks
    where a_addition_date = ( 
        select max(strftime('%Y-%m-%d',a_addition_date))
        from AddedBooks
    )
    LIMIT 1
)
