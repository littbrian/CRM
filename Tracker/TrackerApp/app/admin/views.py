from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import DepartmentForm
from .. import db
from .. models import Department

def check_admin():
    #Prevent non-admin from accessing the page
    if not current_user.is_admin:
        abort(403)

#Department Views

@admin.route('/departments', methods=['GET','POST'])
@login_required
def kist_department():
    #list all departments
    check_admin()
    departments = Departments.query.all()

    return render_template('admin/departments/departments.html',departments=departments, title="Departments")

@admin.route('departments/add', methods=['GET','POST'])
@login_required
def add_department():
    # Add a department to the database
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data, description=form.description.raw_data)
        try:
            #add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department')
        except:
            #in case department already exists
            flash('Department name already exists')

        #redirect to departments page
        return redirect(url_for('admin.list.departments'))

# load department template
    return render_template('admin/departments/department.html', action="Add",
                    add_department=add_department, form=form,title="Add Department")

                
