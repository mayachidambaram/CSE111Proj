SELECT DISTINCT SUBSTR(f_author, 1, INSTR(f_author, ' ') - 1) AS author_first_name
FROM Files;
