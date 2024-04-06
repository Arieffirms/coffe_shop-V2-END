import mysql.connector as connector
from datetime import datetime, timedelta
import random
import string

def koneksi():
        mydb = connector.connect(
            host="localhost",
            user="root",
            password="",
            database="coffe_shop"
        )
        return mydb
    
def series_pembayaran():
    prefix = 'RCO'
    random_part = ''.join(random.choices(string.digits, k=4))
    return prefix + random_part

def id_uniq():
    prefix = 'KRYW'
    random_part = ''.join(random.choices(string.digits, k=6))
    return prefix + random_part


def cek_penjualan():
        db.cursor()
        cursor.execute("SELECT id,nama,nama_pesanan FROM add_chart")
        result = cursor.fetchall()
        for row in result:
            print(row)
            
def register(cursor,id,nama,username,password):
    sql = "INSERT INTO user_karyawan (id,nama,username,password) VALUES (%s,%s,%s,%s)"
    var = (id,nama,username,password)
    cursor.execute(sql,var)
    db.commit()
    print("Data telah di tambah")
    
def login(cursor, username, password):
    cursor.execute("SELECT * FROM user_karyawan WHERE username=%s AND password=%s", (username, password))
    hasil = cursor.fetchall()
    if hasil:
        return True
    else:
        return False


def add_chart_matcha_latte(self):
    mydb = koneksi()
    nama_pembeli = input("Masukkan nama pembeli: ")
    quantity = int(input("Quantity: "))
    pesanan = "Matcha Latte"

    if not nama_pembeli or not quantity:
        print("Mohon isi Nama customer dan pesanannya")
    else:
        mycursor = mydb.cursor()

        mycursor.execute("SELECT stock, harga, waktu_restock FROM stock_barang WHERE nama_barang = %s", (pesanan,))
        result = mycursor.fetchone()
        if result:
            stock, harga, restock_time = result  

            if quantity > stock:
                print("Maaf, stock untuk Matcha Latte habis.")
                return

            new_stock = stock - quantity
            restock_time = datetime.now() + timedelta(days=7)

            total_harga = quantity * harga

            sql_insert = "INSERT INTO add_chart (`id`, `nama`, `nama_pesanan`, `quantity`, `harga`, `total_harga`) VALUES (%s, %s, %s, %s, %s, %s)"
            id_unik = series_pembayaran()
            val = (id_unik, nama_pembeli, pesanan, quantity, harga, total_harga)

            try:
                mycursor.execute(sql_insert, val)
                mydb.commit()

                sql_update_stock = "UPDATE stock_barang SET stock = %s, waktu_restock = %s WHERE nama_barang = %s"
                val_update_stock = (new_stock, restock_time, pesanan)
                mycursor.execute(sql_update_stock, val_update_stock)
                mydb.commit()

                print("Pesanan Anda telah diterima. Mohon ditunggu")
            except Exception as e:
                print("Error", f"Terjadi kesalahan: {str(e)}")
        else:
            print("Error", "Produk tidak ditemukan dalam stock.")


def cek_stok_barang(cursor):
    cursor.execute("SELECT nama_barang, stock FROM stock_barang")
    results = cursor.fetchall()
    if results:
        print("======== Stok Barang =======")
        for row in results:
            print(row)
        print("============================")
    else:
        print("Tidak ada data stock barang.")


def result_penjualan(cursor):
    cursor.execute("SELECT * FROM result_penjualan")
    results = cursor.fetchall()
    if results:
        print("======== hasil penjualan =======")
        for row in results:
            print(row)
        print("============================")
    else:
        print("Tidak ada data stock barang.")


def move_data_to_home():
        mydb = connector.connect(
                host="localhost",
                user="root",
                password="",
                database="coffe_shop"
            )
        mycursor = mydb.cursor()

        try:
            sql_move_data = """
            INSERT IGNORE INTO result_penjualan (id, nama, nama_pesanan, quantity, harga, total_harga)
            SELECT `id`, `nama`, `nama_pesanan`, `quantity`, `harga`, `total_harga` FROM add_chart
            """
            mycursor.execute(sql_move_data)
            mydb.commit()

            if mycursor.rowcount == 0:
                print("Tidak ada data untuk dipindahkan.")
            else:
                print("Data berhasil dipindahkan ke tabel home.")
        except connector.Error as err:
                print(f"Gagal memindahkan data: {err}")

        mycursor.close()
        mydb.close()



db = konesi()
cursor = db.cursor()


menu_utama = True 
while True:
    if menu_utama:
        print("1. Login")
        print("2. Registrasi Pengguna")
        print("3. Keluar")
        menu = input("Masukkan Nomor menu: ")

        if menu == "1":
            while True: 
                print("======================")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                if login(cursor, username, password):
                    print("============ Selamat datang di Dashboard ==============")
                    menu_utama = False 
                    break
                else:
                    print("Login gagal. Silakan coba lagi.")
        
        elif menu == "2":
            id = id_uniq()
            nama = input("Masukkan nama: ")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            register(cursor, id, nama, username, password) 
        elif menu == "3":
            break  
    else: 
        print("======================")
        print("Pilih Menu Minuman")
        print("1. Matcha Latte")
        print("2. Red Valved")
        print("3. add chart")
        print("4. Cek Stok Barang")
        print("5. result Penjualan")
        print("6. Log-out")
        print("======================")
        menu_minuman = input("Masukkan Nomor menu: ")
        if menu_minuman == "1":
            add_chart_matcha_latte(konesi)
            
        elif menu_minuman == "3":
                cek_penjualan()
                while True:
                    print("1.pindah barang")
                    print("2.keluar")
                    menu_minuman = input("Masukkan Nomor menu: ")
                    
                    if menu_minuman == "1":
                        move_data_to_home()
                    elif menu_minuman == "2":
                        break
        elif menu_minuman == "4":
            cek_stok_barang(cursor)  
            
        elif menu_minuman == "5":
            result_penjualan(cursor)
            
        elif menu_minuman == "6":
            menu_utama = True  

db.close()
cursor.close()

# import random

# # Fungsi untuk menghasilkan NIM mahasiswa dengan panjang 12 digit
# def generate_nim():
#     # Angka untuk tahun masuk, misalnya 20 untuk tahun 2020
#     tahun_masuk = random.randint(10, 30)  # Angka 10-30 sebagai contoh
    
#     # Nomor urut mahasiswa, misalnya 0000001-9999999
#     nomor_urut = random.randint(1, 9999999)
    
#     # Format NIM dengan panjang tepat 12 digit
#     nim = f"{tahun_masuk:02}{nomor_urut:07}"
    
#     return nim

# # Contoh penggunaan
# for _ in range(10):
#     nim = generate_nim()
#     print("NIM Mahasiswa:", nim)
