name:python script workflow
on:
push:
branch:
-main
jobs:
run_python_script:
name:Run hello.py
runs-on:ubuntu-latest
steps:
- name:checkout repository
uses:action/checkout@y2
- name set name python@y2
with:
python-version:'3.12'#use the python version you need
- name:run tsting.py
run: pythontsting.py
