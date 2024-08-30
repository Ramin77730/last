from flask import Flask, render_template, send_file, abort
import requests
from io import BytesIO

app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/')
def index():
    return render_template("index.html")

# Маршрут для получения изображения
@app.route('/get_image/<file_id>')
def get_image(file_id):
    try:
        # Формирование URL для доступа к изображению на Google Drive
        url = f"https://drive.google.com/uc?export=view&id={file_id}"

        # Отправка запроса на получение изображения
        response = requests.get(url)

        # Если запрос успешен (статус код 200)
        if response.status_code == 200:
            # Чтение содержимого изображения в формате байтов
            image = BytesIO(response.content)

            # Отправка изображения как файла
            return send_file(image, mimetype='image/jpeg')
        else:
            # Если изображение не найдено
            abort(404)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
