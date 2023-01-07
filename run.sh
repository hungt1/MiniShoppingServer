python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
pip install scikit-learn
pip install sklearn
pip install pretty-html-table
chmod a+x run.sh
python3 manage.py runserver 8000
