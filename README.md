# simple-flask-website-simulator

## Introduction

This is a simple Flask application for simulation website delays.

---

## Project Setup

### First Steps

You can begin by either downloading a zip file of the project through github, or using a git command to clone the project by:

```bash
git clone https://github.com/etycomputer/simple-flask-website-simulator.git
```

### Virtual Environment Setup

Create a [Python 3.8.1](https://www.python.org/downloads/release/python-381/) based virtual environment (venv) for this project directory.
```bash
virtualenv venv -p python3.8.1
```
After you have your virtual environment directory Setup, you need to activate it.

#### On Linux
```bash
source venv/bin/activate
```
#### On Windows
```bash
venv\Scripts\activate
```
### Dependency installations

To install the necessary packages:

```bash
pip install -r requirements.txt
```

---

##Requirements

This project utilizes the following requirements:

1. Python v3.8.1
1. Flask v1.1.2
1. pytest v6.2.3
1. flask-unittest v0.1.1
1. gunicorn v20.1.0