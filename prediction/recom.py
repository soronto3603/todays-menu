from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import load_model

model = Sequential()
model.add(Dense(5, input_dim=5, activation='sigmoid'))
model.add(Dense(128, activation='sigmoid'))
model.add(Dense(256, activation='sigmoid'))
model.add(Dense(38, activation='softmax'))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
model.summary()

x = [[   3 ,   7 ,2019  ,  2 ,  25],
    [   2  ,  0 ,2019   , 4  , 31],
    [   4  ,  4 ,2019  ,  5  ,  8]]

model.load_weights('../model/weights/today20190320132654.h5')
y=model.predict(x)
print(y)