import pymysql
def mysqlconnect():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        passwd='',

        database="sbibank"
    )
    return conn

con = mysqlconnect()

with con.cursor() as cur:
    sql="Insert into cust_dtl (cust_name,cust_contact,cust_address,cust_acno,cust_ifsc) values (%s,%s,%s,%s,%s)"
    cur.execute(sql,('sonu',8888888,'amoghpur',5454545454,'bnbn66'))

    con.commit()
 

    # To close the connection 
