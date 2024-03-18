import mysql.connector


def create_connection():
    connection = None

    try:
        connection =  mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "pythontest",
            port = "3306"
        )
        print("Verbindung zur Datenbank ist erfolgreich!")
        return connection
    
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def fetch_data(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM personen"

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            print(row)
    
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def fetch_data_where_id(connection, id):
    cursor = connection.cursor()

    query = f"SELECT * FROM personen WHERE id={id};"

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


def insert_data(connection, anrede, vorname, nachname, plz, straße, hausnr, stadt):
    cursor = connection.cursor()

    tables = "(anrede, vorname, nachname, plz, straße, hausnr, stadt)"
    values = f"('{anrede}', '{vorname}', '{nachname}', '{plz}', '{straße}', '{hausnr}', '{stadt}')"

    query = f"INSERT INTO personen {tables} VALUES {values};"

    try:
        cursor.execute(query)
        connection.commit()
        print("Daten erfolgreich eingefügt")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def update_data(connection, id, anrede, vorname, nachname, plz, straße, hausnr, stadt):
    cursor = connection.cursor()
    
    query = f"UPDATE personen SET id={id} WHERE vorname ='{vorname}' AND nachname = '{nachname}';"
    
    try:
        cursor.execute(query)
        connection.commit()
        print("Daten erfolgreich geupdatet")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def delete_data_by_id(connection, id):
    cursor = connection.cursor()

    query = f"DELETE FROM personen WHERE id={id};"

    try:
        cursor.execute(query)
        connection.commit()
        print("Daten erfolgreich gelöscht")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def create_table_example(connection):
    cursor = connection.cursor()

    query = f"""
    CREATE TABLE IF NOT EXISTS kartennummer
    (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kartenNr VARCHAR(255)
    )
    """

    try:
        cursor.execute(query)
        connection.commit()
        print("Beispieltabelle erfolgreich erstellt")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


# create_connection()
# insert_data(create_connection(), "Herr", "Lichael", "Mutz", "12345", "Landstraße", "99999-A/2", "Karlsunruhe")
# fetch_data(create_connection())
# update_data(create_connection(),9957627,"Herr", "Lichael", "Mutz","12345", "Landstraße","99999-A/2", "Karlsunruhe")
# fetch_data_where_id(create_connection(), 9957627)
# delete_data_by_id(create_connection(), 9957627)
create_table_example(create_connection())        