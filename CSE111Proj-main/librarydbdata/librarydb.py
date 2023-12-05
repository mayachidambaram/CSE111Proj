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

def Q3_1(_conn, num){
    try: 
        if num = 1:
            output = open('output/3_1.out', 'w')
            header = "{}|{}"
            output.write((header.format("Random Subject","Random Publisher")) + '\n')
            query3_1 = """ select 
                            (select s_subjectname 
                            from Subjects 
                            order by RANDOM() limit 1) as random_subject,
                            (select p_publishername 
                            from Publishers
                            order by RANDOM() limit 1) as random_subject) as random_publisher"""
        elif num = 2:
            output = open('output/3_1.out', 'w')
            header = "{}"
            output.write((header.format("Random Subject")) + '\n')
            query3_1 = """ select s_subjectname as random_subject
                           from Subjects 
                           order by RANDOM() 
                           limit 1"""

        elif num = 3:
            output = open('output/3_1.out', 'w')
            header = "{}"
            output.write((header.format("Random Publisher")) + '\n')
            query3_1 = """ select p_publishername 
                           from Publishers
                           order by RANDOM() 
                           limit 1"""

        cursor = _conn.cursor()
        cursor.execute(query3_1, (p_name,))

        results = cursor.fetchall()

        for row in results:
            output.write("|".join(map(str, row)) + '\n')
        output.close()

        with open('output/3_1.out', 'r') as output:
            file_content = output.read()
            print(file_content)
        output.close()
    except Error as e:
        print(e)
}

def Q3_2(_conn){
    try:
        output = open('output/3_2.out','w')
        header - "{}|{}"
        #working on this

}

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
            print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
            category = int(input("1. Subject\n"
                                 "2. Publisher\n"
                                 "3. Publication date\n"
                                 "4. Author\n"
                                 "5. File Keywords\n"
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
                while True:
                    letter = input("Enter the letter you want the subject to start with: ")
                    with conn:
                        result = Q1_1(conn, letter)
                        if result: 
                            print("Please try again. ")
                        else :
                            break 
                while True:
                    s_name = ""
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
                While True:
                    p_name = ""
                    p_name = input("Choose a publisher. Ensure no typos or capitalization errors: ")
                    with conn:
                        result = Q2_2(conn,p_name)
                        if result:
                            print()
                        else :
                            break
            if category == 3 :
                print("You can find books after a cutoff date based on subject and/or publisher. \n")
                if (s_name = "" and p_name = ""){
                    print("You have neither chosen a subject name nor a publisher name.\n")
                    print("You will be assigned a random subject and random publisher.\n")
                    with conn:
                        Q3_1(conn,1)
                }
                elif (s_name = ""){
                    print("You have not chosen a subject name.\n")
                    print("You will be assigned a random subject.\n")
                    with conn:
                        Q3_1(conn,2)
                }
                elif (p_name = ""){
                    print("You have not chosen a publisher name.\n")
                    print("You will be assigned a random publisher.\n")
                    with conn:
                        Q3_1(conn,3)
                }
                print("\n")
                
                with conn:
                    Q3_2(conn)

            #elif category in range(1, 7):
            #    category_mapping = {
            #        1: 'subject_letter',
            #        2: 'publisher',
            #        3: 'publisher_date',
            #        4: 'author_first_name',
            #        5: 'author_last_name',
            #        6: 'never_borrowed'
            #    }
            #    category_name = category_mapping[category]
            #    if category != 6:
            #        value = input(f"Input which {category_name} you'd like to filter by: ")
            #        filters.append({'category': category_name, 'value': value})
            #    else:
            #        # For 'never_borrowed', set an arbitrary value
            #        filters.append({'category': category_name, 'value': 'dummy'})

            #else:
            #    print("Invalid category. Please choose a number between 0 and 6.")

    elif user_type == '1':
        # Handle teacher actions
        pass
    else:
        print("Invalid input. Please enter 0 or 1.")

    closeConnection(conn, database)

if __name__ == "__main__":
    main()
