import sqlite3

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel

dbPath = r"C:\Users\stoen\Desktop\ComponentsDatabase\src\db\products.db"

conn = sqlite3.connect(dbPath)
cursor = conn.cursor()

# Create the db if it doesn't exist
def initDatabase():
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL,
            model TEXT NOT NULL,
            code TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            datasheet TEXT NOT NULL
        )
        ''')
    except Exception as e:
        print(f"Error initializing database: {e}")

def updateAddFromDB(typeC, modelC, codeC, amountC):
    try:
        cursor.execute('''
            UPDATE products SET quantity = COALESCE(quantity, 0) + ? WHERE type = ? AND model = ? AND code = ?
        ''', (amountC, typeC, modelC, codeC))
        conn.commit()
    except Exception as e:
        print(f"Error updating quantity: {e}")

def isItInDB(typeC, modelC, codeC):
    try:
        cursor.execute('''SELECT * FROM products WHERE type = ? AND model = ? AND code = ?''', (typeC, modelC, codeC))
        result = cursor.fetchall()
        return len(result) > 0
    except Exception as e:
        print(f"Error checking existence: {e}")
        return False

def addProduct(typeC, modelC, codeC, quantityC, datasheetC):
    lowcase_type = typeC.lower()
    lowcase_model = modelC.lower()
    lowcase_codeC = codeC.lower()

    try:
        if isItInDB(lowcase_type, lowcase_model, lowcase_codeC):
            updateAddFromDB(lowcase_type, lowcase_model, lowcase_codeC, quantityC)
        else:
            cursor.execute('''
            INSERT INTO products (type, model, code, quantity, datasheet) VALUES (?, ?, ?, ?, ?)
            ''', (lowcase_type, lowcase_model, lowcase_codeC, quantityC, datasheetC))
        conn.commit()
    except Exception as e:
        print(f"Error adding product: {e}")

def getAllTypes():
    try:
        cursor.execute('''SELECT DISTINCT type FROM products''')
        types = cursor.fetchall()
        typesList = [types[0] for types in types]
        return typesList
    except Exception as e:
        print(f"Error fetching all types: {e}")
        return None

def getMatchingModels(typeC):
    try:
        cursor.execute('''SELECT DISTINCT model FROM products WHERE type = ?''', (typeC,))
        models = cursor.fetchall()
        modelsList = [models[0] for models in models]
        return modelsList
    except Exception as e:
        print(f"Error fetching matching models: {e}")
        return None

def getMatchingCodes(typeC, modelC):
    try:
        cursor.execute('''SELECT DISTINCT code FROM products WHERE model = ? AND type = ?''', (modelC,typeC))
        codes = cursor.fetchall()
        codesList = [codes[0] for codes in codes]
        return codesList
    except Exception as e:
        print(f"Error fetching matching codes: {e}")
        return None

def removeItemFromDB(typeC, modelC, codeC):
    try:
        cursor.execute('''DELETE FROM products WHERE type = ? AND model = ? AND code = ?''', (typeC, modelC, codeC))
        conn.commit()
    except Exception as e:
        print(f"Error removing item from DB: {e}")

def updateSubFromDB(typeC, modelC, codeC, amountC):
    try:
        cursor.execute('''
            UPDATE products SET quantity = COALESCE(quantity, 0) - ? WHERE type = ? AND model = ? AND code = ?
        ''', (amountC, typeC, modelC, codeC))
        conn.commit()
    except Exception as e:
        print(f"Error updating quantity: {e}")

def searchProduct(typeC, modelC, codeC):
    try:
        cursor.execute('''SELECT quantity, datasheet FROM products where type = ? AND model = ? AND code = ?''', (typeC, modelC, codeC))
        quantity_n_datasheet = cursor.fetchall()
        return quantity_n_datasheet
    except Exception as e:
        print(f"Error searching for product: {e}")
        return None

def getTreeViewModel():
    try:
        cursor.execute('''SELECT * FROM products''')
        extracted_data = cursor.fetchall()
        return extracted_data
    except Exception as e:
        print(f"Error fetching tree view model: {e}")
        return None

conn.commit()
