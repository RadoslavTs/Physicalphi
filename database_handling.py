import sqlite3
from helpers import get_password_hash, get_today


# function to create the database on a first initialization
def create_db():
    measurement_types = ["WEIGHT", "HEIGHT"]
    connection = sqlite3.connect('db/users.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS USERS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME TEXT NOT NULL,
            PASSWORD TEXT NOT NULL,
            FIRST_NAME TEXT NOT NULL,
            LAST_NAME TEXT NOT NULL,
            DOB TEXT,
            SEX TEXT,
            BLOOD_TYPE TEXT)
            """)
    c.execute(f"""CREATE TABLE IF NOT EXISTS MEASUREMENTS_TYPES (
            TYPE TEXT PRIMARY KEY)
            """)
    c.execute("""CREATE TABLE IF NOT EXISTS CALENDAR (
            DATE TEXT NOT NULL,
            DESCRIPTION TEXT NOT NULL,
            EVENT_TYPE TEXT NOT NULL, 
            USER_ID INTEGER NOT NULL,
            FOREIGN KEY(USER_ID) REFERENCES USERS(ID))
            """)
    c.execute(f"""CREATE TABLE IF NOT EXISTS MEASUREMENTS (
            MEASUREMENT FLOAT NOT NULL,
            MEASUREMENT_DATE TEXT NOT NULL,
            USER_ID INTEGER NOT NULL,
            MEASUREMENT_TYPE TEXT NOT NULL,
            FOREIGN KEY(USER_ID) REFERENCES USERS(ID),
            FOREIGN KEY(MEASUREMENT_TYPE) REFERENCES MEASUREMENTS_TYPES(TYPE))
            """)
    c.execute("PRAGMA foreign_keys = ON")
    for measurement_type in measurement_types:
        c.execute("PRAGMA foreign_keys = ON")
        c.execute(f"SELECT * FROM MEASUREMENTS_TYPES WHERE TYPE='{measurement_type}'")
        record = c.fetchall()
        if not record:
            c.execute("INSERT INTO MEASUREMENTS_TYPES (TYPE)"
                      f"VALUES ('{measurement_type}')")

    connection.commit()
    connection.close()


# function to check if valid credentials have been provided for the login
def check_login(username, password):
    connection = sqlite3.connect('db/users.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    hashed_pass = get_password_hash(password)
    c.execute(f"SELECT * FROM USERS WHERE USERNAME='{username}'")
    record = c.fetchall()
    if record:
        if hashed_pass == record[0][2]:
            return True
        else:
            return False

    connection.commit()
    connection.close()


def get_user_id(username):
    connection = sqlite3.connect('db/USERS.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute(f"SELECT * FROM USERS WHERE USERNAME='{username}'")
    record = c.fetchall()
    return record[0][0]


# function to populate the database with a new user data and create all the necessary supplementary databases
def create_new_user(username, password, first_name, last_name):
    connection = sqlite3.connect('db/USERS.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute("SELECT * FROM USERS")
    record = c.fetchall()
    users = []
    for user in record:
        users.append(user[1])
    if username not in users:
        hashed_password = get_password_hash(password)
        c.execute("INSERT INTO USERS (USERNAME, PASSWORD, FIRST_NAME, LAST_NAME)"
                  f"VALUES ('{username}', '{hashed_password}', '{first_name}', '{last_name}')")
        connection.commit()
        connection.close()
        return True
    else:
        return False


# function to provide the persons names
def get_user_names(user_id):
    connection = sqlite3.connect('db/USERS.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute(f"SELECT * FROM USERS WHERE ID={user_id}")
    record = c.fetchall()
    first_name = record[0][3]
    second_name = record[0][4]
    connection.commit()
    connection.close()

    return f"{first_name} {second_name}"


# function to provide all data for a person
def get_user_data(user_id):
    connection = sqlite3.connect('db/USERS.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute("PRAGMA foreign_keys = ON")
    c.execute(f"SELECT USERNAME FROM USERS WHERE ID='{user_id}'")
    username = c.fetchall()[0][0]
    c.execute(f"SELECT FIRST_NAME FROM USERS WHERE ID='{user_id}'")
    first_name = c.fetchall()[0][0]
    c.execute(f"SELECT LAST_NAME FROM USERS WHERE ID='{user_id}'")
    last_name = c.fetchall()[0][0]
    c.execute(f"SELECT DOB FROM USERS WHERE ID='{user_id}'")
    date_of_birth = c.fetchall()[0][0]
    c.execute(f"SELECT SEX FROM USERS WHERE ID='{user_id}'")
    sex = c.fetchall()[0][0]
    c.execute(f"SELECT BLOOD_TYPE FROM USERS WHERE ID='{user_id}'")
    blood_type = c.fetchall()[0][0]

    c.execute(f"SELECT * FROM MEASUREMENTS WHERE USER_ID={user_id} AND MEASUREMENT_TYPE='WEIGHT'")
    weight_measurements = c.fetchall()
    c.execute(f"SELECT * FROM MEASUREMENTS WHERE USER_ID={user_id} AND MEASUREMENT_TYPE='HEIGHT'")
    height_measurements = c.fetchall()
    if weight_measurements:
        weight = weight_measurements[-1][0]
    else:
        weight = None
    if height_measurements:
        height = height_measurements[-1][0]
    else:
        height = None

    user_data = {'username': username, 'first name': first_name, 'last name': last_name,
                 'dob': date_of_birth, 'sex': sex, 'weight': weight, 'height': height, 'bloodtype': blood_type}
    connection.commit()
    connection.close()

    return user_data


# function to provide statistical data for the user
def get_user_statistics(userid, measurement_type):
    connection = sqlite3.connect('db/USERS.db')
    c = connection.cursor()
    c.execute(f"SELECT * FROM MEASUREMENTS WHERE MEASUREMENT_TYPE='{measurement_type}' and USER_ID='{userid}'")
    record = c.fetchall()
    connection.commit()
    connection.close()

    return record


# function to update persons data
def update_user_details(user_id, dob, sex, bloodtype):
    connection_users = sqlite3.connect('db/USERS.db')
    c = connection_users.cursor()
    c.execute(f"UPDATE USERS SET DOB='{dob}', SEX='{sex}', BLOOD_TYPE='{bloodtype}'"
              f" WHERE ID='{user_id}'")

    connection_users.commit()
    connection_users.close()


# function to update persons weight and statistics
def update_meas(user_id, measurement, meas_type):
    date = get_today()
    connection = sqlite3.connect('db/USERS.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute(f"SELECT * FROM MEASUREMENTS WHERE MEASUREMENT_DATE='{date}' AND"
              f" MEASUREMENT_TYPE='{meas_type}' AND USER_ID='{user_id}'")
    existing = c.fetchall()
    if not existing:
        c.execute("INSERT INTO MEASUREMENTS (MEASUREMENT, MEASUREMENT_DATE, USER_ID, MEASUREMENT_TYPE)"
                  f"VALUES ('{measurement}', '{date}', '{user_id}', '{meas_type}')")
    else:
        c.execute(f"UPDATE MEASUREMENTS SET MEASUREMENT='{measurement}'"
                  f" WHERE MEASUREMENT_TYPE='{meas_type}' AND MEASUREMENT_DATE='{date}' AND USER_ID='{user_id}'")
    connection.commit()
    connection.close()


# function to add new entry to the calendar
def add_to_calendar(date, description, userid):
    event_type = 'event'
    connection = sqlite3.connect('db/users.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute("INSERT INTO CALENDAR (DATE, DESCRIPTION, EVENT_TYPE, USER_ID)"
              f"VALUES (?, ?, ?, ?)", (date, description, event_type, userid))

    connection.commit()
    connection.close()


# function to get all data for persons calendar
def get_calendar_info(userid):
    connection = sqlite3.connect('db/users.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute(f"SELECT * FROM CALENDAR WHERE USER_ID='{userid}'")

    record = c.fetchall()
    calendar_entries = {}
    for line in record:
        calendar_entries[line[0]] = (line[1], line[2])

    connection.commit()
    connection.close()

    return calendar_entries


# function to get entries from the calendar for a current day
def get_calendar_today(userid, date):
    connection = sqlite3.connect('db/USERS.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute(f"SELECT * FROM CALENDAR WHERE date='{date}' and USER_ID='{userid}'")
    record = c.fetchall()
    today = []
    for line in record:
        today.append(line[1])

    connection.commit()
    connection.close()

    return today


def remove_from_calendar(userid, date, description):
    connection = sqlite3.connect('db/USERS.db')
    c = connection.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    # c.execute(f"DELETE FROM CALENDAR WHERE date='{date}' and USER_ID='{userid}'
    # and DESCRIPTION LIKE '%{description}%'")

    connection.commit()
    connection.close()


# function to manually query the db
# def query_db(user_id, date, meas_type):
#     connection = sqlite3.connect('db/USERS.db')
#     c = connection.cursor()
#     c.execute("PRAGMA foreign_keys = ON")
#     c.execute(f"SELECT * FROM MEASUREMENTS WHERE MEASUREMENT_TYPE='{meas_type}' AND
#     USER_ID='{user_id}' AND MEASUREMENT_DATE='{date}' ")
#     record = c.fetchall()
#
#     for row in record:
#         print(row)
#
#     connection.commit()
#     connection.close()
#


# def manual_insert():
#     connection = sqlite3.connect('db/USERS.db')
#     c = connection.cursor()
#     c.execute("PRAGMA foreign_keys = ON")
#
#     c.execute("INSERT INTO USERS (USERNAME, PASSWORD, FIRST_NAME, LAST_NAME)"
#               "VALUES ('rado', '1234', 'Radoslav', 'Tsepenishev')")
#
#     c.execute("INSERT INTO CALENDAR (DATE, DESCRIPTION, EVENT_TYPE, USER_ID)"
#               "VALUES ('1 January 2023', 'Doctors appointment', 'Event', 1)")
#
#     c.execute("INSERT INTO MEASUREMENTS_TYPES (TYPE)"
#               "VALUES ('WEIGHT')")
#
#     c.execute("INSERT INTO MEASUREMENTS (MEASUREMENT, MEASUREMENT_DATE, USER_ID, MEASUREMENT_TYPE)"
#               "VALUES (25, '2 January 2023', 1, 'WEIGHT')")
#     c.execute("INSERT INTO MEASUREMENTS (MEASUREMENT, MEASUREMENT_DATE, USER_ID, MEASUREMENT_TYPE)"
#               "VALUES (25, '2 January 2023', 1, 'WEIGHT')")
#
#     connection.commit()
#     connection.close()

# def manual_insert_weight():
#     connection = sqlite3.connect('db/USERS.db')
#     c = connection.cursor()
#     c.execute("PRAGMA foreign_keys = ON")
#     c.execute("INSERT INTO MEASUREMENTS (MEASUREMENT, MEASUREMENT_DATE, USER_ID, MEASUREMENT_TYPE)"
#               "VALUES ('103', '2023-04-03', 1, 'WEIGHT')")
#
#     connection.commit()
#     connection.close()
# # #
#
# def query_db():
#     connection = sqlite3.connect('db/USERS.db')
#     c = connection.cursor()
#     c.execute("PRAGMA foreign_keys = ON")
#     c.execute(f"SELECT * FROM MEASUREMENTS WHERE MEASUREMENT_TYPE='WEIGHT'")
#     record = c.fetchall()
#
#     for row in record:
#         print(row)
#
#     connection.commit()
#     connection.close()
# #
# manual_insert_weight()
# query_db()
