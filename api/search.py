import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

c.execute('SELECT id, name FROM api_product')
products = c.fetchall()

vectorlizer = TfidfVectorizer()
vectors = vectorlizer.fit_transform([p[1] for p in products])

def search(query):
    query_vector = vectorlizer.transform([query])
    scores = vectors.dot(query_vector.T).toarray()
    sorted_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return [products[i[0]][0] for i in sorted_scores if i[1] > 0]
    