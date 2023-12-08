import sqlite3
from datetime import datetime

def openConnection(_dbFile):
    conn = None
    try :
        conn = sqlite3.connect(_dbFile)
        print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
        print("Welcome to the library database management system.")
        print('\n')
    except Error as e:
        print(e)
    return conn

def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)
    try :
        _conn.close()
        print("success")
    except Error as e:
        print(e)


def Q1_1(_conn, letter):
    try:
        print('\n')
        output = open('output/1_1.out', 'w')
        header = "{}"
        output.write((header.format("Subject/s :")) + '\n')
        query1_1 = """ SELECT s_subjectname as subject 
                 FROM Subjects  
                 WHERE s_subjectname 
                 LIKE ?; """

        cursor = _conn.cursor()
        cursor.execute(query1_1, (f'{letter.upper()}%',))

        results = cursor.fetchall()

        temp = 0
        if not results:
            output.write("No subjects found starting with specified letter or you may have typed a symbol/number/multiple letters.\n")
            temp = temp + 1
        else:
            for row in results:
                output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/1_1.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
        return temp 

    except Error as e:
        print(e)

def Q1_2(_conn, s_name):
    try:
        print('\n')
        output = open('output/1_2.out', 'w')
        header = "{}|{}"
        output.write((header.format("Subject","Book Count :")) + '\n')
        query1_2 = """SELECT S.s_subjectname as Subject, count(F.f_filekey) as booknuminsubj
                    FROM Files F, Subjects S, ManySubjects M
                    Where F.f_filekey = M.f_filekey and S.s_subjectkey = M.s_subjectkey and S.s_subjectname = ?
                    Group By S.s_subjectname"""

        cursor = _conn.cursor()
        cursor.execute(query1_2, (s_name,))

        results = cursor.fetchall()

        temp = 0
        if not results:
            output.write("Unavailable. You may have misspelled or capitalized incorrectly.\n")
            temp = temp + 1
        else:
            for row in results:
                output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/1_2.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
        return temp
    except Error as e:
        print(e)

def Q2_1(_conn):
    try: 
        output = open('output/2_1.out', 'w')
        header = "{}"
        output.write((header.format("Publisher/s :")) + '\n')
        query2_1 = """SELECT p_publishername as publisher
                      FROM Publisher
                      Group By p_publishername"""

        cursor = _conn.cursor()
        cursor.execute(query2_1)

        results = cursor.fetchall()

        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/2_1.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
    except Error as e:
        print(e)  

def Q2_2(_conn, p_name):
    try:
        output = open('output/2_2.out', 'w')
        header = "{}|{}|{}"
        output.write((header.format("Filekey","Title", "Author")) + '\n')
        query2_2 = """ select F.f_filekey, F.f_title, F.f_author
                from Files F
                where F.f_publisherkey = (
                            select P.p_publisherkey 
                            From Publisher P
                            Where P.p_publishername = ?
                ) """

        cursor = _conn.cursor()
        cursor.execute(query2_2, (p_name,))

        results = cursor.fetchall()

        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/2_2.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
    except Error as e:
        print(e)

def Q3_1(_conn, num):
    try: 
        if num == 1:
            output = open('output/3_1.out', 'w')
            header = "{}|{}"
            output.write((header.format("Random Subject","Random Publisher")) + '\n')
            query3_1 = """ select 
                            (select s_subjectname 
                            from Subjects 
                            order by RANDOM() limit 1) as random_subject,
                            (select p_publishername 
                            from Publisher
                            order by RANDOM() limit 1) as random_publisher"""
        elif num == 2:
            output = open('output/3_1.out', 'w')
            header = "{}"
            output.write((header.format("Random Subject")) + '\n')
            query3_1 = """ select s_subjectname as random_subject
                           from Subjects 
                           order by RANDOM() 
                           limit 1"""

        elif num == 3:
            output = open('output/3_1.out', 'w')
            header = "{}"
            output.write((header.format("Random Publisher")) + '\n')
            query3_1 = """ select p_publishername 
                           from Publisher
                           order by RANDOM() 
                           limit 1"""

        cursor = _conn.cursor()
        cursor.execute(query3_1)

        results = cursor.fetchall()

        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/3_1.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
        return results

    except Error as e:
        print(e)
        return None

def Q3_2(_conn, year, s_name, p_name):
    try:
        output = open('output/3_2.out','w')
        header = "{}|{}|{}|{}"
        output.write((header.format("Title","Year","Subject","Publisher")) + '\n')
        query3_2 = """ select F.f_title, F.f_publicationYear, S.s_subjectname, P.p_publishername
                       from Files F
                       JOIN ManySubjects M on F.f_filekey = M.f_filekey  
                       JOIN Subjects S on S.s_subjectkey = M.s_subjectkey
                       JOIN Publisher P on F.f_publisherkey = P.p_publisherkey
                       where strftime('%Y',F.f_publicationYear) >= ? 
                       and S.s_subjectname = ? and P.p_publishername = ?"""

        cursor = _conn.cursor()
        cursor.execute(query3_2,(year, s_name, p_name))

        results = cursor.fetchall()

        temp = 0
        if not results:
            output.write("Unfortunately, the library has inadequate files.")
            temp = temp + 1
        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/3_2.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
        return temp
    except Error as e:
        print(e)

def Q4(_conn, first_name=None, last_name=None):
    try:
        print('\n')
        output = open('output/Q4.out', 'w')
        header = "{}|{}"
        output.write((header.format("Title", "Author")) + '\n')

        if first_name:
            query = """SELECT F.f_title, F.f_author
                       FROM Files F
                       WHERE SUBSTR(F.f_author, 1, INSTR(F.f_author, ' ') - 1) LIKE ?;"""
        elif last_name:
            query = """SELECT F.f_title, F.f_author
                       FROM Files F
                       WHERE SUBSTR(F.f_author, INSTR(F.f_author, ' ') + 1) LIKE ?;"""
        else:
            print("Invalid option. Please provide either first name or last name.")
            return

        author_name = f"{first_name}%" if first_name else f"% {last_name}"

        cursor = _conn.cursor()
        cursor.execute(query, (author_name,))

        results = cursor.fetchall()

        temp = 0
        if not results:
            output.write("No books found for the specified author.\n")
            temp = temp + 1
        else:
            for row in results:
                output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/Q4.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
        return temp

    except Error as e:
        print(e)

def Q5(_conn):
    try:
        output = open('output/Q5.out', 'w')
        header = "{}"
        output.write((header.format("Most Popular Subject")) + '\n')

        query = """
        SELECT s.s_subjectname AS Most_Popular_Subject
        FROM Subjects s
        JOIN (
            SELECT s_subjectkey, COUNT(DISTINCT f_filekey) AS file_count
            FROM ManySubjects
            GROUP BY s_subjectkey
            ORDER BY file_count DESC
            LIMIT 1
        ) AS maxFileCount ON s.s_subjectkey = maxFileCount.s_subjectkey;
        """

        cursor = _conn.cursor()
        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/Q5.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()

    except Error as e:
        print(e)

def sub1Q6(_conn, title):
    querysub1Q6_0 = """ SELECT max(s_subjectkey) FROM Subjects"""
    cursor = _conn.cursor()
    cursor.execute(querysub1Q6_0)
    skey = cursor.fetchone()
    skey = skey[0] if skey else None
    new_skey = skey + 1
    querySubject = """ INSERT INTO Subjects (s_subjectkey, s_subjectname)
                    VALUES (?, ?);"""
    cursor = _conn.cursor()
    cursor.execute(querySubject, (new_skey, title))
    _conn.commit()
    cursor.close()

def publish1Q6(_conn, name):
    querypublish1Q6_0 = """ SELECT max(p_publisherkey) FROM Publisher"""
    cursor = _conn.cursor()
    cursor.execute(querypublish1Q6_0)
    pkey = cursor.fetchone()
    pkey = pkey[0] if pkey else None
    new_pkey = pkey + 1
    queryPublisher = """ INSERT INTO Publisher (p_publisherkey, p_publishername, p_licensingagreement)
                    VALUES (?, ?, ?);"""
    cursor = _conn.cursor()
    cursor.execute(queryPublisher, (new_pkey, name, 1))
    _conn.commit()
    cursor.close()

def Q6(_conn, title, author, date_str, subject, publisher):
    try:
        query6_0 = """ SELECT max(f_filekey) FROM Files"""
        cursor = _conn.cursor()
        cursor.execute(query6_0)
        fkey = cursor.fetchone()
        fkey = fkey[0] if fkey else None
        new_fkey = fkey + 1
        query6_1 = """ SELECT s_subjectkey FROM Subjects WHERE s_subjectname = ?  """
        cursor = _conn.cursor()
        cursor.execute(query6_1, (subject,))
        skey = cursor.fetchone()
        if not skey:
            print("Subject either has not been created yet or there is a typo")
            return 0

        query6_2 = """ SELECT p_publisherkey FROM Publisher WHERE p_publishername = ?  """
        cursor = _conn.cursor()
        cursor.execute(query6_2, (publisher,))
        pkey = cursor.fetchone()
        if not pkey:
            print("Publisher either has not been created yet or there is a typo. \n")
            return 0

        # Extracting values from the tuples
        skey = skey[0] if skey else None
        pkey = pkey[0] if pkey else None

        query6 = """ INSERT INTO Files (f_filekey, f_title, f_author, f_publicationYear, f_publisherkey, f_subjectkey)
                    VALUES (?, ?, ? , ?, ?, ?);"""

        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

        cursor = _conn.cursor()
        cursor.execute(query6, (new_fkey, title, author, date_obj, pkey, skey))

        _conn.commit()
        cursor.close()


        return 1
    except Error as e:
        print(e)
def sub1Q8(_conn, the_subject):
    try:

        querysub1Q8_0 = """ SELECT s_subjectkey FROM Subjects where s_subjectname = ? """
        cursor = _conn.cursor()
        cursor.execute(querysub1Q8_0, (the_subject,))
        the_subjectkey = cursor.fetchone()
        the_subjectkey = the_subjectkey[0] if the_subjectkey else None
        if not the_subjectkey:
            print("Subject intended to be deleted does not exist or is typed wrong. \n")
            return 0
    
        querySD8_1 = """ delete from Subjects WHERE s_subjectkey = ?;"""
        querySD8_2 = """update Subjects set s_subjectkey = s_subjectkey - 1
                 where s_subjectkey > ?;"""

        cursor = _conn.cursor()
        cursor.execute(querySD8_1, (the_subjectkey, ))
        cursor.execute(querySD8_2, (the_subjectkey, ))

        _conn.commit()
        cursor.close()

        return 1
    except Error as e:
        print(e)

def publish1Q8(_conn, the_publisher):
    try:

        querypublish1Q8_0 = """ SELECT p_publisherkey FROM Publisher where p_publishername = ? """
        cursor = _conn.cursor()
        cursor.execute(querypublish1Q8_0, (the_publisher,))
        the_publisherkey = cursor.fetchone()
        the_publisherkey = the_publisherkey[0] if the_publisherkey else None
        if not the_publisherkey:
            print("Publisher intended to be deleted does not exist or is typed wrong. \n")
            return 0
    
        queryPD8_1 = """ delete from Publisher WHERE p_publisherkey = ?;"""
        queryPD8_2 = """update Publisher set p_publisherkey = p_publisherkey - 1
                 where p_publisherkey > ?;"""

        cursor = _conn.cursor()
        cursor.execute(queryPD8_1, (the_publisherkey, ))
        cursor.execute(queryPD8_2, (the_publisherkey, ))

        _conn.commit()
        cursor.close()

        return 1
    except Error as e:
        print(e)

def Q7_sub(_conn, new_name, subject_name):
    try:
        query = """UPDATE Subjects SET s_subjectname = ? WHERE s_subjectname = ?"""
        cursor = _conn.cursor()
        cursor.execute(query, (new_name, subject_name))
        _conn.commit()
    except Error as e:
        print(e)

def Q7_pub(_conn, new_licensing_agreement, publisher_name):
    try:
        query = """UPDATE Publisher SET p_licensingagreement = ? WHERE p_publishername = ?"""
        cursor = _conn.cursor()
        cursor.execute(query, (new_licensing_agreement, publisher_name))
        _conn.commit()
    except Error as e:
        print(e)

def Q7_file(_conn, new_title, new_author, new_publication_year, new_publisher, new_subject, original_title, original_author):
    try:
        queryQ7 = """ SELECT p_publisherkey FROM Publisher where p_publishername = ? """
        cursor = _conn.cursor()
        cursor.execute(queryQ7, (new_publisher,))
        new_publisherkey = cursor.fetchone()
        new_publisherkey = new_publisherkey[0] if new_publisherkey else None

        queryQ7S = """ SELECT s_subjectkey FROM Subjects where s_subjectname = ? """
        cursor = _conn.cursor()
        cursor.execute(queryQ7, (new_subject,))
        new_subjectkey = cursor.fetchone()
        new_subjectkey = new_subjectkey[0] if new_subjectkey else None

        query = """UPDATE Files 
                   SET f_title = ?, 
                       f_author = ?, 
                       f_publicationYear = ?, 
                       f_publisherkey = ?, 
                       f_subjectkey = ? 
                   WHERE f_title = ? AND f_author = ?"""
        cursor = _conn.cursor()
        cursor.execute(query, (
            new_title, new_author, new_publication_year,
            new_publisherkey, new_subjectkey,
            original_title, original_author
        ))
        _conn.commit()
    except Error as e:
        print(e)

def Q8(_conn, title, author):
    try:

        query8_0 = """ SELECT f_filekey FROM Files where f_title = ? and f_author = ? """
        cursor = _conn.cursor()
        cursor.execute(query8_0, (title, author))
        the_filekey = cursor.fetchone()
        the_filekey = the_filekey[0] if the_filekey else None
        if not the_filekey:
            print("File intended to be deleted does not exist or title/author is typed wrong. \n")
            return 0
    
        query8_1 = """ delete from Files WHERE f_filekey = ?;"""
        query8_2 = """update Files set f_filekey = f_filekey - 1
                 where f_filekey > ?;"""

        cursor = _conn.cursor()
        cursor.execute(query8_1, (the_filekey, ))
        cursor.execute(query8_2, (the_filekey, ))

        _conn.commit()
        cursor.close()

        return 1
    except Error as e:
        print(e)

def Q9(_conn, subject_name):
    try:
        output = open('output/9.out', 'w')
        header = "{}|{}|{}|{}|{}"
        output.write((header.format("Title", "Author", "Publication Year", "Borrow Date", "Username")) + '\n')

        query = """
        SELECT Files.f_title, Files.f_author, Files.f_publicationYear, BorrowedBooks.b_borrow_date, User.u_username
        FROM Files
        JOIN ManySubjects ON Files.f_filekey = ManySubjects.f_filekey
        JOIN Subjects ON ManySubjects.s_subjectkey = Subjects.s_subjectkey
        JOIN BorrowedBooks ON Files.f_filekey = BorrowedBooks.b_book_id
        JOIN Student ON BorrowedBooks.b_student_id = Student.s_studentkey
        JOIN User ON Student.s_studentkey = User.u_userkey
        WHERE Subjects.s_subjectname = ?;
        """

        cursor = _conn.cursor()
        cursor.execute(query, (subject_name,))

        results = cursor.fetchall()

        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/9.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()

    except Error as e:
        print(e)

def Q10(_conn):
    try:
        output = open('output/Q10.out', 'w')
        header = "{}|{}"
        output.write((header.format("First Name", "Last Name")) + '\n')

        query = """
        SELECT u_firstname, u_lastname
        FROM User
        WHERE u_userkey IN (
            SELECT s_studentkey
            FROM Student
            WHERE s_studentkey IN (
                SELECT b_student_id
                FROM BorrowedBooks
                WHERE b_status = 'D'
                GROUP BY b_student_id
            )
        )
        GROUP BY u_firstname;
        """

        cursor = _conn.cursor()
        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/Q10.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()

    except Error as e:
        print(e)



def display_files(cursor):
    query = """
    SELECT f_title AS Title, f_author AS Author
    FROM Files
    GROUP BY f_title, f_author
    """
    cursor.execute(query)
    files = cursor.fetchall()

    print(f"Here are all the files in our database ({len(files)}):")
    for file in files:
        print(f"Title: {file[0]}, Author: {file[1]}")

def apply_filter(cursor, category, value):
    if category == 'subject_letter':
        query = """
        SELECT f_title AS Title, f_author AS Author
        FROM Files
        JOIN Subjects ON Files.subject_id = Subjects.subject_id
        WHERE Subjects.s_subjectname LIKE ?;
        """
        cursor.execute(query, (f"{value}%",))
    else:
        query = f"SELECT f_title AS Title, f_author AS Author FROM Files WHERE {category} LIKE ?"
        cursor.execute(query, (f"{value}%",))

    filtered_files = cursor.fetchall()

    print(f"Filtered files for {category} starting with '{value}':")
    for file in filtered_files:
        print(f"Title: {file[0]}, Author: {file[1]}")

def main():
    database = r"librarydb.sqlite"

    conn = openConnection(database)
    #cursor = connection.cursor()

    user_type = input("If you are a student, press 0. If you are a librarian, press 1: ")
    print("\n")

    if user_type == '0':
        #display_files(cursor)

        #filters = []
        p_name = ""
        s_name = ""

        while True:
            # Allow the user to filter by category
            print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
            try : 
                category = int(input("1. Subject\n"
                                 "2. Publisher\n"
                                 "3. Publication date\n"
                                 "4. Author\n"
                                 "5. Most Popular Subject\n"
                                 "0. Leave/Exit\n"
                                 "Choose the corresponding number to filter by a specific category: "))
                                 #"0. Apply Filters and Display Results\n"))
                                 #"Enter 0 to apply filters and display results: "))
                if category == 0:
                # Apply all selected filters
                #for filter_item in filters:
                #    apply_filter(cursor, filter_item['category'], filter_item['value'])
                    break
                if category == 1:
                    while True:
                        letter = input("Enter the letter you want the subject to start with: ")
                        with conn:
                            result = Q1_1(conn, letter)
                        if result: 
                            print("Please try again. ")
                        else :
                            break 
                    while True:
                        s_name = input("Choose the subject you want and its book count will be returned: ")
                        with conn:
                            result = Q1_2(conn, s_name)
                        if result:
                            print("Please try again.")
                        else :
                            break
                if category == 2:
                    print("Here is list of all publishers you can choose from: \n")
                    with conn:
                        Q2_1(conn)
                    while True:
                        p_name = input("Choose a publisher. Ensure no typos or capitalization errors: ")
                        with conn:
                            result = Q2_2(conn,p_name)
                        if result:
                            print("There is an issue. Unfortunately, we by accident did not add files under this publiser. Please choose another.\n")
                        else :
                            break
                if category == 3 :
                    print("You can find books after a cutoff date based on subject and/or publisher. \n")
                    print("If you would like to choose your subject and/or publisher without randomizing, go back to 1 or 2 category. \n")
                    back = input("If you want to go back, type Y uppercase. If not, you can enter: ")
                    while True:
                        if (back == "Y"):
                            s_name = ""
                            p_name = ""
                            break
                        else:
                            if (s_name == "" and p_name == ""):
                                print("You have neither chosen a subject name nor a publisher name \n")
                                print("You will be assigned a random subject and random publisher \n")
                                with conn:
                                    random_values = Q3_1(conn,1)
                                if random_values:
                                    s_name, p_name = random_values[0]
                            elif (s_name == ""):
                                print("You have not chosen a subject name \n")
                                print("You will be assigned a random subject \n")
                                with conn:
                                    random_values = Q3_1(conn,2)
                                if random_values:
                                    s_name = random_values[0][0]
                            elif (p_name == ""):
                                print("You have not chosen a publisher name \n")
                                print("You will be assigned a random publisher \n")
                                with conn:
                                    random_values = Q3_1(conn,3)
                                    if random_values:
                                        p_name = random_values[0][0]
                            print("\n")
                            while True:
                                year = input("Regarding publication date, what is the earliest year a book you want can be from: ")
                                with conn:
                                    result = Q3_2(conn,year,s_name,p_name)
                                if result:
                                    print("Please try again with a different year or by accident we did not add this subject under this publisher. \n")
                                    print("To prevent continuouly finding a good cutoff date, we advise you to choose again from categories. \n")
                                    break
                                else:
                                    break
                            break
                if category == 4:
                    filter_option = input("Please filter by (F)irst name.").upper()

                    if filter_option == 'F':
                        first_name = input("Type in the first name: ")
                        with conn:
                            result = Q4(conn, first_name=first_name)
                    #elif filter_option == 'L':
                    #    last_name = input("Type in the last name: ")
                    #    with conn:
                    #        result = Q4(conn, last_name=last_name)
                    else:
                        print("Not a valid input")

                if category == 5:
                    with conn:
                        Q5(conn)
            except :
                print("Invalid Input \n")


    elif user_type == '1':
        # Handle teacher actions
         while True:
            # Allow the user to filter by category
            print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
            #try : 
            category = int(input("1. Insert a book/subject/publisher\n"
                                 "2. Update a book/subject/publisher\n"
                                 "3. Delete a book/subject/publisher\n"
                                 "4. Display books checked out by who/ when depending on subject\n"
                                 "5. Look up students w/ overdue books\n"
                                 "0. Leave/Exit\n"
                                 "Choose the corresponding number to filter by a specific category: "))
                                 #"0. Apply Filters and Display Results\n"))
                                 #"Enter 0 to apply filters and display results: "))
            if  category == 0 :
                    break
            if category == 1 :
                    print("Would you like to create a new  subject or new publisher or new book with existing subjects/publishers?")
                    choice = input("Type S for subject, P for publisher, and F for file: ")
                    if choice == 'F':
                        title = input("Type the title of the book: ")
                        author = input("Type the full name of the author: ")
                        date_str = input("Type the publication date: ")
                        subject = input("Type the main subject: ")
                        publisher = input("Type the publisher correctly: ")
                        with conn:
                            Q6(conn, title, author, date_str, subject, publisher)
                    if choice == 'S':
                        title = input("Type name of new subject: ")
                        with conn:
                            sub1Q6(conn, title)
                    if choice == 'P':
                        name = input("Type name of publisher with a licensing agreement with the library: ")
                        with conn:
                            publish1Q6(conn, name)
            if category == 2 :
                print("Would you like to edit a subject or publisher or book?")
                choice = input("Type S for subject, P for publisher, and F for file: ")
                if choice == 'F':
                    original_title = input("Type the current title of the book: ")
                    original_author = input("Type the current name of the author: ")
                    new_title = input("Type new title of the book: ")
                    new_author = input("Type new author name: ")
                    new_publication_year = input("Type new publication date: ")
                    new_subject = input("Type new main subject: ")
                    new_publisher = input("Type new publisher correctly: ")
                    with conn:
                        Q7_file(conn, new_title, new_author, new_publication_year, new_publisher, new_subject, original_title, original_author)
                if choice == 'S':
                    subject_name = input("Type name of the subject: ")
                    new_name = input("Type a changed name of the subject: ")
                    with conn:
                        Q7_sub(conn, new_name, subject_name)
                if choice == 'P':
                    publisher_name = input("Type name of publisher with a licensing agreement with the library: ")
                    new_licensing_agreement = int(input("Type 0 or 1. 0 for no agreement and 1 for yes: "))
                    with conn:
                        Q7_pub(conn, new_licensing_agreement, publisher_name)
            if category == 3 :
                print("Would you like to delete a  subject or a publisher or a book?")
                choice = input("Type S for subject, P for publisher, and F for file: ")
                if choice == 'F':
                    title = input("Type the title of the book: ")
                    author = input("Type the full name of the author: ")
                    with conn:
                        Q8(conn, title, author)
                if choice == 'S':
                    the_subject = input("Type name of the subject: ")
                    with conn:
                        sub1Q8(conn, the_subject)
                if choice == 'P':
                    the_publisher = input("Type name of the publisher: ")
                    with conn:
                        publish1Q8(conn, the_publisher)
            if category == 4:
                while True:
                    subject_name = input("Enter the subject name to display books checked out by who and when: ")
                    with conn:
                        Q9(conn, subject_name)
                    break
            if category == 5:
                with conn:
                    Q10(conn)


            


            #except: 
            #    print("Invalid Input Hello \n")
    else:
        print("Invalid input. Please enter 0 or 1.")

    closeConnection(conn, database)

if __name__ == "__main__":
    main()
