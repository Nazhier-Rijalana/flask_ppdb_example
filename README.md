FLASK CRUD With Login Example: </br>
Cocok Untuk Yang Lagi Matkul RPL atau Interaksi Manusia Komputer Atau Matkul Lainnya yang berhubungan dengan database </br>
cara install : </br>
    1. Clone Repo ini </br>
    2. Install Virtualenv (pip install virtualenv) *bagi yang sudah install skip tutorial ini* </br>
    3. lalu jalankan perintah virtualenv test *test bisa diganti sesuai keinginan* </br>
    4. lalu jalankan perintah source test/bin/activate *test sesuaikan dengan nama virtualenv kalian* </br>
    5. lalu install semua package yang dibutuhkan aplikasi ini dengan perintah pip install -r requirements.txt </br>
    6. setelah selesai edit di app/__init__.py di baris ke 13 rubah app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:toor@localhost/ua_imk' di bagian root rubah dengan username mysql kalian dan toor dengan password kalian jika kosong maka hapus saja dan ua_imk rubah dengan nama database kalian </br>
    7. setelah itu buat database di dbms kalian </br>
    8. lalu lakukan perintah export FLASK_APP=run.py </br>
    9. lalu lakukan perintah flask db init </br>
    10. jika sudah lakukan perintah flask db migrate lalu flask db upgrade </br>
    11. jika sudah maka lakukan python run.py/flask run </br>
    12. taraaa flask sudah siap hehehehe </br>

    untuk tambah username silahkan dengan cara berikut : </br>
    1. jalankan perintah flask shell </br>
    2. lalu ketik perintah berikut : </br>
      a. from app import db </br>
      b. from app.models import * </br>
      c. user = User(username="",password="",Nama="") </br>
      d. db.session.add(user) </br>
      e. db.session.commit() </br>

    okay fitur aplikasi ini adalah <br>
    Crud + login </br>
    cetak ke pdf atau langsung ke printer </br>
    Flask menggunakan versi 1.0.2i </br>
    WTForms </br>
    untuk dbms lain coba dikembangkan hehehe </br>
