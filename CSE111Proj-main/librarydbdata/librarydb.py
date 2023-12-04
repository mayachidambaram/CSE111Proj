import sqlite3

def connect_to_database():
    connection = sqlite3.connect('librarydb.sqlite')  
    return connection

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
    connection = connect_to_database()
    cursor = connection.cursor()

    print("Welcome to the library database management system.")
    user_type = input("If you are a student, press 0. If you are a teacher, press 1: ")

    if user_type == '0':
        display_files(cursor)

        filters = []

        while True:
            # Allow the user to filter by category
            category = int(input("Choose the corresponding number to filter by a specific category:\n"
                                 "1. Subject Letter\n"
                                 "2. Publisher\n"
                                 "3. Publisher date\n"
                                 "4. Author First Name\n"
                                 "5. Author Last Name\n"
                                 "6. Never before borrowed book\n"
                                 "0. Apply Filters and Display Results\n"
                                 "Enter 0 to apply filters and display results: "))

            if category == 0:
                # Apply all selected filters
                for filter_item in filters:
                    apply_filter(cursor, filter_item['category'], filter_item['value'])
                break
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

    connection.close()

if __name__ == "__main__":
    main()
