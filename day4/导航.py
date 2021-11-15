citys = {
    "北京":{
        "朝阳":{"望京","广顺桥","SOHO"},
        "昌平":{"北科","回龙观","白各庄"},
        "顺义":{"解放军空军基地","光之国","野长城"},
        "海淀":{"清华","中关村","上地街"}
    },
    "上海":{
        "浦东新区":{"外滩","迪士尼","豫园"},
        "静安":{"静安寺","新天地","人民广场"}
    },
    "广州":{"中山纪念堂","荔枝湾","白云山"}
}

def lencitys(citys):
    print("-------进入导航-------")
    for i in citys:
        print(i)
    print("-------------------")

shop = [
        ["鼠标", 50],
        ["键盘", 100],
        ["辣条", 10],
        ["小浣熊方便面", 15],
        ["珍视明滴眼液", 25],
        ["水杯", 1],
        ["大宝SOD密", 50000000000000000000],
        ["机械革命", 0.1]
    ]  # 货架

def lenshop(shop):

    import random  # 随机优惠券数量
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 20)

    mycar = []  # 购物车

    #
    # moneybag = ['请输入你的钱：']
    # moneybag = input(moneybag)
    # moneybag = int(moneybag)
    # mg = moneybag
    # print('获得辣条优惠券',num1)
    # print('获得机械革命优惠券',num2)
    print('您获得辣条优惠券 %d张'"      "'您获得机械革命优惠券 %d张' % (num1, num2))
    while True:
        moneybag = input('your money')  # 输入并判断钱包
        if moneybag.isdigit():
            moneybag = int(moneybag)
            mg = moneybag

            while True:
                for key, value in enumerate(shop):  # 显示角标和名字
                    print(key, value)

                chose = input('你需要什么？')  # 输入角标
                if chose.isdigit():  # 检测字符串是否纯数字组成
                    chose = int(chose)
                    if chose >= len(shop):  # 输入大于等于列表
                        print('no')
                    else:
                        if mg < shop[chose][1]:
                            print('no money')
                        # else:
                        #     mycar.append(shop[chose][0])
                        #     mg = mg - shop[chose][1]
                        #     print("monney:", mg)
                        elif chose == 2 and num1 > 0:  # 判断是否有优惠券且选中商品是辣条
                            mycar.append(shop[chose][0])
                            mg = mg - shop[chose][1] * 0.3
                            print('money:', mg)
                        elif chose == 7 and num2 > 0:  # 判断是否有优惠券且选中商品是机械革命
                            mycar.append(shop[chose][0])
                            mg = mg - shop[chose][1] * 0.9
                            print('money:', mg)
                        else:
                            mycar.append(shop[chose][0])
                            mg = mg - shop[chose][1]
                            print("monney:", mg)
                elif chose == "q" or chose == "Q":
                    print('thanks')

                    break
                else:
                    print('没有此物')
            # 打印购物小条
            print("----------------欢迎下次光临购物商城--------------")
            print("以下是您的购物小条，请拿好：")
            print("--------------------------------------------------")
            # for key, value in enumerate(mycar):
            #     print(key, value)
            m = []
            for i in mycar:
                if i not in m:
                    m.append(i)
                    print(" %s x %s " % (i, mycar.count(i)))
                else:
                    continue
            print("-------------------------------------------------")
            print("您本次还剩余额为：￥", mg, "，本次消费：￥", (moneybag - mg))

        elif moneybag == "q" or "Q":
            print('thanks')
            break



while True:
    lencitys(citys)
    chose = input("去哪里请输入")

    if chose == "q" or chose == "Q":
        print("thanks")
        break
    if chose not in citys:
        print("sorry")
    else:
        lencitys(citys[chose])
        chose2 = input("去哪里请输入")
        if chose2 == "q" or chose == "Q":
            print("tkanks")
            break
        if chose2 not in citys[chose]:
            print("sorry")
        else:
            lencitys(citys[chose][chose2])
            chose3 = input("请输入去哪里")
            if chose3 == "q" or chose == "Q":
                print("thanks")
                break
            if chose3 not in citys[chose][chose2]:
                print("sorry")
            else:
                lencitys(citys[chose][chose2])
                print("已到达")

                test = input("需要购买礼物吗")
                if test == "no":
                    print("thanks")
                else:
                    lenshop(shop)







