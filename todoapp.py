from flask import Flask,request, render_template
import re

app = Flask(__name__)
x = []

@app.route('/')
def home_page():
	return render_template("index.html",taskList=x)

#Deleting Individual Items
@app.route('/remove/<int:item_id>')    
def remove_Item(item_id):
	del x[item_id]
	return render_template('index.html',taskList=x)


#Deleting All Items
@app.route('/clear')
def clear_list():
	del x[:]
	return render_template('index.html',taskList=x)


#Adding New Item
@app.route('/submit',methods = ['POST'])
def submit_item():
	if request.method == 'POST':
		email = request.form['email']
		task = request.form['task']
		priority = request.form['priority']
		if not is_email_address_valid(email):
			errors ="Item not added to list as email id was not valid. Try again"
			return render_template('index.html',error=errors,taskList=x)       
		x.append([email,task,priority])
		return render_template('index.html',taskList=x)	

@app.route('/addItem')
def add_itemPage():
	return render_template('form.html')


def is_email_address_valid(email):
    """Validate the email address using a regex."""
    if not re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email):
        return False
    return True



if __name__ == '__main__':
    app.run()