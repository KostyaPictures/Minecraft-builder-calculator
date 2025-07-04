from winreg import CreateKey, QueryValueEx, HKEY_CURRENT_USER

def MainMode(InputBlockCount):
    new_key = CreateKey(HKEY_CURRENT_USER, "SOFTWARE\MinecraftCalc")
    MainMode, regtype = QueryValueEx(new_key, "Mode")
    ibs = InputBlockCount
    if MainMode=="0":
        #Перевести n блоков в x изделий
        #Ступеньки
        stairs=(ibs//6)*4
        #Плиты
        slabs=(ibs//3)*6
        #Заборы
        fences=(ibs//10)*6
        sticks=(ibs//5)
        #Калитки
        gates=(ibs//4)*1
        #Двери
        doors=(ibs//6)*3
        #Люки
        traps=(ibs//6)*2
        #Пластины
        plates=(ibs//2)*1
        #Кнопки
        buttons=ibs
        #Ограды
        walls=(ibs//6)*6
        return stairs, slabs, fences, sticks, gates, doors, traps, plates, buttons, walls
    if MainMode=="1":
        #Расчитать сколько блоков нужно на n изделий (Если вам нужно столько чего-то, то вам нужно N блоков)
        #Ступеньки
        if ibs>=4:
            if ibs%4==0:
                stairs=(ibs//4)*6
            if ibs%4!=0:
                stairs=(ibs//4+1)*6
        else:
            stairs=0
        #Плиты
        if ibs>=6:
            if ibs%6==0:
                slabs=(ibs//6)*3
            if ibs%6!=0:
                slabs=(ibs//6+1)*3
        else:
            slabs=0
        #Заборы
        if ibs>=6:
            if ibs%6==0:
                fences=(ibs//6)*10
                sticks=(ibs//5) #(из STICKS из этих блоков нужно следать палки)
            if ibs%6!=0:
                fences=(ibs//6+1)*10
                sticks=(ibs//5+1)
        else:
            fences=0
            sticks=0
        #Калитки
        if ibs>=1:
            if ibs%1==0:
                gates=(ibs//1)*4
            if ibs%1!=0:
                gates=(ibs//1+1)*4
        else:
            gates=0
        #Двери
        if ibs>=3:
            if ibs%3==0:
                doors=(ibs//3)*6
            if ibs%3!=0:
                doors=(ibs//3+1)*6
        else:
            doors=0
        #Люки
        if ibs>=2:
            if ibs%2==0:
                traps=(ibs//2)*6
            if ibs%2!=0:
                traps=(ibs//2+1)*6
        else:
            traps=0
        #Пластины
        if ibs>=1:
            if ibs%1==0:
                plates=(ibs//1)*2
            if ibs%1!=0:
                plates=(ibs//1+1)*2
        else:
            plates=0
        #Кнопки
        buttons=ibs
        #Ограды
        if ibs>=6:
            if ibs%6==0:
                walls=(ibs//6)*6
            if ibs%6!=0:
                walls=(ibs//6+1)*6
        else:
            walls=0
        return stairs, slabs, fences, sticks, gates, doors, traps, plates, buttons, walls