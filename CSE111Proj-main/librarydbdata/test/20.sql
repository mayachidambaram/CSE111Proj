delete from Files WHERE
f_filekey = 7;

update Files set f_filekey = f_filekey - 1
where f_filekey > 7;

--once the file with the filekey 7 is deleted, the files below it have their filekeys altered so they start at filekey 7 not filekey 8
