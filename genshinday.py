import linecache
def genshin_tenpu(i,path,today):
    if today.weekday() == 0 or today.weekday() == 3:
        if i == 0:
            temp = 'モンド：忘却の峡谷：自由'
        elif i == 1:
            temp = '璃月：太山府：繁栄'
        elif i == 2:
            temp = '稲妻：菫色ノ庭：浮世'
        elif i == 3:
            temp = 'スメール：無学の塔：忠言'
        elif i == -1:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',1).strip()
        elif i == -2:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',2).strip()
        elif i == -3:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',3).strip()
        elif i == -4:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',4).strip()
    elif today.weekday() == 1 or today.weekday() == 4:
        if i == 0:
            temp = 'モンド：忘却の峡谷：抗争'
        elif i == 1:
            temp = '璃月：太山府：勤労'
        elif i == 2:
            temp = '稲妻：菫色ノ庭：風雅'
        elif i == 3:
            temp = 'スメール：無学の塔：創意'
        elif i == -1:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',5).strip()
        elif i == -2:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',6).strip()
        elif i == -3:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',7).strip()
        elif i == -4:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',8).strip()
    elif today.weekday() == 2 or today.weekday() == 5:
        if i == 0:
            temp = 'モンド：忘却の峡谷：詩文'
        elif i == 1:
            temp = '璃月：太山府：黄金'
        elif i == 2:
            temp = '稲妻：菫色ノ庭：天光'
        elif i == 3:
            temp = 'スメール：無学の塔：篤行'
        elif i == -1:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',9).strip()
        elif i == -2:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',10).strip()
        elif i == -3:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',11).strip()
        elif i == -4:
            temp = linecache.getline(path+'/res/genshin_tenpu.txt',12).strip()
    else:
        if i == 0:
            temp = 'モンド：忘却の峡谷：自由、抗争、詩文'
        elif i == 1:
            temp = '璃月：太山府：繁栄、勤労、黄金'
        elif i == 2:
            temp = '稲妻：菫色ノ庭：浮世、風雅、天光'
        elif i == 3:
            temp = 'スメール：無学の塔：忠言、創意、篤行'
        elif i == -1:
            temp0 = linecache.getline(path+'/res/genshin_tenpu.txt',1).strip()
            temp1 = linecache.getline(path+'/res/genshin_tenpu.txt',5).strip()
            temp2 = linecache.getline(path+'/res/genshin_tenpu.txt',9).strip()
            temp = temp0 +temp1 + temp2
        elif i == -2:
            temp0 = linecache.getline(path+'/res/genshin_tenpu.txt',2).strip()
            temp1 = linecache.getline(path+'/res/genshin_tenpu.txt',6).strip()
            temp2 = linecache.getline(path+'/res/genshin_tenpu.txt',10).strip()
            temp = temp0 +temp1 + temp2
        elif i == -3:
            temp0 = linecache.getline(path+'/res/genshin_tenpu.txt',3).strip()
            temp1 = linecache.getline(path+'/res/genshin_tenpu.txt',7).strip()
            temp2 = linecache.getline(path+'/res/genshin_tenpu.txt',11).strip()
            temp = temp0 +temp1 + temp2
        elif i == -4:
            temp0 = linecache.getline(path+'/res/genshin_tenpu.txt',4).strip()
            temp1 = linecache.getline(path+'/res/genshin_tenpu.txt',8).strip()
            temp2 = linecache.getline(path+'/res/genshin_tenpu.txt',12).strip()
            temp = temp0 +temp1 + temp2
    return temp
    
def genshin_buki(i,path,today):
    if today.weekday() == 0 or today.weekday() == 3:
        if i == 0:
            temp = 'モンド：セシリアの苗床：高塔の王 <:TATE:1076413984779030568>'
        elif i == 1:
            temp = '璃月：震雷連山密宮：孤雲寒林 <:TINTIN:1076413975635439626>'
        elif i == 2:
            temp = '稲妻：砂流ノ庭：遠海夷地 <:SANGO:1076413966059831388>'
        elif i == 3:
            temp = 'スメール：有頂の塔：静謐な森のしずく <:KINHU:1076413956811399229>'
        elif i == -1:
            temp = linecache.getline(path+'/res/genshin_buki.txt',1).strip()
        elif i == -2:
            temp = linecache.getline(path+'/res/genshin_buki.txt',2).strip()
        elif i == -3:
            temp = linecache.getline(path+'/res/genshin_buki.txt',3).strip()
        elif i == -4:
            temp = linecache.getline(path+'/res/genshin_buki.txt',4).strip()
        elif i == -5:
            temp = linecache.getline(path+'/res/genshin_buki.txt',5).strip()
        elif i == -6:
            temp = linecache.getline(path+'/res/genshin_buki.txt',6).strip()
        elif i == -7:
            temp = linecache.getline(path+'/res/genshin_buki.txt',7).strip()
        elif i == -8:
            temp = linecache.getline(path+'/res/genshin_buki.txt',8).strip()
    elif today.weekday() == 1 or today.weekday() == 4:
        if i == 0:
            temp = 'モンド：セシリアの苗床：凛風奔狼 <:KIBA:1076413981536829490>'
        elif i == 1:
            temp = '璃月：震雷連山密宮：霧海雲間 <:TAMA:1076413972124811294>'
        elif i == 2:
            temp = '稲妻：砂流ノ庭：鳴神御霊 <:MAGATAMA:1076413962607939604>'
        elif i == 3:
            temp = 'スメール：有頂の塔：オアシスガーデン <:OASISU:1076413954261274695>'
        elif i == -1:
            temp = linecache.getline(path+'/res/genshin_buki.txt',9).strip()
        elif i == -2:
            temp = linecache.getline(path+'/res/genshin_buki.txt',10).strip()
        elif i == -3:
            temp = linecache.getline(path+'/res/genshin_buki.txt',11).strip()
        elif i == -4:
            temp = linecache.getline(path+'/res/genshin_buki.txt',12).strip()
        elif i == -5:
            temp = linecache.getline(path+'/res/genshin_buki.txt',13).strip()
        elif i == -6:
            temp = linecache.getline(path+'/res/genshin_buki.txt',14).strip()
        elif i == -7:
            temp = linecache.getline(path+'/res/genshin_buki.txt',15).strip()
        elif i == -8:
            temp = linecache.getline(path+'/res/genshin_buki.txt',16).strip()
    elif today.weekday() == 2 or today.weekday() == 5:
        if i == 0:
            temp = 'モンド：セシリアの苗床：獅牙戦士 <:TEJOU:1076413979200589855>'
        elif i == 1:
            temp = '璃月：震雷連山密宮：漆黒の隕鉄 <:JUUZI:1076413969956352130>'
        elif i == 2:
            temp = '稲妻：砂流ノ庭：今昔劇画 <:KAMEN:1076413959319588888>'
        elif i == 3:
            temp = 'スメール：有頂の塔：烈日権威 <:KABUTOMUSI:1076413950360559657>'
        elif i == -1:
            temp = linecache.getline(path+'/res/genshin_buki.txt',17).strip()
        elif i == -2:
            temp = linecache.getline(path+'/res/genshin_buki.txt',18).strip()
        elif i == -3:
            temp = linecache.getline(path+'/res/genshin_buki.txt',19).strip()
        elif i == -4:
            temp = linecache.getline(path+'/res/genshin_buki.txt',20).strip()
        elif i == -5:
            temp = linecache.getline(path+'/res/genshin_buki.txt',21).strip()
        elif i == -6:
            temp = linecache.getline(path+'/res/genshin_buki.txt',22).strip()
        elif i == -7:
            temp = linecache.getline(path+'/res/genshin_buki.txt',23).strip()
        elif i == -8:
            temp = linecache.getline(path+'/res/genshin_buki.txt',24).strip()
    else:
        if i == 0:
            temp = 'モンド：セシリアの苗床：高塔の王、凛風奔狼、獅牙戦士 <:TATE:1076413984779030568><:KIBA:1076413981536829490><:TEJOU:1076413979200589855>'
        elif i == 1:
            temp = '璃月：震雷連山密宮：孤雲寒林、霧海雲間、漆黒の隕鉄 <:TINTIN:1076413975635439626><:TAMA:1076413972124811294> <:JUUZI:1076413969956352130>'
        elif i == 2:
            temp = '稲妻：砂流ノ庭：遠海夷地、鳴神御霊、今昔劇画 <:SANGO:1076413966059831388><:MAGATAMA:1076413962607939604><:KAMEN:1076413959319588888>'
        elif i == 3:
            temp = 'スメール：有頂の塔：静謐な森のしずく、オアシスガーデン、烈日権威 <:KINHU:1076413956811399229><:OASISU:1076413954261274695><:KABUTOMUSI:1076413950360559657>'
        elif i == -1:
            temp0 = linecache.getline(path+'/res/genshin_buki.txt',1).strip()
            temp1 = linecache.getline(path+'/res/genshin_buki.txt',9).strip()
            temp2 = linecache.getline(path+'/res/genshin_buki.txt',17).strip()
            temp = temp0 +temp1 + temp2
        elif i == -2:
            temp0 = linecache.getline(path+'/res/genshin_buki.txt',2).strip()
            temp1 = linecache.getline(path+'/res/genshin_buki.txt',10).strip()
            temp2 = linecache.getline(path+'/res/genshin_buki.txt',18).strip()
            temp = temp0 +temp1 + temp2
        elif i == -3:
            temp0 = linecache.getline(path+'/res/genshin_buki.txt',3).strip()
            temp1 = linecache.getline(path+'/res/genshin_buki.txt',11).strip()
            temp2 = linecache.getline(path+'/res/genshin_buki.txt',19).strip()
            temp = temp0 +temp1 + temp2
        elif i == -4:
            temp0 = linecache.getline(path+'/res/genshin_buki.txt',4).strip()
            temp1 = linecache.getline(path+'/res/genshin_buki.txt',12).strip()
            temp2 = linecache.getline(path+'/res/genshin_buki.txt',20).strip()
            temp = temp0 +temp1 + temp2
        elif i == -5:
            temp0 = linecache.getline(path+'/res/genshin_buki.txt',5).strip()
            temp1 = linecache.getline(path+'/res/genshin_buki.txt',13).strip()
            temp2 = linecache.getline(path+'/res/genshin_buki.txt',21).strip()
            temp = temp0 +temp1 + temp2
        elif i == -6:
            temp0 = linecache.getline(path+'/res/genshin_buki.txt',6).strip()
            temp1 = linecache.getline(path+'/res/genshin_buki.txt',14).strip()
            temp2 = linecache.getline(path+'/res/genshin_buki.txt',22).strip()
            temp = temp0 +temp1 + temp2
        elif i == -7:
            temp0 = linecache.getline(path+'/res/genshin_buki.txt',7).strip()
            temp1 = linecache.getline(path+'/res/genshin_buki.txt',15).strip()
            temp2 = linecache.getline(path+'/res/genshin_buki.txt',23).strip()
            temp = temp0 +temp1 + temp2
        elif i == -8:
            temp0 = linecache.getline(path+'/res/genshin_buki.txt',8).strip()
            temp1 = linecache.getline(path+'/res/genshin_buki.txt',16).strip()
            temp2 = linecache.getline(path+'/res/genshin_buki.txt',24).strip()
            temp = temp0 +temp1 + temp2
    return(temp)