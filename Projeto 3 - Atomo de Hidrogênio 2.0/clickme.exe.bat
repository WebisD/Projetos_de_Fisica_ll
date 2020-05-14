ECHO OFF
python -m pip install --upgrade pip wheel setuptools virtualenv
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
python -m pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/
python mainApp.py
PAUSE