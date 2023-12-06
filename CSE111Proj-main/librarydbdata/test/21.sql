SELECT DISTINCT SUBSTR(f_author, INSTR(f_author, ' ') + 1) AS author_last_name
FROM Files;

-- same thing as 9.sql but with last names
