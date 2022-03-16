import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mynewpass",
  database = "attendance_project"
)
mycursor = mydb.cursor()
# print(datetime.now().strftime("%Y-%m-%d"))
print(date.today())
DOA = str(date.today())
# get_attendance = f"""Select * From attendance where DOA = \'{date_today}\' """
# print(get_attendance)
frame_current_name = "Ayush"
insert_sql = "INSERT INTO attendance(Name,DOA) VALUES (%s, %s)"

mycursor.execute(insert_sql, (frame_current_name,DOA))

mydb.commit()
mydb.close()
# mycursor.execute(get_attendance)

# myresult = mycursor.fetchall()
# print(myresult)
# for x in myresult:
#   print(x)