from flask import flash, redirect, render_template, url_for, abort
from . import administrator
from flask_login import current_user, login_required
from app import db
from ..models import SiswaBaru
from .forms import SiswaBaru_Forms
from datetime import datetime

@administrator.route('/dashboard')
@login_required
def dashboard():
    return render_template('administrator/dashboard.html', title="Welcome To Aplikasi PPDB SMA U@")

@administrator.route('/dashboard/list_siswa')
@login_required
def list_siswa():
    siswa = SiswaBaru.query.order_by(SiswaBaru.id).all()
    return render_template('administrator/list.html',siswa=siswa ,title="List Siswa Baru")

@administrator.route('/dashboard/tambah_siswabaru', methods=['GET','POST'])
@login_required
def create():
    form=SiswaBaru_Forms()
    tambah_siswa=True
    if form.validate_on_submit():
        siswa = SiswaBaru(
			nama_lengkap = form.Nama_lengkap.data,
			jenis_kelamin = form.Jenis_Kelamin.data,
			nisn = form.nisn.data,
			asal_sekolah = form.asal_sekolah.data,
			nilai_unas = form.nilai_un.data,
			alamat = form.alamat.data,
			nomer_hp = form.nomer_hp.data,
			nama_ortu_ayah = form.nama_orangtua_ayah.data,
			nama_ortu_ibu = form.nama_orangtua_ibu.data,
			pekerjaan_ortu_ayah = form.pekerjaan_orangtua_ayah.data,
			pekerjaan_ortu_ibu = form.pekerjaan_orangtua_ibu.data,
			pendidikan_ortu_ayah = form.pendidikan_ayah.data,
			pendidikan_ortu_ibu = form.pendidikan_ibu.data,
			penghasilan_ortu_ayah= form.penghasilan_ayah.data,
			penghasilan_ortu_ibu=form.penghasilan_ibu.data,
            hobi = form.hobi.data,
			diterima_di_kelas =form.diterima_di_kelas.data
			)
        try:
            db.session.add(siswa)
            db.session.commit()
            flash("Data Berhasil di tambahkan")
            return redirect(url_for('administrator.list_siswa'))
        except:
            flash("Data Telah Ada")
            return redirect(url_for('administrator.list_siswa'))
    return render_template('administrator/tambah.html',action="Add", form=form, tambah_siswa=tambah_siswa, title="Tambah Siswa")

@administrator.route('/dashboard/edit_siswabaru/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    siswa = SiswaBaru.query.get_or_404(id)
    form = SiswaBaru_Forms(obj=siswa)
    tambah_siswa=False
    if(form.validate_on_submit()):
        siswa.nama_lengkap = form.Nama_lengkap.data
        siswa.jenis_kelamin = form.Jenis_Kelamin.data
        siswa.nisn = form.nisn.data
        siswa.asal_sekolah = form.asal_sekolah.data
        siswa.nilai_unas = form.nilai_un.data
        siswa.alamat = form.alamat.data
        siswa.nomer_hp = form.nomer_hp.data
        siswa.nama_ortu_ayah = form.nama_orangtua_ayah.data
        siswa.nama_ortu_ibu = form.nama_orangtua_ibu.data
        siswa.pekerjaan_ortu_ayah = form.pekerjaan_orangtua_ayah.data
        siswa.pekerjaan_ortu_ibu = form.pekerjaan_orangtua_ibu.data
        siswa.pendidikan_ortu_ayah = form.pendidikan_ayah.data
        siswa.pendidikan_ortu_ibu = form.pendidikan_ibu.data
        siswa.penghasilan_ortu_ayah= form.penghasilan_ayah.data
        siswa.penghasilan_ortu_ibu=form.penghasilan_ibu.data
        siswa.diterima_di_kelas =form.diterima_di_kelas.data
        siswa.hobi = form.hobi.data
        db.session.commit()
        flash("Siswa berhasil di update")
        return redirect(url_for('administrator.list_edit_or_delete'))

    form.Nama_lengkap.data = siswa.nama_lengkap
    form.Jenis_Kelamin.data = siswa.jenis_kelamin
    form.nisn.data = siswa.nisn
    form.asal_sekolah.data = siswa.asal_sekolah
    form.nilai_un.data = siswa.nilai_unas
    form.alamat.data = siswa.alamat
    form.nomer_hp.data = siswa.nomer_hp
    form.nama_orangtua_ayah.data = siswa.nama_ortu_ayah
    form.nama_orangtua_ibu.data = siswa.nama_ortu_ibu
    form.pekerjaan_orangtua_ayah.data = siswa.pekerjaan_ortu_ayah
    form.pekerjaan_orangtua_ibu.data = siswa.pekerjaan_ortu_ibu
    form.pendidikan_ayah.data= siswa.pendidikan_ortu_ayah
    form.pendidikan_ibu.data = siswa.pendidikan_ortu_ibu
    form.penghasilan_ayah.data = siswa.penghasilan_ortu_ayah
    form.penghasilan_ibu.data = siswa.penghasilan_ortu_ibu
    form.diterima_di_kelas.data = siswa.diterima_di_kelas
    form.hobi.data = siswa.hobi
    return render_template('administrator/tambah.html', action="Edit", siswa=siswa, tambah_siswa=tambah_siswa, form=form,title="Update Siswa")


@administrator.route('/dashboard/delete_siswabaru/<int:id>', methods=['GET','POST'])
@login_required
def delete(id):
    siswa = SiswaBaru.query.get_or_404(id)
    db.session.delete(siswa)
    db.session.commit()
    flash("Siswa Telah Di Delete")
    return redirect(url_for('administrator.list_edit_or_delete'))


@administrator.route('/dashboard/print_siswabaru/<int:id>', methods=['GET','POST'])
@login_required
def print_siswa(id):
    siswa = SiswaBaru.query.get_or_404(id)
    User = current_user.username
    return render_template('administrator/print.html', siswa=siswa, User=User,now=datetime.now() ,title="Print Siswa Baru" + siswa.nama_lengkap)

@administrator.route('/dashboard/print_siswa')
@login_required
def list_print():
    siswa = SiswaBaru.query.order_by(SiswaBaru.id).all()
    return render_template('administrator/list_print.html', siswa=siswa, title="List Siswa Yang Akan di Print")

@administrator.route('/dashboard/list_siswa_edit_delete')
@login_required
def list_edit_or_delete():
    siswa = SiswaBaru.query.order_by(SiswaBaru.id).all()
    return render_template('administrator/list_edit_delete.html', siswa=siswa, title="List Siswa Yang Akan di Print")
