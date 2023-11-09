select distinct User.u_firstname, User.u_lastname
from AddedBooks
join 
    User ON
    AddedBooks.a_librarian_id = User.u_userkey
join 
    Subjects ON
    AddedBooks.a_subjectkey = Subjects.s_subjectkey
join 
    Publisher ON 
    AddedBooks.a_publisherkey = Publisher.p_publisherkey
join 
    Files ON
    AddedBooks.a_book_id = Files.f_filekey
--finds names of librarians who added books
