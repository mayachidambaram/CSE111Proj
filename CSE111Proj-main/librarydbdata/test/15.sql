SELECT DISTINCT F.f_title, F.f_author, BB.b_borrow_date
FROM BorrowedBooks AS BB
JOIN Files AS F ON BB.b_book_id = F.f_filekey
WHERE BB.b_borrow_date = '2023-11-09';
-- Displays files that have been borrowed at a specific date
