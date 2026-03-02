##first things first
when using exteranal dependencies (instal with PIP), it is best to use a pythin vertual enviroment(venv) to create isolated enviriomnets and to avoid conflicts between projects.

## what is pip?

- "prefers installation program" - pagage magager for python.
- downlades and adds to your peogram, third party libariess from pyPI - python package index

## why use venv?

- when using pip you dont want to creat version conflicts in your system - so you install dependacys at the project level.
- venv is essentically a project level copy of python

### setting up a venv

- in the terminal type `python -m venv venv` - or `python -m venv my_folder`
  - this creates a folder named venv contaiining the isolated enviroment
- now we have to resorsec for the virtual enviromnte, but we have not activated it yet(so any installs we have are atill global)
- activate the enviroment with(in windows) `venv/scripts/activate`
- when you are done working in your virtual enviromnt, you can exit it with `deactivate`

#### freezing requirements

- you should getignore your `venv folder, but you want to keep track of what needs intslalled for youe program
  - to do this u use a requiremts.txt file. you can create it (while the venv is going) with `pip freeze > requirements.txt`
  - this will create a `requiremtsns.txt` file.

#### installing from requirements.txt

- if you pull your project down from github or other source control, ypou will need to create the virtual enviroment (you should do this). then you can install all dependecies with `pip install -r requirements.txt`

## PyQT5 - what is it?

- PyQT5 is a populor python libary for creatinf graphical user interfies (GUIs) - pronoused "gooey"

### instal PyQT5

- `pip install PyQt5`
- make sure you aee in your enviroment
