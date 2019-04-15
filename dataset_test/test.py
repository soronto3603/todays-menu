import csv

with open("12032019.csv","r",encoding="utf-8") as f:
    rdr = csv.reader(f)
    for line in rdr:
        print(line)
    
"""
데이터 이상 없긴한데... 빈칸나옴ㅁ.. 신경쓰임
['1547972040.0', '나쁨', 'heavy intensity drizzle rain', '샐러드']
[]
['1546429680.0', '나쁨', 'Snow', '어묵']
[]
['1547867220.0', '나쁨', 'heavy intensity drizzle', '부대찌개']
[]
['1548981720.0', '좋음', 'heavy intensity rain', '피자
"""