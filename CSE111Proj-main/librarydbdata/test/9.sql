SELECT DISTINCT SUBSTR(f_author, 1, INSTR(f_author, ' ') - 1) AS author_first_name
FROM Files;
--find author's first names that are unique so no repeats even if the author have different last names
