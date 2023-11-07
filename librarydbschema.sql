CREATE TABLE Files (
    f_filekey INT PRIMARY KEY,
    f_title VARCHAR(255),
    f_author VARCHAR(100),
    f_publicationYear INT
    FOREIGN KEY (f_publisherkey) REFERENCES Publisher(p_publisherkey),
    FOREIGN KEY (f_subjectkey) REFERENCES Subjects(s_subjectkey)
    
);

CREATE TABLE User (
    u_userkey INT PRIMARY KEY,
    u_username VARCHAR(50),
    u_pass_word VARCHAR(50),
    u_firstname VARCHAR(50),
    u_lastname VARCHAR(100),
    u_email VARCHAR(100),
    u_phonenum INT
);

CREATE TABLE Student(
    s_studentkey INT PRIMARY KEY,
    s_yearofgrad INT,
    s_idnumber INT
);

CREATE TABLE Librarian(
    l_librariankey INT PRIMARY KEY,
    l_idnumber INT
);

CREATE TABLE ManySubjects (
    PRIMARY KEY (f_filekey, s_subjectkey),
    FOREIGN KEY (f_filekey) REFERENCES Files(f_filekey),
    FOREIGN KEY (s_subjectkey) REFERENCES Subjects(s_subjectkey)
);

CREATE TABLE Publisher(
    p_publisherkey INT PRIMARY KEY,
    p_publishername VARCHAR(100),
    p_licensingagreement INT  
);

CREATE TABLE Subjects(
    s_subjectkey INT PRIMARY KEY,
    s_description VARCHAR(255),
    s_subjectname VARCHAR(255)
);