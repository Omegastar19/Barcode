import mysql.connector

# Functies voor aanmaken en verwijderen van databases
def create_database(database_name):
    """Deze functie maakt een databse aan met de gewenste naam (database_name)"""
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root"
    )

    mycursor = mydb.cursor()

    try:
       sql = "CREATE DATABASE " + database_name
       mycursor.execute(sql)
       print("Database aangemaakt met de naam " + database_name)
    except mysql.connector.errors.DatabaseError:
       print("Er is al een database met de naam " + database_name)

def delete_database(database_name):
   """Met behulp van deze functie kunnen we de database met naam 'database_name' verwijderen"""
   mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root"
    )

   mycursor = mydb.cursor()
   sql = "DROP DATABASE " + database_name
   mycursor.execute(sql) 

# Functies voor het aanmaken en verwijderen van tabellen in een database
def create_table(database_name, table_name, column_tuple):
    """
    Deze functie maakt binnen een database (naar keuze) een tabel aan met een door de gebruiker gekozen naam en kolomnamen.
    Argumenten:
    - database
    - tabelnaam
    - kolomnamen
    """
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database = database_name
    )
    
    sql = "CREATE TABLE " + table_name + " (" + column_tuple + ")"
    mycursor = mydb.cursor()
    mycursor.execute(sql)

    mydb.commit()

def delete_table(database_name, table_name):
    """
    Met behulp van deze functie kunnen we een tabel naar keuze uit de datbase verwijderen
    """
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database = database_name
    )
    sql = "DROP TABLE " + table_name

    mycursor = mydb.cursor()
    mycursor.execute(sql)

    mydb.commit()

# Functie ten behoeve van het toevoegen en verwijderen van artikelen in de database
def add_product(database_name, table_name, omschrijving, barcode, voorraad):
    """"""
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database= database_name
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO " + table_name + " (omschrijving, barcode, voor raad) VALUES (%s, %s, %s)"
    val = (omschrijving, barcode, voorraad)
    mycursor.execute(sql, val)

    mydb.commit()

def delete_data(database_name, table_name, property_name, value):
    """
    Deze functie verwijdert data in een tabel (naar keuze) binnen een database (naar keuze)
    Verwijdert een compleet artikel
    """
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database= database_name
    )

    if property_name == 'voorraad':
        print("U kunt geen artikel op basis van de voorraad verwijderen")
    elif property_name == 'omschrijving' or property_name == 'barcode':
        sql = "DELETE FROM " + table_name + " WHERE " + property_name + "=%s"
        val = (value,)

        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
    
    mydb.commit()

def increase_inventory(database_name, tabel_naam, barcode):
    """Deze functie verhoogt de voorraad van het product met barcode met 1"""
    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user= "root",
        database = database_name
    )    

    mycursor = mydb.cursor()

    sql_get_inventory = "SELECT voorraad FROM " + tabel_naam + " WHERE barcode = " + barcode
    mycursor.execute(sql_get_inventory)
    result = mycursor.fetchone()

    voorraad = result[0]
    print("Voorraad voor scannen: " + str(voorraad))
    voorraad += 1
    print("Voorraad na scannen: " + str(voorraad))

    sql_increase_inventory = "UPDATE " + tabel_naam + " SET voorraad = " + str(voorraad) + " WHERE barcode = " + barcode
    mycursor.execute(sql_increase_inventory)
    
    mydb.commit()

def decrease_inventory(database_name, tabel_naam, barcode):
    """Deze functie verhoogt de voorraad van het product met barcode met 1"""
    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user= "root",
        database = database_name
    )    

    mycursor = mydb.cursor()

    sql_get_inventory = "SELECT voorraad FROM " + tabel_naam + " WHERE barcode = " + barcode
    mycursor.execute(sql_get_inventory)
    result = mycursor.fetchone()

    voorraad = result[0]
    print("Voorraad voor scannen: " + str(voorraad))
    voorraad -= 1
    print("Voorraad na scannen: " + str(voorraad))

    sql_increase_inventory = "UPDATE " + tabel_naam + " SET voorraad = " + str(voorraad) + " WHERE barcode = " + barcode
    mycursor.execute(sql_increase_inventory)
    
    mydb.commit()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ruimte voor testen functies


# create_database("Magazijn")
# delete_database("magazijn")
# create_table('magazijn', 'voorraad', ("id INT AUTO_INCREMENT PRIMARY KEY, omschrijving VARCHAR (255), barcode VARCHAR(255), voorraad INT"))
# delete_table('magazijn', 'voorraad')
# add_product('magazijn', 'voorraad', 'Crash Course Programmeren in Python', 9789059056749, 10)
# add_product('magazijn', 'voorraad', 'PHP & MYSQL server-side web development', 9781119149224, 10)
# delete_data('magazijn', 'voorraad', 'voorraad', 10)
# delete_data('magazijn', 'voorraad', 'barcode', 9781119149224)

# increase_inventory("magazijn", "voorraad", "9781119149224")
for scans in range(1, 4):
    decrease_inventory("magazijn", "voorraad", "9781119149224")