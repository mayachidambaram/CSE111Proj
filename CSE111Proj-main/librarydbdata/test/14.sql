select u_firstname, u_lastname
from User
where u_userkey IN (
    select s_studentkey
    from Student
    where s_studentkey IN (
        select b_student_id
        from BorrowedBooks
        where b_status = 'D'
        group by b_student_id
    )
)
group by u_firstname
