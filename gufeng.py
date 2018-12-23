import random

words2 = ["朱砂","天下","杀伐","人家","韶华",
         "风华","繁华","血染","墨染","白衣",
         "素衣","嫁衣","倾城","孤城","空城",
         "旧城","旧人","伊人","心疼","春风",
         "古琴","无情","迷离","奈何","断弦",
         "焚尽","散乱","陌路","乱世","笑靥",
         "浅笑","明眸","轻叹","烟火","一生",
         "三生","浮生","桃花","梨花","落花",
         "烟花","离殇","情殇","爱殇","剑殇",
         "灼伤","仓皇","匆忙","陌上","清商",
         "焚香","墨香","微凉","断肠","痴狂",
         "凄凉","黄梁","未央","成双","无恙",
         "虚妄","凝霜","洛阳","长安","江南",
         "忘川","千年","纸伞","烟雨","回眸",
         "公子","红尘","红颜","红衣","红豆",
         "红线","青丝","青史","青冢","白发",
         "白首","白骨","黄土","黄泉","碧落",
         "紫陌"]
words4 = ["情深缘浅","情深不寿","莫失莫忘","阴阳相隔","如花美眷",
          "似水流年","眉目如画","曲终人散","繁华落尽","不诉离殇",
          "一世长安"]

len2 = len(words2)
len4 = len(words4)

def getW2():
    return words2[random.randint(0,len2-1)]

def getW4():
    a = random.randint(0,1)
    if a==0:
        return getW2()+getW2()
    else:
        return words4[random.randint(0,len4-1)]

def get1():
    # XX, XX, XX了xX.
    return getW2()+"，"+getW2()+"，"+getW2()+"了"+getW2()+"。"

def get2():
    # XXXX, XXxx, 不过是一场xxxx.
    return getW4()+"，"+getW4()+"，不过是一场"+getW4()+"。"

def get3():
    # 你说xxxx, 我说xxxx, 最后不过xxxx.
    return "你说"+getW4()+"，我说"+getW4()+"，最后不过"+getW4()+"。"

def get4():
    # xx, Xx, 许我一场xxxx.
    return getW2()+"，"+getW2()+"，许我一场"+getW4()+"。"

def get5():
    # 你说xxxx xxxx, 后来xxxx xxxx.
    return "你说"+getW4()+getW4()+"，后来"+getW4()+getW4()+"。"

def get6():
    # xxXX, Xxxx, 终不敌xxxx.
    return getW4()+"，"+getW4()+"，终不敌"+getW4()+"。"

'''
def get7():
    # 一X一X一XX, 半x半x半xx.
    return "一"+get
'''

def getSentence(sentNum=1):
    total = ""
    for i in range(sentNum):
        a = random.randint(1,6)
        if a==1:
            total += get1()+"\n"
        if a==2:
            total += get2()+"\n"
        if a==3:
            total += get3()+"\n"
        if a==4:
            total += get4()+"\n"
        if a==5:
            total += get5()+"\n"
        if a==6:
            total += get6()+"\n"
    return total

if __name__ == "__main__":
    print(getSentence(20))
