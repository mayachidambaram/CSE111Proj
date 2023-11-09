SELECT Files.f_title, Files.f_author, Files.f_publicationYear, BorrowedBooks.b_borrow_date, User.u_username
FROM Files
JOIN ManySubjects ON Files.f_filekey = ManySubjects.f_filekey
JOIN Subjects ON ManySubjects.s_subjectkey = Subjects.s_subjectkey
JOIN BorrowedBooks ON Files.f_filekey = BorrowedBooks.b_book_id
JOIN Student ON BorrowedBooks.b_student_id = Student.s_studentkey
JOIN User ON Student.s_studentkey = User.u_userkey
WHERE Subjects.s_subjectname = 'Computer Science';
