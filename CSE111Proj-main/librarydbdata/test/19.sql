UPDATE Files
SET f_filekey = 13
WHERE f_filekey IS NULL;
--previously, we added a file. But the system does not automatically give it a filekey so we have to change the NULL filekey to filekey 13
