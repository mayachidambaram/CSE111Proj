select s.s_subjectname as sname
from Subjects s 
WHERE s.s_subjectkey = ( 
    select many.s_subjectkey
    from ManySubjects many
    where many.f_filekey IN (  
        select F.f_filekey
        from Files F
    )
    Group By many.s_subjectkey
    Order By count(many.f_filekey) desc 
    limit 1 
)
--finds most popular subject meaning the subject with the most books
