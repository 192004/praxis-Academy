@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login()
    else:
        return show_the_login_form()