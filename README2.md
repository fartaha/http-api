# HTTP API using Flask
author: Taha Heidari
email: taha.heidari@aalto.fi
---

+ This is my implementation for Preliminary Assignment for Engineering Positions @ WOLT to address the Backend specifics using Flask and Python to create a single HTTP API endpoint.
+ To make it work: do the following steps  

## Step1
Unzip the downloaded file called `WOLT-HTTP.zip`

## Step2
Open the terminal and run the following command to create and activate a virtual environment.
+ This is to make sure that installing different libraries doesn't break other apps

```shell
python -m venv venv
source venv/bin/activate
```

## Step3
Install all dependencies by running the following commmand in terminal.

```shell
pip install -r requirements.txt
```

## Step4
run the wolt-app.py by by running the following commmand in terminal:

```shell
python wolt_app.py
```
+ This will starts a local server on port:8000

## Step5
**Open an another terminal** while letting the previous one be working.

## Step6
In the **new terminal** you can make request by running the following command which points to the JSON input as follows:

```shell
curl -X POST -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}' http://localhost:8000/calculate_delivery_fee
```
+ you can change the values in the JSON above to test the code.

