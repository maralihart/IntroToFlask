# Introduction to Flask with Python
A basic Flask web app curriculum built by [Mara (MaraDrinksMilk on Twitch)](https://twitch.tv/maradrinksmilk)

# Set up
This is written for [Replit.com](https://replit.com). Replit will download all the needed dependencies for us and get us set up with hosting a lot quicker. Great for a hackathon!

Paste the following code into `main.py`. This will set up a basic Flask app that simply says "Hello World"
```
from flask import Flask

app = Flask(__name__)

@app.route('/') # At your url without anything following it, it will run main()
def main():
	return 'Hello World'

app.run(host='0.0.0.0', port=5000, debug=True)
```
Click `run` at the top.
That's it. You now have a **working Flask app**!

# Making it Unique!
While you have a basic Flask app going, you probably want to make it your own style. This would involve adding in some HTML templates.

## Make a Template with HTML
1. Make a folder/directory called `templates` and inside create `index.html` with the below code. Feel free to edit.
```
<html>
  <head>
    <title>MaraDrinksMilk</title>
  </head>
  <body>
    <h1>Welcome to my site!</h1>
    <h3>My name is Mara, check me out on <a href="https://twitch.tv/maradrinksmilk" target="_blank">Twitch</a>!</h3>
    
    <p>Can't wait to code with you!</p>
  </body>
</html>
```
2. Now if you rerun your code, nothing changes. You have to link your function to this template. 
Replace `return "Hello World"` with `return render_template('index.html')` which means that Flask will be looking inside the `template` folder to find the file `index.html`.
* Oh, no! You got an error? Don't forget to add `render_template` to your imports from Flask

## Making More than One Page
You probably noticed that now our default web page gives us a `Not Found` error. Let's adjust!
1. Make a new route and function similar to the one that is already there. 
2. Replace the route to say `/hello` and the function name to be `hello`.
3. Let's make a new template called `hello.html` and make sure to change that in the return as well. Inside this file, copy and paste the following code:
```
<html>
  <head>
    <title>MaraDrinksMilk</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
```
Now, open your website in a new Tab and go to `<url>/hello`. You should need a large heading that says "Hello World"

## Adding Variables in Flask
1. Create a new route and function similar to `hello` instead named `hello_name`, but instead make the route 
1. Add a place to pass the variable in the URL. Replace `@app.route('/')` with `@app.route('/hello/<name>')`. This means that whatever is after the / in the url, Flask will take this as the variable `name`
2. Pass it through the function as an argument so your function header is now `def hello_name(name)`
3. Now, how do we get it to our template? Add another argument in your `render_template` function so it looks like `return render_template('hello.html', name=name)`
4. If you try your app at `<your url>/hello/ada`, nothing will happen even if you take in the name. You'll need to edit the template file. 
5. If we put in `{{name}}` instead of World, we'll see the name. 
6. Now, if you pull up `<your url>/hello`, you'll see "Hello, !" and we want to make "World" the default name if nothing is given. Let's try replacing `{{name}}` with `{{name if name else "World"}}`
* This is called a ternary operator or a conditional operator. It's just a quick one-line if else statement. The format in Python is `[result if true] if [condition] else [result if false]`

## Making it Look Better with CSS
1. Make a new folder called `static`. Static means that there are no modifications. We will not be changing these items while we are running.
2. In `static`, we'll make another folder called `css` where we'll create `index.css`.
3. Then to link it, we'll go to our desired .html file `index.html` and add in the `<head>` (after `<title>`) the following line `<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">`
4. Now we'll make a couple changes. Paste the following code into `index.css`
```
body {
  background-color: #E4B3A9;
}

h1 {
  color: white;
  text-align: center;
}
```
* This may take minute or two to load, but look at the new tab (not the window in replit) for updated changes!

# Free 24/7 Hosting
1. Sign up for UptimeRobot
2. Go to your dashboard
3. Click `+ Add a New Monitor` in the top left
4. For monitor type, choose `HTTP(S)`
5. For friendly name, write whatever will help you remember
6. For the URL, enter your replit.com link you get when you run your flask app
7. For monitoring interval, stick with 5 minutes

**Wow**, now your web app will never go down... for free!