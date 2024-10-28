

print("為旅客找到合適、口俾良好且便捷交通之著名餐廳。")

#收集顧客數據
age = int(input("請問您幾歲？"))
if age >=0 and age <= 11 :
    print(age,"歲","的國小生")
elif age >11 and age <= 15:
    print(age,"歲","的國中生")
elif age >15 and age <18:
    print(age,"歲","的高中生")
elif age >=18 and age <=27:
    print(age,"歲","的大專生或研究生")
elif age > 27 and age <60:
    print(age,"歲","的社會人仕")
else:
    print(age,"歲","的長者")


city_1 = ["台北市", "新北市", "桃園市", "新竹市", "基隆市", "宜蘭縣", "新竹縣"]
city_2 = ["台中市", "苗栗縣", "彰化縣", "南投縣", "雲林縣"]
city_3 = ["高雄市", "台南市", "嘉義市", "屏東縣", "澎湖縣"]
city_4 = ["花蓮縣", "台東縣"]
city_5 = ["金門縣", "連江縣"]
city_6 = ["其他國家"]

while True:
    home = input("請問您住哪？請輸入全寫（例：台北市）：")
    if home in city_1:
        print("歡迎來到台中，北部居民")
        break
    elif home in city_2:
        print("歡迎來到台中，中部居民")
        break
    elif home in city_3:
        print("歡迎來到台中，南部居民")
        break
    elif home in city_4:
        print("歡迎來到台中，東部居民")
        break
    elif home in city_5:
        print("歡迎來到台中，外島居民")
        break
    elif home in city_6:
        print("歡迎國際旅客列台中")
        break
    else:
        print("只能限台灣縣市，請重新輸入。")




#問卷
resturant_1 = int(input("請問您認為餐廳服務態度如何？（1為不滿意；5為最滿意）："))
resturant_2 = int(input("餐廳菜色品質如何？（1為不滿意；5為最滿意）："))
resturant_3 = int(input("請問您認為餐廳價值合理嗎？（1為不滿意；5為最滿意）："))
resturant_4 = int(input("請問您認為餐廳還境（包括週邊生活機能）如何？（1為不滿意；5為最滿意）："))
    
totel = resturant_1 + resturant_2 + resturant_3 + resturant_4

while totel > 20:
    print("請輸入範圍內的數字（1～5），謝謝！")
    resturant_1 = int(input("請問您認為餐廳服務態度如何？（1為不滿意；5為最滿意）："))
    resturant_2 = int(input("餐廳菜色品質如何？（1為不滿意；5為最滿意）："))
    resturant_3 = int(input("請問您認為餐廳價值合理嗎？（1為不滿意；5為最滿意）："))
    resturant_4 = int(input("請問您認為餐廳環境（包括週邊生活機能）如何？（1為不滿意；5為最滿意）："))
        
    totel = int(resturant_1 + resturant_2 + resturant_3 + resturant_4)
else:
    print("顧客評分：",totel, "，" ,"謝謝您的保貴意見！")


