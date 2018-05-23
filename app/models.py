from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from app import db, login_manager
from datetime import datetime
from sqlalchemy import DateTime
class User(UserMixin, db.Model):

    __tablename__= 'm_user'

    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True,nullable=False)
    password_hash = db.Column(db.String(100), unique=True, nullable=False)
    Nama = db.Column(db.String(60), nullable=False)

    @property
    def password(self):
        raise AttributeError('Password tidak valid')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verifikasi_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User: {}>'. format(self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class SiswaBaru(db.Model):

    __tablename__ = 'm_siswa_baru'

    id = db.Column(db.Integer,primary_key=True)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    jenis_kelamin = db.Column(db.String(100), nullable=False)
    nisn = db.Column(db.Integer, nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    nomer_hp = db.Column(db.Integer,nullable=False)
    asal_sekolah = db.Column(db.String(100), nullable=False)
    nilai_unas = db.Column(db.Integer,nullable=False)
    nama_ortu_ayah = db.Column(db.String(100), nullable=True)
    nama_ortu_ibu = db.Column(db.String(100), nullable=True)
    pekerjaan_ortu_ayah = db.Column(db.String(100),nullable=True)
    pekerjaan_ortu_ibu = db.Column(db.String(100),nullable=True)
    pendidikan_ortu_ayah = db.Column(db.String(100),nullable=True)
    pendidikan_ortu_ibu = db.Column(db.String(100),nullable=True)
    penghasilan_ortu_ayah = db.Column(db.String(100),nullable=True)
    penghasilan_ortu_ibu = db.Column(db.String(100),nullable=True)
    diterima_di_kelas = db.Column(db.String(100),nullable=False)
    hobi = db.Column(db.String(100),nullable=True)
    def __repr__(self):
        return '{}'.format(self.nama_lengkap)
