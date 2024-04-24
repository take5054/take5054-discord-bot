def phasmo(message,path):
    if 'DOTS' in message:
        if 'オーブ' in message:
            f = open(path+'/res/dotso-bu.txt', 'r',encoding='utf-8')
        elif 'スピボ' in message:
            f = open(path+'/res/dotssupi.txt', 'r',encoding='utf-8')
        elif '指紋' in message:
            f = open(path+'/res/dotssimon.txt', 'r',encoding='utf-8')
        elif '氷点下' in message:
            f = open(path+'/res/dotshyou.txt', 'r',encoding='utf-8')
        elif 'ライティング' in message:
            f = open(path+'/res/dotsrai.txt', 'r',encoding='utf-8')
        elif 'EMF' in message:
            f = open(path+'/res/dotsemf.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'/res/error.txt','r',encoding='utf-8')
    elif 'EMF' in message:
        if 'オーブ' in message:
            f = open(path+'/res/emfo-bu.txt', 'r',encoding='utf-8')
        elif 'スピボ' in message:
            f = open(path+'/res/emfsupi.txt', 'r',encoding='utf-8')
        elif 'ライティング' in message:
            f = open(path+'/res/emfrai.txt', 'r',encoding='utf-8')
        elif '指紋' in message:
            f = open(path+'/res/emfsimon.txt', 'r',encoding='utf-8')
        elif '氷点下' in message:
            f = open(path+'/res/emfhyou.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'/res/error.txt','r',encoding='utf-8')
    elif 'オーブ' in message:
        if 'スピボ' in message:
            f = open(path+'/res/o-busupi.txt', 'r',encoding='utf-8')
        elif 'ライティング' in message:
            f = open(path+'/res/o-burai.txt', 'r',encoding='utf-8')
        elif '氷点下' in message:
            f = open(path+'/res/o-buhyou.txt', 'r',encoding='utf-8')
        elif '指紋' in message:
            f = open(path+'/res/o-busimon.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'/res/error.txt','r',encoding='utf-8')
    elif 'スピボ' in message:
        if 'ライティング' in message:
            f = open(path+'/res/supirai.txt', 'r',encoding='utf-8')
        elif '氷点下' in message:
            f = open(path+'/res/supihyou.txt', 'r',encoding='utf-8')
        elif '指紋' in message:
            f = open(path+'/res/supisimon.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'/res/error.txt','r',encoding='utf-8')
    elif '指紋' in message:
        if '氷点下' in message:
            f = open(path+'/res/simonhyou.txt', 'r',encoding='utf-8')
        elif 'ライティング' in message:
            f = open(path+'/res/simonrai.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'/res/error.txt','r',encoding='utf-8')
    elif '氷点下' in message and 'ライティング' in message:
        f = open(path+'/res/hyourai.txt','r',encoding='utf-8')
    else:
        f = open(path+'/res/error.txt','r',encoding='utf-8')
    data = f.read()
    f.close()
    return(data)