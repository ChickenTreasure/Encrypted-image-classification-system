import os
import shutil

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import custom_object_scope
from PIL import Image
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, request, redirect
from tensorflow.python.platform import gfile
from search import recommend




UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

# 定义 WeightedAverageGate 自定义层
class WeightedAverageGate(tf.keras.layers.Layer):
    def __init__(self):
        super(WeightedAverageGate, self).__init__()

    def build(self, input_shape):
        num_inputs = len(input_shape)
        self.weight = self.add_weight(shape=(num_inputs,1), initializer='ones', trainable=True)

    def call(self, inputs):
        expanded_weights = tf.expand_dims(self.weight, axis=-1)
        weighted_sum = tf.reduce_sum(inputs * expanded_weights, axis=0)
        return weighted_sum

# 加载模型时注册自定义层
with custom_object_scope({'WeightedAverageGate': WeightedAverageGate}):
    model = load_model('C:/Users/LENOVO/Desktop/model/save.h5')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image):
    # 对图像进行预处理以适配双流卷积模型
    image = image.resize((28, 28))
    image = image.convert('L')
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)  # 添加 batch 维度
    image = np.stack([image, image], axis=0)  # 双流卷积模型需要两个相同的输入
    return image

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # 打开图像并进行预处理
        image = Image.open(file_path)
        image = preprocess_image(image)
        
        # 预测
        predictions = model.predict(image)
        predicted_class = np.argmax(predictions, axis=1)
        
        # 删除上传的文件
        os.remove(file_path)
        
        return jsonify({'prediction': int(predicted_class[0])})
    else:
        return jsonify({'error': 'Invalid file format'}), 400

@app.route('/upload_img', methods=['GET', 'POST'])
def upload_img():
    print("image upload")
    result = 'static/result'
    if not gfile.Exists(result):
        os.mkdir(result)
    shutil.rmtree(result)

    if request.method == 'POST' or request.method == 'GET':
        print("files")
        print(request.files)
        print("form")
        print(request.form)

        # 检查request中是否存在文件数据
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        # 没有选择图片的情况下提交空文件
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            input_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            recommend(input_location, extracted_features)
            os.remove(input_location)
            image_list = [file[2:-4] for file in os.listdir(result) if not file.startswith('.')]
            print(image_list)
            return jsonify(image_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3367)
