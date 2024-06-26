# -*- coding: utf-8 -*-
"""sigmoid.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IN1bI1uzIr_wuaMnqynSrWQIkTcYV1tn
"""

import numpy as np
import tensorflow as tf

from keras import Sequential
from keras.layers import Flatten,Dense
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

df=load_breast_cancer()

X_train,X_test,y_train,y_test=train_test_split(df.data,df.target,test_size=0.20,random_state=0)
sc=StandardScaler()

X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

model=Sequential([
    Flatten(input_shape=(X_train.shape[1],)),
    Dense(1,activation='sigmoid')
])

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(X_train,y_train,epochs=5)
test_loss,test_accuracy=model.evaluate(X_test,y_test)
print(test_loss)
print(test_accuracy)

