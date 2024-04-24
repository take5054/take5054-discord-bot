def phasmo(message,path):
    path += '/res/phasmo/'
    if 'DOTS' in message:
        if 'オーブ' in message:
            f = open(path+'dotso-bu.txt', 'r',encoding='utf-8')
        elif 'スピボ' in message:
            f = open(path+'dotssupi.txt', 'r',encoding='utf-8')
        elif '指紋' in message:
            f = open(path+'dotssimon.txt', 'r',encoding='utf-8')
        elif '氷点下' in message:
            f = open(path+'dotshyou.txt', 'r',encoding='utf-8')
        elif 'ライティング' in message:
            f = open(path+'dotsrai.txt', 'r',encoding='utf-8')
        elif 'EMF' in message:
            f = open(path+'dotsemf.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'error.txt','r',encoding='utf-8')
    elif 'EMF' in message:
        if 'オーブ' in message:
            f = open(path+'emfo-bu.txt', 'r',encoding='utf-8')
        elif 'スピボ' in message:
            f = open(path+'emfsupi.txt', 'r',encoding='utf-8')
        elif 'ライティング' in message:
            f = open(path+'emfrai.txt', 'r',encoding='utf-8')
        elif '指紋' in message:
            f = open(path+'emfsimon.txt', 'r',encoding='utf-8')
        elif '氷点下' in message:
            f = open(path+'emfhyou.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'error.txt','r',encoding='utf-8')
    elif 'オーブ' in message:
        if 'スピボ' in message:
            f = open(path+'o-busupi.txt', 'r',encoding='utf-8')
        elif 'ライティング' in message:
            f = open(path+'o-burai.txt', 'r',encoding='utf-8')
        elif '氷点下' in message:
            f = open(path+'o-buhyou.txt', 'r',encoding='utf-8')
        elif '指紋' in message:
            f = open(path+'o-busimon.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'error.txt','r',encoding='utf-8')
    elif 'スピボ' in message:
        if 'ライティング' in message:
            f = open(path+'supirai.txt', 'r',encoding='utf-8')
        elif '氷点下' in message:
            f = open(path+'supihyou.txt', 'r',encoding='utf-8')
        elif '指紋' in message:
            f = open(path+'supisimon.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'error.txt','r',encoding='utf-8')
    elif '指紋' in message:
        if '氷点下' in message:
            f = open(path+'simonhyou.txt', 'r',encoding='utf-8')
        elif 'ライティング' in message:
            f = open(path+'simonrai.txt', 'r',encoding='utf-8')
        else:
            f = open(path+'error.txt','r',encoding='utf-8')
    elif '氷点下' in message and 'ライティング' in message:
        f = open(path+'hyourai.txt','r',encoding='utf-8')
    else:
        f = open(path+'error.txt','r',encoding='utf-8')
    data = f.read()
    f.close()
    return(data)