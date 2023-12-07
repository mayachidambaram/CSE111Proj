/* select s.s_subjectname as sname
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
) */

SELECT s.s_subjectname AS sname
FROM Subjects s
JOIN (
    SELECT s_subjectkey, COUNT(DISTINCT f_filekey) AS file_count
    FROM ManySubjects
    GROUP BY s_subjectkey
    ORDER BY file_count DESC
    LIMIT 1
) AS maxFileCount ON s.s_subjectkey = maxFileCount.s_subjectkey;

--finds most popular subject meaning the subject with the most books
