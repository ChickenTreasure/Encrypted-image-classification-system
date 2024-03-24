import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import time

import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras import layers
from tensorflow.keras.regularizers import l2
from tensorflow.keras.utils import to_categorical



# 乘法门层
class MultiplicationGate(layers.Layer):
    def __init__(self):
        super(MultiplicationGate, self).__init__()

    def call(self, inputs):
        # 对输入进行乘法门操作
        output = inputs[0] * inputs[1]
        return output

# 加权平均门层

class WeightedAverageGate(layers.Layer):
    def __init__(self):
        super(WeightedAverageGate, self).__init__()

    def build(self, input_shape):
        num_inputs = len(input_shape)
        self.weight = self.add_weight(shape=(num_inputs,1), initializer='ones', trainable=True)

    def call(self, inputs):
        expanded_weights = tf.expand_dims(self.weight, axis=-1)
        weighted_sum = tf.reduce_sum(inputs * expanded_weights, axis=0)
        return weighted_sum


# 定义双流卷积模型
def create_dual_stream_model():
    input_shape1 = (28, 28, 1)  # 假设输入图像尺寸为28x28，通道数为1
    input_shape2 = (28, 28, 1)
    input_1 = tf.keras.Input(shape=input_shape1)  # 第一个输入流
    input_2 = tf.keras.Input(shape=input_shape2)  # 第二个输入流

    # 第一层卷积层
    conv1_1 = layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=l2(0.001))(input_1)
    conv2_1 = layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=l2(0.001))(input_2)

    # 第一层池化层
    pool1_1 = layers.MaxPooling2D((2, 2))(conv1_1)
    pool2_1 = layers.MaxPooling2D((2, 2))(conv2_1)

    # 将池化层的输出转换为一维向量形式
    flatten_data1_1 = layers.Flatten()(pool1_1)
    flatten_data2_1 = layers.Flatten()(pool2_1)

    # 创建加权平均门层
    weighted_avg_gate1 = WeightedAverageGate()
    weighted_avg_gate1_output = weighted_avg_gate1([flatten_data1_1, flatten_data2_1])


    # 将加权平均门处理后的数据恢复成原来的大小
    reshaped_data1 = layers.Reshape(target_shape=(13, 13, 32))(weighted_avg_gate1_output)
    # 第二层卷积层
    conv1_2 = layers.Conv2D(64, (3, 3), activation='relu', kernel_regularizer=l2(0.001))(reshaped_data1)
    conv2_2 = layers.Conv2D(64, (3, 3), activation='relu', kernel_regularizer=l2(0.001))(pool2_1)

    # 第二层池化层
    pool1_2 = layers.MaxPooling2D((2, 2))(conv1_2)
    pool2_2 = layers.MaxPooling2D((2, 2))(conv2_2)

    # 将池化层的输出转换为一维向量形式
    flatten_data1_2 = layers.Flatten()(pool1_2)
    flatten_data2_2 = layers.Flatten()(pool2_2)

    # 加权平均门操作
    weighted_avg_gate2 = WeightedAverageGate()
    weighted_avg_gate2_output = weighted_avg_gate2([flatten_data1_2, flatten_data2_2])


    # 全连接层
    dense1 = layers.Dense(1024, activation='relu')(weighted_avg_gate2_output)
    dense2 = layers.Dense(1024, activation='relu')(dense1)

    # 输出层
    output = layers.Dense(10, activation='softmax')(dense2)  # 假设有10个类别

    model = tf.keras.Model(inputs=[input_1, input_2], outputs=output)
    return model

# 提取MNIST数据集的标签
def label_exacted(input_path):
    # 获取文件夹中的所有文件名
    file_names = os.listdir(input_path)
    # 用于保存标签和类别的数组
    labels = []
    classes = []
    # 定义类别标签映射
    class_labels = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}     # MNIST数据集
    # 遍历文件名列表
    for file_name in file_names:
        # 提取第一个字符
        first_char = file_name[9]
        # 根据类别标签映射为整数标签
        class_label = class_labels[first_char]
        # 添加标签和类别到列表
        labels.append(class_label)
        classes.append(first_char)
    # 转换为NumPy数组
    labels = np.array(labels)
    classes = np.array(classes)
    return labels, classes



#加载训练数据,灰度图像
def exact_traindata(dataset_path,target_size):
    # 定义数据列表
    data = []

    # 遍历数据集文件夹
    for filename in os.listdir(dataset_path):
        # 构建图像文件路径
        image_path = os.path.join(dataset_path, filename)
        # 打开图像文件
        image = Image.open(image_path).convert('L')
        # 调整图像大小为指定尺寸
        image = image.resize(target_size, Image.LANCZOS)
        # 将图像转换为 NumPy 数组
        image_array = np.array(image)
        # 关闭 image，避免产生图片打开数量过多,不会报错，但是速度会变慢
        image.close()
        # 将图像数据添加到数据列表
        data.append(image_array)

    # 转换为 NumPy 数组
    data = np.array(data)
    # 确保数据形状正确（例如，如果图像是灰度图，可以添加一个维度）
    data = np.expand_dims(data, axis=-1)
    # 确保数据类型正确（例如，如果模型期望float32类型的数据，可以使用astype进行转换）
    data = data.astype('float32')
    # 确保数据范围正确（例如，如果图像像素范围是0-255，可以将其缩放到0-1之间）
    data /= 255.0
    return data


# 这个下面的代码时可以正常执行的
if __name__ == "__main__":
    # 创建双流卷积模型
    model = create_dual_stream_model()

    # 编译模型
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


    # 加载训练数据(远程服务器运行)
    #改动，添加上了路径
    train_data_1 = exact_traindata('./dataset/train_AES', (28, 28))
    train_data_2 = exact_traindata('./dataset/train_gradient_images',
                                       (28, 28))
    train_labels, train_class = label_exacted('./dataset/train_AES')


    #加载验证及数据（远程服务器运行)
    #改动，添加上了路径
    test_data_1 = exact_traindata('./dataset/val_AES',(28,28))
    test_data_2 = exact_traindata('./dataset/val_gradient_images',(28,28))
    test_labels, test_class = label_exacted('./dataset/val_AES')



    #训练数据标签处理
    num_classes = 10
    train_labels = to_categorical(train_labels, num_classes=num_classes)
    test_labels = to_categorical(test_labels, num_classes=num_classes)

    # 记录开始时间
    start_time = time.time()

    # 训练模型
    model.fit([train_data_1, train_data_2], train_labels, epochs=50, batch_size=64, validation_data=([test_data_1, test_data_2], test_labels))

    # 记录结束时间
    end_time = time.time()

    # 计算执行时间
    execution_time = end_time - start_time

    print(f"程序执行时间: {execution_time} 秒")

    # 保存模型
    #改动，添加上了路径
    model.save('./save.h5')
