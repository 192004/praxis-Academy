from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="inventaris",
        user="postgres",
        password="fitri19"
    )

    curs = conn.cursor()
    if request.method == "POST":
        nama_barang = request.form.get("nama_barang")
        jumlah_barang = request.form.get("jumlah_barang")
        kode_barang = request.form.get("kode_barang")
        keterangan = request.form.get("keterangan")
        detail = request.form.get("detail")
        query = f"insert into inventaris(nama_barang, jumlah_barang, kode_barang, keterangan) values ('{nama_barang}','{jumlah_barang}', '{kode_barang}', '{keterangan}')"
        curs.execute(query)
        conn.commit() 
        curs.close()
        conn.close()  

    print(request.method)
    query = f"select * from inventaris"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)

@app.route("/detail/<inventaris_id>")
def detail(inventaris_id):
    conn = psycopg2.connect(
        host="localhost",
        database="inventaris",
        user="postgres",
        password="fitri19"
    )
    curs = conn.cursor()
    query = f"select * from inventaris where id = {inventaris_id}"
    curs.execute(query)
    data = curs.fetchone()
    conn.commit()        
    curs.close()
    conn.close()
    print (data)
    return render_template("detail.html", context=data)

@app.route("/delete/<inventaris_id>")
def delete(inventaris_id):
    conn = psycopg2.connect(
        host="localhost",
        database="inventaris",
        user="postgres",
        password="fitri19"
    )
    curs = conn.cursor()
    query = f"delete from inventaris where id = {inventaris_id}"
    curs.execute(query)
    conn.commit()        
    curs.close()
    conn.close()
    return redirect ("/")

@app.route("/update/<inventaris_id>" ,methods=["GET", "POST"])
def update(inventaris_id):
    conn = psycopg2.connect(
        host="localhost",
        database="inventaris",
        user="postgres",
        password="fitri19"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama_barang = request.form.get("nama_barang")
        jumlah_barang = request.form.get("jumlah_barang")
        kode_barang= request.form.get("kode_barang")
        keterangan = request.form.get("keterangan")
        query = f"insert into inventaris(nama_barang, jumlah_barang, kode_barang, keterangan) values ('{nama_barang}','{jumlah_barang}', '{kode_barang}', '{keterangan}')"
        curs.execute(query)
        conn.commit()   
        return redirect("/")
   
    query = f"select * from inventaris"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)
    


if __name__ == "__main__":
    app.run()
  
       

    