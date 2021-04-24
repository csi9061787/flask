import pymysql
#函數可以直接呼叫,用作於把資料庫裡的資料回傳
def getStaff():
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = '7871609'
    db = 'TESTDB'
    charset = 'utf8mb4'

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor()

    sql = """
    SELECT ID, Name, DeptId, Age, Gender, Salary FROM Staff;
    """
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

if __name__ == '__main__':
    for r in getStaff():
        print(r)