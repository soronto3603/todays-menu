"""
python datagen.py --filename "15032019.csv" --number 10
"""

import random
import datetime 
import csv

# len 38
menu=[    
    "떡볶이","피자","치킨","파스타","스테이크","짜장면","짬뽕","탕수육","덮밥",
    "오므라이스","샐러드","김밥","라면","어묵","국수","냉면","만두","떡국","파전 with 막걸리",
    "고기","라면","제육볶음","초밥","비빔밥","불고기","국밥","쭈꾸미 볶음","굶어",
    "족발","보쌈","돈까스","부대찌개","도시락","순대","매운닭발","튀김","쫄면",
    "함박스테이크"
]

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

#  len 7
emotion=[
    "좋음","나쁨","더러움","화남","짜증남","슬픔","술땡김"
]

"""
특정 일로부터 timestamp generator
startDate = datetime.datetime(2019, 1, 1, 00)
for x in reversed(list(random_date(startDate,10))):
    print x.strftime("%d/%m/%y %H:%M")
>>>>>
20/09/13 13:45
20/09/13 13:36
20/09/13 13:29
20/09/13 13:25
20/09/13 13:20
20/09/13 13:19
20/09/13 13:16
20/09/13 13:16
20/09/13 13:07
20/09/13 13:03
20/09/13 13:01
"""
def random_date(start,l):
    current = start
    while l >= 0:
        current = current + datetime.timedelta(minutes=random.randrange(1000))
        yield current
        l-=1

"""
# print(gen_data(100))
>>>>>
[1546937040.0, '슬픔', 'Haze', '짜장면'], 
[1546371540.0, '좋음', 'light rain', '덮밥'],
[1546650360.0, '짜증남', 'Rain and snow', '김밥'], 
[1547389800.0, '더러움', 'dust', '쭈꾸미 볶음'], 
[1547172840.0, '슬픔', 'broken clouds', '고기'] ...
"""
def gen_data(cap):
    startDate = datetime.datetime(2019, 1, 1, 00)
    time_data = list(random_date(startDate,cap))
    datas = []
    for x in range(cap):
        datas.append([random.choice(time_data).timestamp(),random.choice(emotion),random.choice(weather),random.choice(menu)])
    
    return datas


def save_data(data,path):
    with open(path,'w',encoding='utf-8') as f:
        wr =  csv.writer(f)
        for x in data:
            wr.writerow(x)

# center_date = 19
# for x in range(10):
#     save_data(gen_data(100),"120320"+str(center_date+x)+".csv")


if __name__ == '__main__':
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="today_menu_random_data_generator")
    parser.add_argument('--filename',required=True,metavar="ex)12032019.csv",help="파일이름")
    parser.add_argument('--number',required=True,metavar="ex)100",help="데이터 개수")

    args=parser.parse_args()


    save_data(gen_data(int(args.number)),args.filename)
    