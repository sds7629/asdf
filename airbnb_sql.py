import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Rlawlsdn1573!",
    db="airbnb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

with connection.cursor() as cursor:
    sql = "insert into products(productName, price, stockQuantity) values (%s, %s, %s)"
    cursor.execute(sql, ("Python Book", 10000, 10))
    connection.commit()

    cursor.execute("select * from products")
    for book in cursor.fetchall():
        print(book)

    sql = "update products set stockQuantity = stockQuantity - %s where pk = %s"
    cursor.execute(sql, (1, 1))
    connection.commit()

    sql = "select customerID, sum(totalAmount) as totalAmount from orders group by customerID"
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(datas)

    "new "

    cursor.close()
