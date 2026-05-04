import mysql.connector 


def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="singmad_rich"
    )

    cur = conn.cursor()

    return conn,cur

def create_db():
    conn,cur = connection()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sigmald_products2 (
            id SERIAL PRIMARY KEY,
            product_name TEXT,
            description TEXT,
            product_brand TEXT,
            product_number TEXT,
            product_key TEXT,
            material_id JSON,
            price JSON,
            alies JSON,
            descriptions JSON,
            images JSON,
            attributes JSON,
            safty_info JSON,
            status VARCHAR(50) DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
    """)
    conn.commit()
    conn.close()

def pending_file():
    conn,cur = connection()
    cur.execute("""CREATE TABLE IF NOT EXISTS pending_files(
                p_id INT AUTO_INCREMENT PRIMARY KEY,
                p_name VARCHAR(255),
                p_status VARCHAR(255)
                )""")
    conn.commit()
    conn.close()


def insert_pending_data(data):
    conn,cur = connection()
    cur.execute("""INSERT INTO pending_files(p_name,p_status) VALUES(%s,%s)""",(
        data.get('file_name'),
        data.get('status'),
    ))
    conn.commit()
    conn.close()


def insert_data(data):
    query = """INSERT INTO sigmald_products2 (product_name,description,product_brand,product_number,product_key,material_id,price,alies,descriptions,images,attributes,safty_info,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    conn,cur = connection()
    cur.executemany(query,data)
    print('10 Data inserted!')
    conn.commit()
    conn.close()

