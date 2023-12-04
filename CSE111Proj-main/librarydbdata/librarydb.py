import sqlite3

def openConnection(_dbFile):
    print("Open database: ", _dbFile)
    conn = None
    try :
        conn = sqlite3.connect(_dbFile)
        print("Welcome to the library database management system.")
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

    
def Q1(_conn, letter):
    print("1. Subject Letter\n")

    try:
        output = open('output/1.out', 'w')
        header = "{}"
        output.write((header.format("Subject/s :")) + '\n')
        query1 = """ SELECT s_subjectname as subject 
                 FROM Subjects  
                 WHERE s_subjectname 
                 LIKE ?; """

        cursor = _conn.cursor()
        cursor.execute(query1, (f'{letter.upper()}%',))

        results = cursor.fetchall()

        if not results:
            output.write("No subjects found starting with specified letter.\n")
        else:
            for row in results:
                output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/1.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
    except Error as e:
        print(e)

def Q2(_conn):
    print("2. Number of Books In Each Subject\n")

    try:
        output = open('output/2.out', 'w')
        header = "{}|{}"
        output.write((header.format("Subject","Book Count")) + '\n')
        query2 = """ SELECT S.s_subjectname as Subject, count(F.f_filekey) as booknuminsubj 
        FROM Files F, Subjects S, ManySubjects M
        Where F.f_filekey = M.f_filekey and S.s_subjectkey = M.s_subjectkey
        Group By S.s_subjectname """

        cursor = _conn.cursor()
        cursor.execute(query2)

        results = cursor.fetchall()

        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/2.out', 'r') as output:
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

    user_type = input("If you are a student, press 0. If you are a teacher, press 1: ")
    print("\n")

    if user_type == '0':
        #display_files(cursor)

        filters = []

        while True:
            # Allow the user to filter by category
            print("-------------------------------------------------------------\n")
            category = int(input("1. Subject Letter\n"
                                 "2. Number of Books In Each Subject\n"
                                 "3. Publisher date\n"
                                 "4. Author First Name\n"
                                 "5. Author Last Name\n"
                                 "6. Never before borrowed book\n"
                                 "0. Exit or Restart\n"
                                 "Choose the corresponding number to filter by a specific category: "))
                                 #"0. Apply Filters and Display Results\n"))
                                 #"Enter 0 to apply filters and display results: "))

            if category == 0:
                # Apply all selected filters
                #for filter_item in filters:
                #    apply_filter(cursor, filter_item['category'], filter_item['value'])
                break
            if category == 1:
                letter = ""
                letter = input("Enter the letter you want the subject to start with: ")
                with conn:
                    Q1(conn, letter)
            if category == 2:
                with conn:
                    Q2(conn)
            elif category in range(1, 7):
                category_mapping = {
                    1: 'subject_letter',
                    2: 'publisher',
                    3: 'publisher_date',
                    4: 'author_first_name',
                    5: 'author_last_name',
                    6: 'never_borrowed'
                }
                category_name = category_mapping[category]
                if category != 6:
                    value = input(f"Input which {category_name} you'd like to filter by: ")
                    filters.append({'category': category_name, 'value': value})
                else:
                    # For 'never_borrowed', set an arbitrary value
                    filters.append({'category': category_name, 'value': 'dummy'})

            else:
                print("Invalid category. Please choose a number between 0 and 6.")

    elif user_type == '1':
        # Handle teacher actions
        pass
    else:
        print("Invalid input. Please enter 0 or 1.")

    closeConnection(conn, database)

if __name__ == "__main__":
    main()
