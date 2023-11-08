SELECT f_title, f_author, f_publicationYear
FROM Files
JOIN ManySubjects ON Files.f_filekey = ManySubjects.f_filekey
JOIN Subjects ON ManySubjects.s_subjectkey = Subjects.s_subjectkey
WHERE Subjects.s_subjectname = 'Chemistry';
