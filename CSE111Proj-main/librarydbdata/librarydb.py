import sqlite3

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
                       where strftime('%Y',F.f_publicationYear) <= ? 
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

    user_type = input("If you are a student, press 0. If you are a teacher, press 1: ")
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
                                 "5. Most Popular Subject"
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
                    filter_option = input("Do you want to filter by (F)irst name or (L)ast name? ").upper()

                    if filter_option == 'F':
                        first_name = input("Type in the first name: ")
                        with conn:
                            result = Q4(conn, first_name=first_name)
                    elif filter_option == 'L':
                        last_name = input("Type in the last name: ")
                        with conn:
                            result = Q4(conn, last_name=last_name)
                    else:
                        print("Invalid option. Please enter 'F' for first name or 'L' for last name.")

                if category == 5:
                    print("We have a number of subjects")
            except :
                print("Invalid Input \n")
            

    elif user_type == '1':
        # Handle teacher actions
         while True:
            # Allow the user to filter by category
            print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
            try : 
                category = int(input("1. Insert a book"
                                 "2. Update a book"
                                 "3. Delete a book"
                                 "1. Display books checked out by who/ when depending on subject\n"
                                 "2. Display books \n" #smth about update/delete/insert
                                 "5. Look up students w/ overdue books\n"
                                 "0. Leave/Exit\n"
                                 "Choose the corresponding number to filter by a specific category: "))
                                 #"0. Apply Filters and Display Results\n"))
                                 #"Enter 0 to apply filters and display results: "))
            except : 
                print("Invalid Input \n")
    else:
        print("Invalid input. Please enter 0 or 1.")

    closeConnection(conn, database)

if __name__ == "__main__":
    main()
