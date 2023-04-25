# README

## Virtual environment

Install virtual environment

```sh
$ sudo apt install python3-venv
```

Activate `venv` and install dependencies

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python3 -m pip install --upgrade pip
(.venv) $ pip install -r requirements.txt
```

Start the web app:

```sh
$ flask run -h 0.0.0.0
* Environment: production
...
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Fire up a web browser and navigate to [http://localhost:5000](http://localhost:5000)


## Docker

Build a docker image:

```sh
docker build -t xtec/flask .
```

Run the `xtec/flask` image:

```sh
docker run --rm -d --name flask -p 5000:80 xtec/flask
``` 


## Tools

[Virtual Environment](venv.md). The `venv` module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

[pip](pip.md).

[VSCode](vscode.md) .Working with Python in Visual Studio Code, using the 

[Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), is simple, fun, and productive. The extension makes VS Code an excellent Python editor, and works on any operating system with a variety of Python interpreters. It leverages all of VS Code's power to provide auto complete and IntelliSense, linting, debugging, and unit testing, along with the ability to easily switch between Python environments, including virtual and conda environments.



