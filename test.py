import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import custom_object_scope

import tensorflow as tf


from PIL import Image
import numpy as np

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

def preprocess_image(image_path, target_size):
    # 打开图像并调整大小
    image = Image.open(image_path).convert('L')
    image = image.resize(target_size, Image.LANCZOS)
    # 转换为 NumPy 数组并扩展维度
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=-1)
    # 归一化
    image_array = image_array.astype('float32') / 255.0
    return image_array

def predict_image(image_path, model):
    # 预处理图像
    input_image = preprocess_image(image_path, (28, 28))
    # 进行预测
    predictions = model.predict(np.array([input_image]))
    # 获取预测结果
    predicted_class = np.argmax(predictions[0])
    return predicted_class

@app.route('/predict', methods=['POST'])
def upload_and_predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # 使用模型进行预测
        predicted_class = predict_image(file_path, model)
        # 删除上传的文件
        os.remove(file_path)
        return jsonify({'prediction': int(predicted_class)})
    else:
        return jsonify({'error': 'Invalid file format'}), 400


@app.route('/upload_and_predict', methods=['POST'])
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
        # 这里需要根据你的模型输出进行相应的处理
        # 假设模型的输出是一个向量，每个元素代表一个类别的概率
        predicted_class = np.argmax(predictions, axis=1)
        
        # 删除上传的文件
        os.remove(file_path)
        
        return jsonify({'prediction': int(predicted_class[0])})
    else:
        return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3367)
