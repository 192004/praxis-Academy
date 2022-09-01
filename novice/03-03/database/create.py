try:
    import psycopg2
    conn = psycopg2.connect(
    host="localhost",
    database="contoh",
    user="postgres",
    password="fitri19")
    curs = conn.cursor()

    nama = "anggang"
    umur = 24
    query = f"insert into siswa(nama, umur) values'{nama}', {umur}"

    curs.execute(query)
    conn.commit()
    print("data berhasil diupdate")
except Exception:
    pass 