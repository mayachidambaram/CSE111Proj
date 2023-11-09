select f_filekey as filekey, f_title as title
from Files
where f_filekey NOT IN (
    select b_book_id
    from BorrowedBooks
)
--find books that have never been borrowed
