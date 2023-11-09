SELECT S.s_subjectname as Subject, count(F.f_filekey) as booknuminsubj
FROM Files F, Subjects S, ManySubjects M
Where F.f_filekey = M.f_filekey and S.s_subjectkey = M.s_subjectkey
Group By S.s_subjectname
