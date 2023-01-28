from flask import Flask, request, jsonify
from flask_cors import CORS
import model
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def recommend_movies():
    res = model.predict(request.args.get(
        'q'), request.args.get('v'), request.args.get('d'))
    return jsonify(res)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
