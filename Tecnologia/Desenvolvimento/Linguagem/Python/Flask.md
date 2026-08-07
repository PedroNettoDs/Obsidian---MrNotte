### Sobre
É um 'micro'[[Framework]] Web escrito em [[Python]]

### Mínimo necessário
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_word():
	return "<p>Hello, World!</p>"
```


https://flask-palletsprojects-com.translate.goog/en/stable/quickstart/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc