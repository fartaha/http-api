# http-api
A simple HTTP-API with Flask


# How to write a simple HTTP API with Flask

> + In this repo we create a simple Flask HTTP API that calculate sum of two values from a JSON input and outputs the sum in the JSON format. 
> + All is done in Python and you can apply the method used here to any other complex application and formulas that need to run a Python code in the Backend.

# Table of Contents
1. [Step 1 (create a directory)](#step1)
2. [Step 2 (setting up the environment)](#step2)
3. [Step 3 (installing Flask)](#step3)
4. [Step 4 (Python code and Flask)](#step4)
5. [Step 5 (test)](#step5)



## Step1
**Make** a repository or directory in your local machine:
lets call it `flask-app/`
```console
flask-app/
│
├──
│
└── 
```
## Step2
**Navigate** to your app directory and create and activate a virtual environment to make sure that installing libraries doesn't break your other apps:
```
$ python -m venv venv
$ source venv/bin/activate
```
Now you have a `venv/` directory inside your app directory.
```console
flask-app/
│
├
│
└── venv/
```
## Step3
**Install**  Flask using:
```shell
$ pip instal flask
```
to make sure that Flask is installed:
call the Python prompt by typing:
```shell
$ python
```
and then running the following:
```python
import flask
print(flask.__version__)
```
if it gives you the version, then it's installed correctly in your environment.
## Step4
Create a Python file in your directory and call it something like `flask-app1.py`. You should have now all of these in your main directory:
```console
flask-app/
│
├── flask-app1.py
│
└── venv/
```
Modify the Python file `.py` with adding the following code to it:
> **@app.route('/sum', methods=['POST'])**
> + This is basically creating a http endpoint for getting the JSON 
```python
from  flask  import  Flask, request, jsonify
 
app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def  sum():
	data = request.get_json()
	a = data['a']
	b = data['b']
	result = a + b
return  jsonify(result=result)

if  __name__ == '__main__':
	app.run(port=8000)
```
## Step5
Now we can test it whether our app works well or not: 
> + It should gives us the JSON output of 8 for a JSON input of 3, 5:
> **'{"a":5, "b":3}'**

To do so run the following command in the shell to run the app first:
```shell
$ python flask-app1.py
```
It should run a server on http://127.0.0.1:8000 and then you can make a JSON request like:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"a":5, "b":3}' http://localhost:8000/sum
``` 
It should show the result as a JSON output like**{"result":8}** in the shell:
```shell
{"result":8}
```
