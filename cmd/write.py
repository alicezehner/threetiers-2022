import mysql.connector

cnx = mysql.connector.connect(user='root', 
    password='password',
    host='127.0.0.1',
    database='education',
    auth_plugin='mysql_native_password')

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 

college = input('Enter college name: ')
students = input('Enter student population: ')

cursor = cnx.cursor()
query = (f'INSERT INTO `Colleges` VALUES (NULL, "{college}", "{students}, NULL, NULL, NULL)')

cursor.execute(query)

H = ('SELECT * FROM Colleges')
cursor.execute(H)

# print
for row in cursor.fetchall():
    print(row)

cnx.commit()
cursor.close()
cnx.close()