from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from .. models import Employee


@auth.route('/register', methods=['GET','POST'])
def register():
    """
    Handle request to the /register route
    add employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            password=form.password.data)

        #add employee to database
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered, you may now login.')

        return redirect(url_for('auth.login'))

    #load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET','POST'])
def login():
    #Handle login request and log employees in through the login form
    
    form = LoginForm()
    if form.validate_on_submit():
        #check whether employee exists in the db and the password entered matches the pw in db
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(
                form.password.data):
            #log employee in
            login_user(employee)

            #redirect to dashboard after logging in
            if employee.is_admin:
                return redirect('home.admin_dashboard')
            else:
                return redirect(url_for('home.dashboard'))

        # when login details are not correct
        else:
            flash('Invalid email or password')
    
    #load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    #handles requests to /logout route and logs employee out through the logout link
    logout_user()
    flash('You have successfully logged out')

    #redirect to login page
    return redirect(url_for('auth.login'))