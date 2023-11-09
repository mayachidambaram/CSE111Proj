SELECT count(*) as num, u_firstname as firstname, u_lastname as lastname, u_username as username
FROM BorrowedBooks, Student, User
WHERE u_firstname = 'Michael' and u_lastname = 'Brown' and u_userkey = s_studentkey and s_studentkey = b_student_id
--find number of books of books student Michael Brown borrowed
