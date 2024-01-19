from flask import abort, render_template
from flask_login import current_user, login_required


from . import home

@home.route('/')
def homepage():
    #render homepage template on the / route
    return render_template('home/index.html', title="welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    #render dashboard template on the / route
    return render_template('home/dashboard.html', title="dashboard")

#admin dashboard view
@home.route('/admin/dashboard')
def admin_dashboard():
    #prevent non-admins fromm accessing this page
    if not current_user.is_admin:
        abort(403)
    
    return render_template('home/admin_dashboard.html', title="Dashboard")