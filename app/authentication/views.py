from flask import flash, redirect, render_template, url_for, abort
from . import authentication
from flask_login import current_user, login_required, login_user, logout_user
from app import db
from ..models import User
from .forms import LoginForm


@authentication.route('/', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = User.query.filter_by(username=form.username.data).first()
        if admin is not None and admin.verifikasi_password(form.password.data):
            login_user(admin)
            return redirect(url_for('administrator.dashboard'))
        else:
            flash('Invalid Username and Password')
    return render_template('authentication/login.html' ,form=form, title="Login To App")


@authentication.route('/Logout')
@login_required
def logout():
    logout_user()
    flash("Anda Telah Logout")
    return redirect(url_for('authentication.login'))
