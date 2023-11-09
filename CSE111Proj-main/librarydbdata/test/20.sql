delete from Files WHERE
f_filekey = 7;

update Files set f_filekey = f_filekey - 1
where f_filekey > 7;
