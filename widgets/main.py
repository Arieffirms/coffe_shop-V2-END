import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem,QFileDialog
import xlsxwriter
import mysql.connector as connector
import re
import random
import datetime
import string
from datetime import datetime, timedelta
from login import Ui_LoginDashboard

## ======= menentukan serial number dan id ================##
def series_pembayaran():
    prefix = '#RCO'
    random_part = ''.join(random.choices(string.digits, k=4))
    return prefix + random_part

def id_uniq():
    prefix = 'KRYW'
    random_part = ''.join(random.choices(string.digits, k=6))
    return prefix + random_part

def id_member():
    prefix = '#rpsmbr'
    random_part = ''.join(random.choices(string.digits, k=7))
    return prefix + random_part

def koneksi():
    mydb = connector.connect(
            host="localhost",
            user="root",
            password="",
            database="coffe_shop"
        )
    return mydb
# ===========================================================

class LoginScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui =Ui_LoginDashboard()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.stackedWidget_3.hide()
        self.ui.stackedWidget_4.hide()
        self.ui.widget_3.hide()
        self.ui.widget.hide()
        self.ui.widget_2.hide()
        self.ui.pushButton_login.clicked.connect(self.login)
        self.ui.commandLinkButton.clicked.connect(self.daftar_sekarang)

        self.ui.commandLinkButton_9.clicked.connect(self.close_daftar)
        self.ui.home.clicked.connect(self.dashboard_home)
        self.ui.home_2.clicked.connect(self.dashboard_product)
        self.ui.home_4.clicked.connect(self.dashboard_orders)
        self.ui.home_3.clicked.connect(self.dashboard_stock_barang)
        self.ui.home_6.clicked.connect(self.dashboard_member)
        self.ui.commandLinkButton_3.clicked.connect(self.close_menu)
        self.ui.commandLinkButton_4.clicked.connect(self.close_menu)
        self.ui.commandLinkButton_5.clicked.connect(self.close_menu)
        self.ui.commandLinkButton_7.clicked.connect(self.close_menu)
        self.ui.commandLinkButton_8.clicked.connect(self.close_menu)
        self.ui.commandLinkButton_6.clicked.connect(self.close_menu)
        
        self.ui.pushButton_2.clicked.connect(self.view_all_home_results)
        
        self.ui.pushButton_11.clicked.connect(self.add_caffe_mocha)
        self.ui.pushButton_12.clicked.connect(self.add_ice_expresso_matcha_fusion)
        self.ui.pushButton_16.clicked.connect(self.add_caffe_americano)
        self.ui.pushButton_13.clicked.connect(self.add_flat_white)
        self.ui.pushButton_14.clicked.connect(self.add_caramel_macciato)
        self.ui.pushButton_15.clicked.connect(self.add_cappucino)

        
        self.ui.pushButton_17.clicked.connect(self.orders)
        self.ui.pushButton_18.clicked.connect(self.delete_add_chart)
        self.ui.pushButton.clicked.connect(self.result_transaksi)
        self.ui.pushButton_7.clicked.connect(self.add_chart_caffe_mocha)
        self.ui.pushButton_8.clicked.connect(self.add_chart_Iced_Espresso_and_Matcha_Fusion)
        self.ui.pushButton_6.clicked.connect(self.add_chart_Caffe_Americano)
        self.ui.pushButton_10.clicked.connect(self.add_chart_flat_white)
        self.ui.pushButton_9.clicked.connect(self.add_chart_caramel_macchiato)
        self.ui.pushButton_5.clicked.connect(self.add_chart_Cappuccino)
        
        
        
        self.ui.commandLinkButton_19.clicked.connect(self.close_menu_list)
        self.ui.commandLinkButton_20.clicked.connect(self.close_menu_list)
        self.ui.commandLinkButton_21.clicked.connect(self.close_menu_list)
        self.ui.commandLinkButton_22.clicked.connect(self.close_menu_list)
        self.ui.commandLinkButton_23.clicked.connect(self.close_menu_list)
        self.ui.commandLinkButton_24.clicked.connect(self.close_menu_list)

        self.ui.commandLinkButton_2.clicked.connect(self.close_transaksi_qris)
        self.ui.pushButton_20.clicked.connect(self.close_transaksi_qris)
        self.ui.pushButton_19.clicked.connect(self.result_transaksi_qris)
        
        self.ui.commandLinkButton_11.clicked.connect(self.create_member_id)
        self.ui.commandLinkButton_25.clicked.connect(self.close_member_id)
        self.ui.pushButton_27.clicked.connect(self.buat_members)
        self.ui.pushButton_4.clicked.connect(self.cari_member)
        self.ui.pushButton_28.clicked.connect(self.delete_member)
        self.ui.pushButton_29.clicked.connect(self.transaksi_cari_nama_pesanan)
        self.ui.pushButton_3.clicked.connect(self.delete_pesanan_transaksi)
        
        
        
        self.ui.commandLinkButton_10.clicked.connect(self.stock_list_coffe_americano)
        self.ui.commandLinkButton_12.clicked.connect(self.stock_list_cappucino)
        self.ui.commandLinkButton_13.clicked.connect(self.stock_list_caffe_mocha)
        self.ui.commandLinkButton_14.clicked.connect(self.stock_list_caramel_machiato)
        self.ui.commandLinkButton_15.clicked.connect(self.stock_list_flat_white)
        self.ui.commandLinkButton_16.clicked.connect(self.stock_list_iced_expresso)

        
        
        self.ui.pushButton_21.clicked.connect(self.add_stock_coffe_america)
        self.ui.pushButton_22.clicked.connect(self.add_stock_cappuccino)
        self.ui.pushButton_23.clicked.connect(self.add_stock_Caffe_Mocha)
        self.ui.pushButton_24.clicked.connect(self.add_stock_caramel_macchiato)
        self.ui.pushButton_25.clicked.connect(self.add_stock_flat_white)
        self.ui.pushButton_26.clicked.connect(self.add_stock_iced_expresso)
        
        self.ui.pushButton_login_2.clicked.connect(self.daftar_result)
        self.ui.home_5.clicked.connect(self.logout)
        
        self.ui.pushButton_30.clicked.connect(self.printData)
        
      
        
        
        

    def daftar_sekarang(self): 
        self.ui.widget.show() 
        
        
    def login(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        un = self.ui.username.text()
        pw = self.ui.password.text()
        
        if not un or not pw:
            QMessageBox.information(self, "Perhatian!", "Mohon isi username dan password")
        else:
            if not re.match(r"[^@]+@gmail\.com", un):
                QMessageBox.information(self, "Invalid Email!", "Mohon Masukan Alamat Email Yang Valid Dan Password")
                self.ui.username.setText("")
            else:
                mycursor.execute("SELECT nama FROM user_karyawan WHERE username = %s AND password = %s", (un, pw))
                user = mycursor.fetchone()
                if user:
                    nama_pengguna = user[0]
                    QMessageBox.information(self, "Selamat", "Anda Berhasil Login Selamat Bekerja")
                    self.ui.stackedWidget.setCurrentIndex(1)
                    self.ui.label_20.setText(un)
                    self.ui.label_19.setText(nama_pengguna)
                else:       
                    QMessageBox.information(self, "Invalid User", "Username dan Password anda Salah Atau Belum Terdaftar")
                    self.ui.username.setText("")
                    self.ui.password.setText("")
        mydb.close()
        mycursor.close()
        
    def daftar_sekarang(self):
        self.ui.widget.show()
        
    def close_daftar(self):
        self.ui.widget.close()
        
    def daftar_result(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        nama = self.ui.username_2.text()
        username = self.ui.username_3.text()
        no_tlpn = self.ui.username_4.text()
        password = self.ui.username_5.text()
        confirm_password = self.ui.username_6.text() 
        
        if not nama or not username or not no_tlpn or not password or not confirm_password:
            QMessageBox.information(self, "Invalid Register", "Mohon Masukan semua perintah kolom tidak boleh kosong")
        else:
            if not re.match(r"[^@]+@gmail\.com", username):
                QMessageBox.information(self, "Invalid Email!", "Mohon Masukan Alamat Email yang Valid")
                self.ui.lineEdit_4.setText("")  
            elif password != confirm_password:
                QMessageBox.information(self, "Password Mismatch!", "Konfirmasi password tidak cocok dengan password")
                self.ui.username_5.setText("")  
                self.ui.username_6.setText("") 
            else:
                sql = "INSERT INTO user_karyawan (id, nama, username, no_tlp, password) VALUES (%s, %s, %s, %s,%s)"
                id = id_uniq()
                val = (id, nama, username, no_tlpn, password)
                mycursor.execute(sql, val)
                mydb.commit()
                QMessageBox.information(self, "Success!", "Registrasi berhasil.")
                self.ui.widget.close()
        
        mycursor.close()
        mydb.close()

        
        

    def dashboard_home(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
    
    
    def dashboard_product(self):
        self.ui.stackedWidget_2.setCurrentIndex(3)
        
        
    def dashboard_orders(self):
        self.ui.stackedWidget_2.setCurrentIndex(4)
        
        
    def dashboard_stock_barang(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
 
 
    def dashboard_member(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)
        mydb = koneksi()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM customer_member")

        self.ui.tableWidget_4.setRowCount(0)

        rows = mycursor.fetchall()  

        if not rows:  
            QMessageBox.information(self, "Informasi", "Tidak Ada member")
        else:
            for row_data in rows:
                row_number = self.ui.tableWidget_4.rowCount()
                self.ui.tableWidget_4.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.ui.tableWidget_4.setItem(row_number, column_number, item)

        mycursor.close()
        
        
    def buat_members(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        nama = self.ui.username_14.text()
        
        if not nama:
            QMessageBox.warning(self, "Perhatian", "Masukan Nama Pada Colom")
        else:
            sql = "INSERT INTO customer_member (id_member, nama ) VALUES (%s,%s)"
            id = id_member()
            val = (id, nama)
            mycursor.execute(sql, val)
            mydb.commit()
            QMessageBox.information(self, "Success!", "berhasil membuat Id Member.")
            self.ui.widget_3.close()
            
        
    def cari_member(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        nama = self.ui.username_13.text()

        sql = "SELECT * FROM customer_member WHERE nama LIKE %s"
        mycursor.execute(sql, ("%" + nama + "%",))  
        results = mycursor.fetchall()
        self.ui.tableWidget_4.setRowCount(0)

        if results:  
            for row_number, row_data in enumerate(results):
                self.ui.tableWidget_4.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.ui.tableWidget_4.setItem(row_number, column_number, item)
        else:  
            QMessageBox.warning(self, "Perhatian", f"Tidak ditemukan data untuk {nama}.")

        mycursor.close()
        
    def delete_member(self):
        nama = self.ui.username_13.text()

        confirm = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menghapus member dengan nama {nama}?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            mydb = koneksi()
            mycursor = mydb.cursor()
            sql = "DELETE FROM customer_member WHERE nama LIKE %s"
            mycursor.execute(sql, ("%" + nama + "%",)) 
            mydb.commit()
            QMessageBox.information(self, "Informasi", f"Member dengan nama {nama} telah dihapus.")
            mycursor.close()
            self.ui.username_13.clear()
        else:
            QMessageBox.information(self, "Informasi", "Penghapusan dibatalkan.")
 
        
    def view_all_home_results(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM transaksi")
        self.ui.tableWidget.setRowCount(0)
        rows = mycursor.fetchall()  
        if not rows:  
            message = "Tidak ada transaksi saat ini."
            QMessageBox.information(self, "Informasi", message)
        else:
            for row_data in rows:
                self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())  # Menambahkan satu baris baru
                for col, field in enumerate(row_data):
                    self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, col, QTableWidgetItem(str(field)))
                    
                    
                    
        mycursor.execute("SELECT total_harga FROM transaksi")
        totals = mycursor.fetchall()
        total_price = 0
        for total in totals:
            total_price += total[0]
        self.ui.label_22.setText(f"{total_price} Rupiah")
        
        
        mycursor.execute("SELECT COUNT(*) FROM user_karyawan")
        hasil = mycursor.fetchone()
        jumlah_pengguna = hasil[0]
        self.ui.label_21.setText(f"{jumlah_pengguna} Person")
        
        
        mycursor.execute("SELECT quantity FROM transaksi")
        hasil_penjualan = mycursor.fetchall()
        total_transaksi = 0

        for transaksi in hasil_penjualan:
            total_transaksi += transaksi[0]

        self.ui.label_23.setText(f"{total_transaksi} Pesanan Terjual")
        mycursor.close()
        mydb.close()
    
    
    def transaksi_cari_nama_pesanan(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        nama = self.ui.username_15.text()

        sql = "SELECT * FROM transaksi WHERE nama_pesanan LIKE %s"
        mycursor.execute(sql, ("%" + nama + "%",))  
        results = mycursor.fetchall()
        self.ui.tableWidget.setRowCount(0)

        if results:  
            for row_number, row_data in enumerate(results):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.ui.tableWidget.setItem(row_number, column_number, item)
        else:  
            QMessageBox.warning(self, "Perhatian", f"Tidak ditemukan data untuk {nama}.")

        mycursor.close()
        
    def delete_pesanan_transaksi(self):
        id = self.ui.username_15.text()

        if not id:
            QMessageBox.warning(self, "Perhatian", "Anda wajib Memasukan id pada penghapusan!")
        else:
            confirm = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menghapus member dengan id {id}?", QMessageBox.Yes | QMessageBox.No)

            if confirm == QMessageBox.Yes:
                mydb = koneksi()
                mycursor = mydb.cursor()

                check_sql = "SELECT COUNT(*) FROM transaksi WHERE id LIKE %s"
                mycursor.execute(check_sql, ("%" + id + "%",))
                count = mycursor.fetchone()[0]

                if count == 0:
                    QMessageBox.warning(self, "Perhatian", f"Member dengan id {id} tidak ditemukan.")
                else:
                    sql = "DELETE FROM transaksi WHERE id LIKE %s"
                    mycursor.execute(sql, ("%" + id + "%",))
                    mydb.commit()
                    QMessageBox.information(self, "Informasi", f"Member dengan id {id} telah dihapus.")
                    self.ui.tableWidget.removeRow(0)
                    self.ui.username_15.clear()

                mycursor.close()
            else:
                QMessageBox.information(self, "Informasi", "Penghapusan dibatalkan.")


    def close_menu(self):
        self.ui.stackedWidget_3.close()
        
    
    def add_caffe_mocha(self):
        self.ui.stackedWidget_3.show()
        self.ui.stackedWidget_3.setCurrentIndex(2)
        nama_barang = "Caffe Mocha"
        
        mydb = koneksi()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT stock FROM menu WHERE nama_barang = %s", (nama_barang,)) 
        stock_barang = mycursor.fetchone()
        self.ui.label_61.setText(f"{stock_barang[0]}") 
        mycursor.close()

    
    def add_ice_expresso_matcha_fusion(self):
        self.ui.stackedWidget_3.show()
        self.ui.stackedWidget_3.setCurrentIndex(4)
        nama_barang = "Iced Espresso and Matcha Fusion"
        
        mydb = koneksi()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT stock FROM menu WHERE nama_barang = %s", (nama_barang,)) 
        stock_barang = mycursor.fetchone()
        self.ui.label_65.setText(f"{stock_barang[0]}") 
        mycursor.close()

    def add_caffe_americano(self):
        self.ui.stackedWidget_3.show()
        self.ui.stackedWidget_3.setCurrentIndex(0)
        nama_barang = "Caffe Americano"
        
        mydb = koneksi()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT stock FROM menu WHERE nama_barang = %s", (nama_barang,)) 
        stock_barang = mycursor.fetchone()
        self.ui.label_69.setText(f"{stock_barang[0]}") 
        mycursor.close()
    
    
    def add_flat_white(self):
        self.ui.stackedWidget_3.show()
        self.ui.stackedWidget_3.setCurrentIndex(5)
        nama_barang = "Flat White"
        
        mydb = koneksi()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT stock FROM menu WHERE nama_barang = %s", (nama_barang,)) 
        stock_barang = mycursor.fetchone()
        self.ui.label_67.setText(f"{stock_barang[0]}") 
        mycursor.close()

    def add_caramel_macciato(self):
        self.ui.stackedWidget_3.show()
        self.ui.stackedWidget_3.setCurrentIndex(3)
        nama_barang = "Caramel Macchiato"
        
        mydb = koneksi()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT stock FROM menu WHERE nama_barang = %s", (nama_barang,)) 
        stock_barang = mycursor.fetchone()
        self.ui.label_63.setText(f"{stock_barang[0]}") 
        mycursor.close()
    
    def add_cappucino(self):
        self.ui.stackedWidget_3.show()
        self.ui.stackedWidget_3.setCurrentIndex(1)
        nama_barang = "Cappuccino"
        
        mydb = koneksi()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT stock FROM menu WHERE nama_barang = %s", (nama_barang,)) 
        stock_barang = mycursor.fetchone()
        self.ui.label_71.setText(f"{stock_barang[0]}") 
        mycursor.close()
        

    def orders(self):
        mydb = koneksi()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM pesanan")

        self.ui.tableWidget_3.setRowCount(0)

        total_price = 0

        rows = mycursor.fetchall() 

        if not rows:  # Jika tabel pesanan kosong
            message = "Tidak ada pesanan saat ini."
            QMessageBox.information(self, "Informasi", message)
        else:
            for row_data in rows:
                self.ui.tableWidget_3.insertRow(self.ui.tableWidget_3.rowCount())  # Menambahkan satu baris baru
                for col, field in enumerate(row_data):
                    self.ui.tableWidget_3.setItem(self.ui.tableWidget_3.rowCount() - 1, col, QTableWidgetItem(str(field)))
                total_price += row_data[6]  # Mengambil total harga dari data pesanan

            message = f"{total_price} Rupiah"

            self.ui.listWidget.clear()
            self.ui.listWidget.addItem(message)

        mycursor.close()
        mydb.close()

    def result_transaksi(self):
        try:
            mydb = koneksi()
            mycursor = mydb.cursor()
            metode_pembayaran = self.ui.comboBox.currentText() 
            uang_customer = self.ui.lineEdit_14.text()

            if metode_pembayaran == "CASH":
                if not uang_customer:
                    QMessageBox.warning(self, "Peringatan", "Mohon masukkan jumlah uang yang diberikan.")
                    return

                try:
                    uang_customer = int(uang_customer)
                    if uang_customer <= 0:
                        raise ValueError
                except ValueError:
                    QMessageBox.warning(self, "Peringatan", "Jumlah uang harus berupa angka positif.")
                    return

                total_harga = 0
                pesanan_query = "SELECT id_member, total_harga FROM pesanan"
                mycursor.execute(pesanan_query)
                for id_member, harga in mycursor.fetchall():
                    total_harga += harga

                    nama = ""
                    cari_nama_query = "SELECT nama FROM customer_member WHERE id_member = %s"
                    mycursor.execute(cari_nama_query, (id_member,))
                    result = mycursor.fetchone()
                    if result:
                        nama = result[0]

                if total_harga == 0:
                    QMessageBox.warning(self, "Peringatan", "Tidak ada pesanan untuk diproses.")
                    return

                if uang_customer < total_harga:
                    QMessageBox.warning(self, "Peringatan", "Jumlah uang harus lebih atau pas.")
                    return

                transaksi = """
                INSERT IGNORE INTO transaksi (id, id_member, nama_pesanan, quantity, harga, total_harga, metode_pembayaran, uang_customer, kembalian, diskon, nama)
                SELECT id, id_member, nama_pesanan, quantity, harga, total_harga, %s, %s, %s, diskon, %s
                FROM pesanan
                """
                val = (metode_pembayaran, uang_customer, uang_customer - total_harga, nama)
                mycursor.execute(transaksi, val)
                mydb.commit()

                if mycursor.rowcount == 0:
                    QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk dipindahkan.")
                else:
                    delete_query = "DELETE FROM pesanan"
                    mycursor.execute(delete_query)
                    mydb.commit()
                    self.ui.listWidget.clear()
                    self.ui.tableWidget_3.setRowCount(0)
                    QMessageBox.information(self, "Info", "Data berhasil dipindahkan ke tabel transaksi.")
            
            elif metode_pembayaran == "QRIS":
                self.ui.widget_2.show()
                mycursor.execute("SELECT SUM(total_harga) FROM pesanan")
                total_harga_semua = mycursor.fetchone()[0]
                self.ui.label_73.setText(f"{total_harga_semua}")

                mycursor.execute("SELECT SUM(quantity) FROM pesanan")
                total_quantity = mycursor.fetchone()[0]
                self.ui.label_72.setText(f"{total_quantity}")
                mycursor.close()

        finally:
            mycursor.close()
            mydb.close()

            
    
    def result_transaksi_qris(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        try:
                    metode_pembayaran = "QRIS"
                    total_harga = 0
                    pesanan_query = "SELECT id_member, total_harga FROM pesanan"
                    mycursor.execute(pesanan_query)
                    rows = mycursor.fetchall()

                    if not rows:
                        QMessageBox.warning(self, "Info", "Tidak ada pesanan yang tersedia untuk diproses.")
                    else:
                        for id_member, harga in rows:
                            total_harga += harga 

                            
                            nama = ""
                            cari_nama_query = "SELECT nama FROM customer_member WHERE id_member = %s"
                            mycursor.execute(cari_nama_query, (id_member,))
                            result = mycursor.fetchone()
                            if result:
                                nama = result[0]

                            # Menyisipkan transaksi ke dalam tabel transaksi
                            transaksi = """
                            INSERT IGNORE INTO transaksi (id, id_member, nama_pesanan, quantity, harga, total_harga, metode_pembayaran, uang_customer, kembalian, diskon, nama)
                            SELECT id, %s, nama_pesanan, quantity, harga, total_harga, %s, %s, 0, diskon, %s
                            FROM pesanan
                            """
                            val = (id_member, metode_pembayaran, total_harga, nama)
                            mycursor.execute(transaksi, val)
                        
                        mydb.commit()
                        if mycursor.rowcount == 0:
                            QMessageBox.warning(self, "Info", "Data sudah ada di tabel transaksi.")
                        else:
                            delete_query = "DELETE FROM pesanan"
                            mycursor.execute(delete_query)
                            mydb.commit()
                            self.ui.listWidget.clear()
                            self.ui.tableWidget_3.setRowCount(0)
                            QMessageBox.information(self, "Info", "Data berhasil dipindahkan ke tabel transaksi.")
                            self.ui.widget_2.hide()
        except connector.Error as err:
            QMessageBox.warning(self, "Peringatan", f"Gagal memindahkan data: {err}")    


    def delete_add_chart(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        
        reply = QMessageBox.question(self, 'Konfirmasi', 'Apakah Anda yakin ingin menghapus pesanan pertama?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                sql = "DELETE FROM pesanan ORDER BY id LIMIT 1"
                mycursor.execute(sql)
                mydb.commit()
                
                if mycursor.rowcount == 0: 
                    QMessageBox.warning(self, "Peringatan", "Tidak ada pesanan yang tersedia.")
                else:
                    self.ui.tableWidget_3.removeRow(0)
                    self.ui.listWidget.clear()
                    QMessageBox.information(self, "Info", "Pesanan pertama telah dihapus.")
            except mycursor.Error as err:
                QMessageBox.warning(self, "Peringatan", f"Gagal menghapus baris: {err}")
        else:
            QMessageBox.information(self, "Info", "Penghapusan pesanan dibatalkan.")
        mycursor.close()
        mydb.close()
        
        

    def add_chart_caffe_mocha(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        member_id = self.ui.lineEdit_5.text()
        quantity = self.ui.lineEdit_7.text() 
        nama_pesanan = "Caffe Mocha"

        if not quantity:
            QMessageBox.information(self, "ATTENTION!", "Mohon isi kolom quantity-nya")
            return
        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "ATTENTION!", "Quantity harus berupa angka")
            self.ui.lineEdit_7.setText("") 
            return

        mycursor.execute("SELECT stock, harga, waktu_restock FROM menu WHERE nama_barang = %s", (nama_pesanan,))
        result = mycursor.fetchone()
        if result:
            stock, harga, waktu_restock = result
            stock = int(stock)  
            
            if quantity > stock:
                QMessageBox.warning(self, "ATTENTION!", f"Stock {nama_pesanan} Telah Habis")
                return

            total_harga = quantity * harga
            diskon = 0

            if member_id:
                mycursor.execute("SELECT * FROM customer_member WHERE id_member = %s", (member_id,))
                if not mycursor.fetchone():
                    QMessageBox.warning(self, "ATTENTION!", "ID member tidak ada di data dan mungkin belum mendaftarnya.")
                    return
                else:
                    diskon = 0.1

            potongan_harga = total_harga * diskon

            total_harga -= potongan_harga

            new_stock = stock - quantity
            restock_time = datetime.now() + timedelta(days=7)
            
            sql_insert_pesanan = "INSERT INTO pesanan (id, id_member ,nama_pesanan, quantity, harga, total_harga, diskon) VALUES (%s,%s,%s, %s, %s, %s,%s)"    
            id_pesanan = series_pembayaran()
            val_pesanan = (id_pesanan, member_id, nama_pesanan, quantity, harga, total_harga, potongan_harga)
            mycursor.execute(sql_insert_pesanan, val_pesanan)
            mydb.commit()
            sql_update = "UPDATE menu SET stock = %s, waktu_restock = %s WHERE nama_barang = %s"
            val_update_stock = (new_stock, restock_time, nama_pesanan)
            mycursor.execute(sql_update, val_update_stock)
            mydb.commit()
            
            QMessageBox.information(self, "Success", f"Pesanan {nama_pesanan} telah ditambahkan ke daftar pesanan sebanyak {quantity}.")
            self.ui.stackedWidget_3.hide()
        else:
            QMessageBox.warning(self, "ATTENTION!", "Produk tidak ditemukan dalam stock.")
        

        mycursor.close()
        mydb.close()

    def add_chart_Iced_Espresso_and_Matcha_Fusion(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        member_id = self.ui.lineEdit_9.text()
        quantity = self.ui.lineEdit_8.text() 
        nama_pesanan = "Iced Espresso and Matcha Fusion"

        if not quantity:
            QMessageBox.information(self, "ATTENTION!", "Mohon isi kolom quantity-nya")
            return
        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "ATTENTION!", "Quantity harus berupa angka")
            self.ui.lineEdit_7.setText("") 
            return

        mycursor.execute("SELECT stock, harga, waktu_restock FROM menu WHERE nama_barang = %s", (nama_pesanan,))
        result = mycursor.fetchone()
        if result:
            stock, harga, waktu_restock = result
            stock = int(stock)  
            
            if quantity > stock:
                QMessageBox.warning(self, "ATTENTION!", f"Stock {nama_pesanan} Telah Habis")
                return

            total_harga = quantity * harga
            diskon = 0

            if member_id:
                mycursor.execute("SELECT * FROM customer_member WHERE id_member = %s", (member_id,))
                if not mycursor.fetchone():
                    QMessageBox.warning(self, "ATTENTION!", "ID member tidak ada di data dan mungkin belum mendaftarnya.")
                    return
                else:
                    diskon = 0.1

            potongan_harga = total_harga * diskon

            total_harga -= potongan_harga

            new_stock = stock - quantity
            restock_time = datetime.now() + timedelta(days=7)
            
            sql_insert_pesanan = "INSERT INTO pesanan (id, id_member ,nama_pesanan, quantity, harga, total_harga, diskon) VALUES (%s,%s,%s, %s, %s, %s,%s)"    
            id_pesanan = series_pembayaran()
            val_pesanan = (id_pesanan, member_id, nama_pesanan, quantity, harga, total_harga, potongan_harga)
            mycursor.execute(sql_insert_pesanan, val_pesanan)
            mydb.commit()
            sql_update = "UPDATE menu SET stock = %s, waktu_restock = %s WHERE nama_barang = %s"
            val_update_stock = (new_stock, restock_time, nama_pesanan)
            mycursor.execute(sql_update, val_update_stock)
            mydb.commit()
            
            QMessageBox.information(self, "Success", f"Pesanan {nama_pesanan} telah ditambahkan ke daftar pesanan sebanyak {quantity}.")
            self.ui.stackedWidget_3.hide()
        else:
            QMessageBox.warning(self, "ATTENTION!", "Produk tidak ditemukan dalam stock.")
        

        mycursor.close()
        mydb.close()


    def add_chart_Caffe_Americano(self):

        mydb = koneksi()
        mycursor = mydb.cursor()
        member_id = self.ui.lineEdit.text()
        quantity = self.ui.lineEdit_3.text() 
        nama_pesanan = "Caffe Americano"

        if not quantity:
            QMessageBox.information(self, "ATTENTION!", "Mohon isi kolom quantity-nya")
            return
        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "ATTENTION!", "Quantity harus berupa angka")
            self.ui.lineEdit_7.setText("") 
            return

        mycursor.execute("SELECT stock, harga, waktu_restock FROM menu WHERE nama_barang = %s", (nama_pesanan,))
        result = mycursor.fetchone()
        if result:
            stock, harga, waktu_restock = result
            stock = int(stock)  
            
            if quantity > stock:
                QMessageBox.warning(self, "ATTENTION!", f"Stock {nama_pesanan} Telah Habis")
                return

            total_harga = quantity * harga
            diskon = 0

            if member_id:
                mycursor.execute("SELECT * FROM customer_member WHERE id_member = %s", (member_id,))
                if not mycursor.fetchone():
                    QMessageBox.warning(self, "ATTENTION!", "ID member tidak ada di data dan mungkin belum mendaftarnya.")
                    return
                else:
                    diskon = 0.1

            potongan_harga = total_harga * diskon

            total_harga -= potongan_harga

            new_stock = stock - quantity
            restock_time = datetime.now() + timedelta(days=7)
            
            sql_insert_pesanan = "INSERT INTO pesanan (id, id_member ,nama_pesanan, quantity, harga, total_harga, diskon) VALUES (%s,%s,%s, %s, %s, %s,%s)"    
            id_pesanan = series_pembayaran()
            val_pesanan = (id_pesanan, member_id, nama_pesanan, quantity, harga, total_harga, potongan_harga)
            mycursor.execute(sql_insert_pesanan, val_pesanan)
            mydb.commit()
            sql_update = "UPDATE menu SET stock = %s, waktu_restock = %s WHERE nama_barang = %s"
            val_update_stock = (new_stock, restock_time, nama_pesanan)
            mycursor.execute(sql_update, val_update_stock)
            mydb.commit()
            
            QMessageBox.information(self, "Success", f"Pesanan {nama_pesanan} telah ditambahkan ke daftar pesanan sebanyak {quantity}.")
            self.ui.stackedWidget_3.hide()
        else:
            QMessageBox.warning(self, "ATTENTION!", "Produk tidak ditemukan dalam stock.")
        

        mycursor.close()
        mydb.close()

    def add_chart_flat_white(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        member_id = self.ui.lineEdit_12.text()
        quantity = self.ui.lineEdit_13.text() 
        nama_pesanan = "Flat White"

        if not quantity:
            QMessageBox.information(self, "ATTENTION!", "Mohon isi kolom quantity-nya")
            return
        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "ATTENTION!", "Quantity harus berupa angka")
            self.ui.lineEdit_7.setText("") 
            return

        mycursor.execute("SELECT stock, harga, waktu_restock FROM menu WHERE nama_barang = %s", (nama_pesanan,))
        result = mycursor.fetchone()
        if result:
            stock, harga, waktu_restock = result
            stock = int(stock)  
            
            if quantity > stock:
                QMessageBox.warning(self, "ATTENTION!", f"Stock {nama_pesanan} Telah Habis")
                return

            total_harga = quantity * harga
            diskon = 0

            if member_id:
                mycursor.execute("SELECT * FROM customer_member WHERE id_member = %s", (member_id,))
                if not mycursor.fetchone():
                    QMessageBox.warning(self, "ATTENTION!", "ID member tidak ada di data dan mungkin belum mendaftarnya.")
                    return
                else:
                    diskon = 0.1

            potongan_harga = total_harga * diskon

            total_harga -= potongan_harga

            new_stock = stock - quantity
            restock_time = datetime.now() + timedelta(days=7)
            
            sql_insert_pesanan = "INSERT INTO pesanan (id, id_member ,nama_pesanan, quantity, harga, total_harga, diskon) VALUES (%s,%s,%s, %s, %s, %s,%s)"    
            id_pesanan = series_pembayaran()
            val_pesanan = (id_pesanan, member_id, nama_pesanan, quantity, harga, total_harga, potongan_harga)
            mycursor.execute(sql_insert_pesanan, val_pesanan)
            mydb.commit()
            sql_update = "UPDATE menu SET stock = %s, waktu_restock = %s WHERE nama_barang = %s"
            val_update_stock = (new_stock, restock_time, nama_pesanan)
            mycursor.execute(sql_update, val_update_stock)
            mydb.commit()
            
            QMessageBox.information(self, "Success", f"Pesanan {nama_pesanan} telah ditambahkan ke daftar pesanan sebanyak {quantity}.")
            self.ui.stackedWidget_3.hide()
        else:
            QMessageBox.warning(self, "ATTENTION!", "Produk tidak ditemukan dalam stock.")
        

        mycursor.close()
        mydb.close()


    def add_chart_caramel_macchiato(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        member_id = self.ui.lineEdit_11.text()
        quantity = self.ui.lineEdit_10.text() 
        nama_pesanan = "Caramel Macchiato"

        if not quantity:
            QMessageBox.information(self, "ATTENTION!", "Mohon isi kolom quantity-nya")
            return
        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "ATTENTION!", "Quantity harus berupa angka")
            self.ui.lineEdit_7.setText("") 
            return

        mycursor.execute("SELECT stock, harga, waktu_restock FROM menu WHERE nama_barang = %s", (nama_pesanan,))
        result = mycursor.fetchone()
        if result:
            stock, harga, waktu_restock = result
            stock = int(stock)  
            
            if quantity > stock:
                QMessageBox.warning(self, "ATTENTION!", f"Stock {nama_pesanan} Telah Habis")
                return

            total_harga = quantity * harga
            diskon = 0

            if member_id:
                mycursor.execute("SELECT * FROM customer_member WHERE id_member = %s", (member_id,))
                if not mycursor.fetchone():
                    QMessageBox.warning(self, "ATTENTION!", "ID member tidak ada di data dan mungkin belum mendaftarnya.")
                    return
                else:
                    diskon = 0.1

            potongan_harga = total_harga * diskon

            total_harga -= potongan_harga

            new_stock = stock - quantity
            restock_time = datetime.now() + timedelta(days=7)
            
            sql_insert_pesanan = "INSERT INTO pesanan (id, id_member ,nama_pesanan, quantity, harga, total_harga, diskon) VALUES (%s,%s,%s, %s, %s, %s,%s)"    
            id_pesanan = series_pembayaran()
            val_pesanan = (id_pesanan, member_id, nama_pesanan, quantity, harga, total_harga, potongan_harga)
            mycursor.execute(sql_insert_pesanan, val_pesanan)
            mydb.commit()
            sql_update = "UPDATE menu SET stock = %s, waktu_restock = %s WHERE nama_barang = %s"
            val_update_stock = (new_stock, restock_time, nama_pesanan)
            mycursor.execute(sql_update, val_update_stock)
            mydb.commit()
            
            QMessageBox.information(self, "Success", f"Pesanan {nama_pesanan} telah ditambahkan ke daftar pesanan sebanyak {quantity}.")
            self.ui.stackedWidget_3.hide()
        else:
            QMessageBox.warning(self, "ATTENTION!", "Produk tidak ditemukan dalam stock.")
        

        mycursor.close()
        mydb.close()

    def add_chart_Cappuccino(self):
        mydb = koneksi()
        mycursor = mydb.cursor()
        member_id = self.ui.lineEdit_2.text()
        quantity = self.ui.lineEdit_4.text() 
        nama_pesanan = "Cappuccino"

        if not quantity:
            QMessageBox.information(self, "ATTENTION!", "Mohon isi kolom quantity-nya")
            return
        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "ATTENTION!", "Quantity harus berupa angka")
            self.ui.lineEdit_7.setText("") 
            return

        mycursor.execute("SELECT stock, harga, waktu_restock FROM menu WHERE nama_barang = %s", (nama_pesanan,))
        result = mycursor.fetchone()
        if result:
            stock, harga, waktu_restock = result
            stock = int(stock)  
            
            if quantity > stock:
                QMessageBox.warning(self, "ATTENTION!", f"Stock {nama_pesanan} Telah Habis")
                return

            total_harga = quantity * harga
            diskon = 0

            if member_id:
                mycursor.execute("SELECT * FROM customer_member WHERE id_member = %s", (member_id,))
                if not mycursor.fetchone():
                    QMessageBox.warning(self, "ATTENTION!", "ID member tidak ada di data dan mungkin belum mendaftarnya.")
                    return
                else:
                    diskon = 0.1

            potongan_harga = total_harga * diskon

            total_harga -= potongan_harga

            new_stock = stock - quantity
            restock_time = datetime.now() + timedelta(days=7)
            
            sql_insert_pesanan = "INSERT INTO pesanan (id, id_member ,nama_pesanan, quantity, harga, total_harga, diskon) VALUES (%s,%s,%s, %s, %s, %s,%s)"    
            id_pesanan = series_pembayaran()
            val_pesanan = (id_pesanan, member_id, nama_pesanan, quantity, harga, total_harga, potongan_harga)
            mycursor.execute(sql_insert_pesanan, val_pesanan)
            mydb.commit()
            sql_update = "UPDATE menu SET stock = %s, waktu_restock = %s WHERE nama_barang = %s"
            val_update_stock = (new_stock, restock_time, nama_pesanan)
            mycursor.execute(sql_update, val_update_stock)
            mydb.commit()
            
            QMessageBox.information(self, "Success", f"Pesanan {nama_pesanan} telah ditambahkan ke daftar pesanan sebanyak {quantity}.")
            self.ui.stackedWidget_3.hide()
        else:
            QMessageBox.warning(self, "ATTENTION!", "Produk tidak ditemukan dalam stock.")
        

        mycursor.close()
        mydb.close()
 
    def close_menu_list(self):
        self.ui.stackedWidget_4.close()

    def close_transaksi_qris(self):
        self.ui.widget_2.close()

    def stock_list_coffe_americano(self):
        self.ui.stackedWidget_4.show()
        self.ui.stackedWidget_4.setCurrentIndex(0)
    
    def stock_list_cappucino(self):
        self.ui.stackedWidget_4.show()
        self.ui.stackedWidget_4.setCurrentIndex(1)
        
    def stock_list_caffe_mocha(self):
        self.ui.stackedWidget_4.show()
        self.ui.stackedWidget_4.setCurrentIndex(5)
        
    def stock_list_caramel_machiato(self):
        self.ui.stackedWidget_4.show()
        self.ui.stackedWidget_4.setCurrentIndex(4)

    def stock_list_flat_white(self):
        self.ui.stackedWidget_4.show()
        self.ui.stackedWidget_4.setCurrentIndex(3)
        
    def stock_list_iced_expresso(self):
        self.ui.stackedWidget_4.show()
        self.ui.stackedWidget_4.setCurrentIndex(2)
        
        
    def add_stock_coffe_america(self):
        tambah_stok = self.ui.username_7.text()

        confirm = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menambahkan stok untuk menu Caffe Americano sebanyak {tambah_stok}?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            mydb = koneksi()
            mycursor = mydb.cursor()
            sql = "UPDATE menu SET stock = stock + %s WHERE nama_barang = 'Caffe Americano'"
            mycursor.execute(sql, (tambah_stok,))
            mydb.commit()
            QMessageBox.information(self, "Informasi", f"Stok untuk menu Caffe Americano sebanyak {tambah_stok} telah ditambahkan.")
            self.ui.username_7.clear()
            mycursor.close()
        else:
            QMessageBox.information(self, "Informasi", "Penambahan stok untuk menu Caffe Americano dibatalkan.")
        
    def add_stock_cappuccino(self):
        tambah_stok = self.ui.username_8.text()

        confirm = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menambahkan stok untuk menu Cappuccino sebanyak {tambah_stok}?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            mydb = koneksi()
            mycursor = mydb.cursor()
            sql = "UPDATE menu SET stock = stock + %s WHERE nama_barang = 'Cappuccino'"
            mycursor.execute(sql, (tambah_stok,))
            mydb.commit()
            QMessageBox.information(self, "Informasi", f"Stok untuk menu Cappuccino sebanyak {tambah_stok} telah ditambahkan.")
            self.ui.username_8.clear()
            mycursor.close()
        else:
            QMessageBox.information(self, "Informasi", "Penambahan stok untuk menu Cappuccino dibatalkan.")
        
    def add_stock_Caffe_Mocha(self):
        tambah_stok = self.ui.username_9.text()

        confirm = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menambahkan stok untuk menu Caffe Mocha sebanyak {tambah_stok}?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            mydb = koneksi()
            mycursor = mydb.cursor()
            sql = "UPDATE menu SET stock = stock + %s WHERE nama_barang = 'Caffe Mocha'"
            mycursor.execute(sql, (tambah_stok,))
            mydb.commit()
            QMessageBox.information(self, "Informasi", f"Stok untuk menu Caffe Mocha sebanyak {tambah_stok} telah ditambahkan.")
            self.ui.username_9.clear()
            mycursor.close()
        else:
            QMessageBox.information(self, "Informasi", "Penambahan stok untuk menu Caffe Mocha dibatalkan.")
    
    def add_stock_caramel_macchiato(self):
        tambah_stok = self.ui.username_10.text()

        confirm = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menambahkan stok untuk menu Caramel Macchiato sebanyak {tambah_stok}?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            mydb = koneksi()
            mycursor = mydb.cursor()
            sql = "UPDATE menu SET stock = stock + %s WHERE nama_barang = 'Caramel Macchiato'"
            mycursor.execute(sql, (tambah_stok,))
            mydb.commit()
            QMessageBox.information(self, "Informasi", f"Stok untuk menu Caramel Macchiato sebanyak {tambah_stok} telah ditambahkan.")
            self.ui.username_10.clear()
            mycursor.close()
        else:
            QMessageBox.information(self, "Informasi", "Penambahan stok untuk menu Caramel Macchiato dibatalkan.")
    
    def add_stock_flat_white(self):
        tambah_stok = self.ui.username_11.text()

        confirm = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menambahkan stok untuk menu Flat White sebanyak {tambah_stok}?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            mydb = koneksi()
            mycursor = mydb.cursor()
            sql = "UPDATE menu SET stock = stock + %s WHERE nama_barang = 'Flat White'"
            mycursor.execute(sql, (tambah_stok,))
            mydb.commit()
            QMessageBox.information(self, "Informasi", f"Stok untuk menu Flat White sebanyak {tambah_stok} telah ditambahkan.")
            self.ui.username_11.clear()
            mycursor.close()
        else:
            QMessageBox.information(self, "Informasi", "Penambahan stok untuk menu Flat White dibatalkan.")
    
    def add_stock_iced_expresso(self):
        tambah_stok = self.ui.username_12.text()

        confirm = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menambahkan stok untuk menu Iced Espresso and Matcha Fusion sebanyak {tambah_stok}?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            mydb = koneksi()
            mycursor = mydb.cursor()
            sql = "UPDATE menu SET stock = stock + %s WHERE nama_barang = 'Iced Espresso and Matcha Fusion'"
            mycursor.execute(sql, (tambah_stok,))
            mydb.commit()
            QMessageBox.information(self, "Informasi", f"Stok untuk menu Iced Espresso and Matcha Fusion sebanyak {tambah_stok} telah ditambahkan.")
            self.ui.username_12.clear()
            mycursor.close()
        else:
            QMessageBox.information(self, "Informasi", "Penambahan stok untuk menu Iced Espresso and Matcha Fusion dibatalkan.")

        

    def create_member_id(self):
        self.ui.widget_3.show()
  
    def close_member_id(self):
        self.ui.widget_3.close()
        
    
    def logout(self):
        reply = QMessageBox.question(self, 'Logout', 'apakah anda ingin logout?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.ui.stackedWidget.setCurrentIndex(0)
            
            
    def printData(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx)")
        if fileName:
            self.exportToExcel(self.ui.tableWidget, fileName)

    def exportToExcel(self, tableWidget, fileName):
        workbook = xlsxwriter.Workbook(fileName)
        worksheet = workbook.add_worksheet()

        # Menulis header
        headers = []
        column_count = tableWidget.columnCount()
        for column in range(column_count):
            header = tableWidget.horizontalHeaderItem(column).text()
            headers.append(header)
            worksheet.write(0, column, header)

        # Menulis data
        for row in range(tableWidget.rowCount()):
            for column in range(column_count):
                item = tableWidget.item(row, column)
                if item is not None:
                    worksheet.write(row + 1, column, item.text())

        workbook.close()


        
    


        
    def bug(self):
        self.ui.stackedWidget.setCurrentIndex(1)



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = LoginScreen()
#     window.show()
#     sys.exit(app.exec_())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginScreen()
    window.show()
    # window.bug()  
    sys.exit(app.exec_())
