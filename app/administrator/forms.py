from flask_wtf import FlaskForm
from app import db
from wtforms import StringField, SubmitField, SelectField, IntegerField, FloatField, DateTimeField, FieldList, FormField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Optional
from ..models import SiswaBaru

class SiswaBaru_Forms(FlaskForm):
	Nama_lengkap = StringField('Nama Lengkap', validators=[DataRequired()])
	Jenis_Kelamin = SelectField('Jenis Kelamin',choices=[('Laki-Laki','Laki-Laki'),('Perempuan','Perempuan')] ,validators=[DataRequired()])
	nisn = IntegerField('NISN', validators=[DataRequired()])
	alamat = StringField('Alamat', validators=[DataRequired()])
	nomer_hp = IntegerField('Nomer Hp', validators=[DataRequired()])
	asal_sekolah = StringField('Asal Sekolah', validators=[DataRequired()])
	nilai_un = FloatField('Nilai UN', validators=[DataRequired()])
	nama_orangtua_ayah = StringField('Nama Orangtua Ayah', validators=[Optional()])
	nama_orangtua_ibu =StringField('Nama Orangtua Ibu', validators=[Optional()])
	pekerjaan_orangtua_ayah = StringField('Pekerjaan Orangtua Ayah', validators=[Optional()])
	pekerjaan_orangtua_ibu = StringField('pekerjaan Orangtua Ibu', validators=[Optional()])
	pendidikan_ayah = StringField('Pendidikan Ayah', validators=[Optional()])
	pendidikan_ibu = StringField('Pendidikan Ibu', validators=[Optional()])
	penghasilan_ayah = FloatField('Gaji Orangtua Ayah', validators=[Optional()])
	penghasilan_ibu = FloatField('Gaji Orangtua Ibu', validators=[Optional()])
	hobi = StringField('Hobi Siswa')
	diterima_di_kelas = SelectField('Diterima di Kelas',choices=[('X','X'),('XI','XI'),('XII','XII')] ,validators=[DataRequired()])
	submit = SubmitField('Submit')
