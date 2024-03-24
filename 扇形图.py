import matplotlib.pyplot as plt

# 训练数据集的准确率
train_acc = [0.9192, 0.9719, 0.9797, 0.9851, 0.9870, 0.9899, 0.9907, 0.9928, 0.9941, 0.9940,
             0.9942, 0.9954, 0.9950, 0.9959, 0.9959, 0.9971, 0.9967, 0.9964, 0.9962, 0.9976,
             0.9970, 0.9967, 0.9977, 0.9964, 0.9976, 0.9975, 0.9978, 0.9974, 0.9971, 0.9979,
             0.9972, 0.9982, 0.9979, 0.9974, 0.9980, 0.9972, 0.9996, 0.9967, 0.9982, 0.9990,
             0.9984, 0.9973, 0.9985, 0.9992, 0.9969, 0.9990, 0.9981, 0.9978, 0.9979, 0.9995]

# 验证数据集的准确率
val_acc = [0.9658, 0.9743, 0.9767, 0.9787, 0.9753, 0.9820, 0.9838, 0.9808, 0.9805, 0.9793,
           0.9813, 0.9813, 0.9795, 0.9812, 0.9832, 0.9833, 0.9847, 0.9802, 0.9798, 0.9832,
           0.9838, 0.9825, 0.9787, 0.9810, 0.9828, 0.9823, 0.9770, 0.9778, 0.9827, 0.9747,
           0.9823, 0.9828, 0.9797, 0.9845, 0.9813, 0.9852, 0.9853, 0.9830, 0.9833, 0.9817,
           0.9820, 0.9808, 0.9840, 0.9793, 0.9835, 0.9833, 0.9820, 0.9830, 0.9822, 0.9823]

# 计算训练准确率和验证准确率的平均值
avg_train_acc = sum(train_acc) / len(train_acc)
avg_val_acc = sum(val_acc) / len(val_acc)

# 绘制训练准确率和验证准确率的扇形图
plt.figure(figsize=(10, 5))

# 训练准确率的扇形图
plt.subplot(1, 2, 1)
labels_train = ['Training Accuracy', '']
sizes_train = [avg_train_acc, 1 - avg_train_acc]
plt.pie(sizes_train, labels=labels_train, autopct='%1.1f%%', startangle=140)
plt.title('Average Training Accuracy')
plt.axis('equal')

# 验证准确率的扇形图
plt.subplot(1, 2, 2)
labels_val = ['Validation Accuracy', '']
sizes_val = [avg_val_acc, 1 - avg_val_acc]
plt.pie(sizes_val, labels=labels_val, autopct='%1.1f%%', startangle=140)
plt.title('Average Validation Accuracy')
plt.axis('equal')

plt.tight_layout()
plt.show()
