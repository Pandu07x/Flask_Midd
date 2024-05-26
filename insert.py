import psycopg2
from datetime import datetime




def insertlogs(request,user):
    try:
        client = psycopg2.connect(database="Test", user="postgres", password="12345678", host="localhost", port="5432")
        client.autocommit = True
        cursor = client.cursor()
        dates=datetime.now()
        query = f'INSERT INTO public.logs( user_id, path, ip, method, start_timestamp, session)VALUES (%s, %s, %s, %s, %s, %s);'
        values = (user, request.path, request.remote_addr, request.method,dates , request.cookies["session"])
        print(values,datetime.now())
        cursor.execute(query, values)
        getquery='select id from logs where user_id=%s and start_timestamp=%s'
        getvalues=(user,dates)
        cursor.execute(getquery,getvalues)
        data=cursor.fetchall()
        return data[0]
    except Exception as e:
        print(e,"Exception")

def updatelogs(id):
    client = psycopg2.connect(database="Test", user="postgres", password="12345678", host="localhost", port="5432")
    client.autocommit = True
    cursor = client.cursor()
    dates = datetime.now()
    query='update logs set end_timestamp=%s where id=%s'
    values=(dates,id)
    cursor.execute(query,values)

