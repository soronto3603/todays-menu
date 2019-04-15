"""
python tm.py --input ../dataset_test/12032030.csv --output today
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import datetime

# 랜덤시드 고정시키기
np.random.seed(5)

# 원래의 코드
# dataset = np.loadtxt("./warehouse/pima-indians-diabetes.data", delimiter=",")

def division_datetime(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    day = date.strftime("%A")
    month = date.strftime("%B")
    year = date.strftime("%Y")
    return day,month,year

month=["January","February","March","April","May","June","July","August","September","October","November","December"]
month2int = {}
int2month = {}
for idx,x in enumerate(month):
    month2int[x] = idx
    int2month[idx] = x


weekday=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day2int = {}
int2day = {}
for idx,x in enumerate(weekday):
    day2int[x] = idx
    int2day[idx] = x

# len 38
menu=[    
    "떡볶이","피자","치킨","파스타","스테이크","짜장면","짬뽕","탕수육","덮밥",
    "오므라이스","샐러드","김밥","라면","어묵","국수","냉면","만두","떡국","파전 with 막걸리",
    "고기","라면","제육볶음","초밥","비빔밥","불고기","국밥","쭈꾸미 볶음","굶어",
    "족발","보쌈","돈까스","부대찌개","도시락","순대","매운닭발","튀김","쫄면",
    "함박스테이크"
]

menu2int = {}
int2menu = {}
for idx,x in enumerate(menu):
    menu2int[x] = idx
    int2menu[idx] = x

#  len 53
weather=[
    "thunderstorm with light rain","thunderstorm with rain","thunderstorm with heavy rain",
    "light thunderstorm","thunderstorm","heavy thunderstorm","ragged thunderstorm","thunderstorm with light drizzle",
    "thunderstorm with drizzle","thunderstorm with heavy drizzle","light intensity drizzle","drizzle",
    "heavy intensity drizzle","light intensity drizzle rain","drizzle rain","heavy intensity drizzle rain","shower rain and drizzle"
    "heavy shower rain and drizzle","shower drizzle","light rain","moderate rain","heavy intensity rain","very heavy rain","extreme rain"
    "freezing rain","light intensity shower rain","shower rain","heavy intensity shower rain","ragged shower rain",
    "light snow","Snow","Heavy snow","Sleet","Light shower sleet","Shower sleet","Light rain and snow","Rain and snow","Light shower snow",
    "Shower snow","Heavy shower snow","mist","Smoke","Haze","sand/ dust whirls","fog",
    "sand","dust","volcanic ash","squalls","tornado","clear sky","few clouds","scattered clouds","broken clouds","overcast clouds"
]

weather2int = {}
int2weather = {}
for idx,x in enumerate(weather):
    weather2int[x] = idx
    int2weather[idx] = x

#  len 7
emotion=[
    "좋음","나쁨","더러움","화남","짜증남","슬픔","술땡김"
]

emotion2int = {}
int2emotion = {}
for idx,x in enumerate(emotion):
    emotion2int[x] = idx
    int2emotion[idx]= x




if __name__ == '__main__':
    import argparse
    import os

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="today_menu_random_data_generator")
    # parser.add_argument('--input',required=True,metavar="ex)12032019.csv",help="파일이름")

    args=parser.parse_args()
    
    dataset_path="../dataset_test/"
    file_list = next(os.walk(dataset_path))[2]
    file_list.sort()

    print("선택된 데이터 리스트 :")
    print(file_list)
    dataset = []
    import pandas as pd
    for f in file_list:
        if f.endswith(".csv"):

            data = pd.read_csv(dataset_path+f, delimiter=",")
            data = data.values
            for r in data:
                row = []
                r[0]=int(r[0])
                day, month, year = division_datetime(r[0])
                row.append(day2int[day])
                row.append(month2int[month])
                row.append(int(year))
                row.append(emotion2int[r[1]])
                row.append(weather2int[r[2]])
                row.append(menu2int[r[3]])
                dataset.append(row)

    print("총 데이터 수 : "+str(len(dataset)))

    dataset = np.asarray( dataset )
    x_train = dataset[:700,0:5]
    y_train = dataset[:700,5]
    x_test = dataset[700:,0:5]
    y_test = dataset[700:,5]

    # print("X_TRAIN : ",x_train)
    # print("Y_TRAIN : ",y_train)
    print(len(x_test[0]),len(x_test))
    print("X_TEST : ", x_test)

    # x_test = [[   1 ,   0 ,2019  ,  4 ,  52],
    #             [   6   , 0 ,2019  ,  0  , 22],
    #             [   6  ,  0 ,2019  ,  0 ,  15]]
    # x_test = np.asarray( x_test )
    # [[   1    0 2019    4   52]
    #  [   6    0 2019    0   22]
    #  [   6    0 2019    0   15]]

    """
    >>>>>
    [1546937040.0=>YY,MM,DD, '슬픔', 'Haze', '짜장면'],

    x >>
    [   5    6 2019    1    9]
    [   5    0 2019    5    4]]
    y >>
    30 32  5 31  8  0  0 28 20
    """

    model = Sequential()
    model.add(Dense(5, input_dim=5, activation='sigmoid'))
    model.add(Dense(128, activation='sigmoid'))
    model.add(Dense(256, activation='sigmoid'))
    model.add(Dense(38, activation='softmax'))

    model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
    model.summary()
    model.fit(x_train, y_train, epochs=1500, batch_size=64)

    # [[   1    0 2019    4   52]
    #  [   6    0 2019    0   22]
    #  [   6    0 2019    0   15]]

    scores = model.evaluate(x_test, y_test)
    print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

    x_test = [[   1 ,   0 ,2019  ,  4 ,  52],
            [   6   , 0 ,2019  ,  0  , 22],
            [   6  ,  0 ,2019  ,  0 ,  15],
            [ 0 , 3 ,2019 , 1, 0]]
    x_test = np.asarray( x_test )

    pred = model.predict_classes(x_test)
    print(pred)

    while(True):
        a= [input().split(" ")]
        x_test = np.asarray( a) 
        pred = model.predict_classes(x_test)
        for i in pred:
            print(int2menu[i])
        
        
        