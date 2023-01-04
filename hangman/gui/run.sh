python3 -m venv gui/venv
. venv/bin/activate; pip install -Ur gui/requirements.txt
python gui/main.py
rm -rf gui/venv
