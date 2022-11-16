from flask import Blueprint, flash, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method =='POST':

        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
         
        def containsNumber(value):
            for i in value:
                if i.isdigit():
                    return True
                return False

        data = containsNumber(firstName)
        print(data)

        if len(email) < 4:
             flash('Invaild email address', category='error')
        elif len(password1) < 7:
            flash('That password is to short', category='error')
        elif len(password2) < 7:
            flash('That password is to short', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif data == True:
            flash('The Name can\'t contain numbers', category='error') 
        else:
            flash('The user has been registered successfully.', category='success')                  

    return render_template('sign_up.html')
