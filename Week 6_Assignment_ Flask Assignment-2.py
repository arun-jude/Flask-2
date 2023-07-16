# Question 1 - Explain GET and POST methods

# Answer 1 -
# GET method - GET: This method is used to retrieve data from the server. 
# e.g In an eCommerce application, there is a search button to search for an item. 
# after entering a keyword if we noticed, the keyword you searched for gets displayed in the URL. 
# This request is used when the data is not sensitive.

# POST method - This method makes enables users to send data over to the server. 
# e.g In any authentication-enabled application, the registration and login form is the best example for the post method. 
# Whenever we enter Information and submit the data get transferred over to the POST request. 
# And if we noticed, unlike get request there is no information will be ever displayed in the URL.

# Question 2 - 

# Answer 2 - 
# In the client-server architecture, the request object contains all the data that is sent from the client to the server.
# This data can be recovered using the GET/POST methods.

# Question 3 -

# Answer 3 - 
# Flask redirect is defined as a function or utility in Flask which allows developers to redirect users to a specified URL 
# and assign a specified status code. When this function is called, a response object is returned, 
# and the redirection happens to the target location with the status code.

# Question 4 - 

# Answer 4 - 
# Templates are files that contain static data as well as placeholders for dynamic data. 
# A template is rendered with specific data to produce a final document.
#The template system provides some HTML syntax which are placeholders for variables and expressions 
# that are replaced by their actual values when the template is rendered.

#use of render_template() function: -
#render_template() function in Flask facilitates us to render the external HTML file instead of hardcoding the HTML code
# in the Python program

# Question 5 - 

# Answer 5 - simple API code example: -

from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtraction of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiplication of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The division of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return render_template('results.html' , result = result)



@app.route('/postman_action',methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
