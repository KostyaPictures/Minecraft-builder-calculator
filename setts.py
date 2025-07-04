from winreg import *



def ask():
    from main import current_lang
    if current_lang=="1":
        a1="Reset config?\n(1)Yes (2)No (3)No, don't ask again (4) reset language+settings"
        b1="What do you want to do?\n(1) Transfer \"n\" blocks into strairs, slabs, etc. (2) Calculate how many blocks is needed for \"n\" strairs, slabs, etc."
        c1="In which system to calculate?\n(1)In planks (2)In logs"
        d1="Divide the number into units? (135 blocks -> 2 stacks 7 blocks)\n(1)Don't need (2)Yes"
    if current_lang=="2":
        a1="Сбросить настройки?\n(1)Да (2)Нет (3)Нет, больше не спрашивать (4) сбросить язык+настройки"
        b1="Что вы хотите?\n(1) Перевести n блоков в изделия (2) Расчитать сколько блоков нужно на n изделий"
        c1="В чём вычислять?\n(1)В досках (2)В брёвнах"
        d1="Сделать число удобным? (135 блоков -> 2 стака 7 блоков)\n(1)Не нужно (2)Да"
    
    
    new_key = CreateKey(HKEY_CURRENT_USER, "SOFTWARE\MinecraftCalc")



    try:
        AskAgain, regtype = QueryValueEx(new_key, "AskAgain")
    except FileNotFoundError:
        SetValueEx(new_key, "AskAgain", 0, REG_SZ, "1")
        SetValueEx(new_key, "Mode", 0, REG_SZ, "2")
        SetValueEx(new_key, "Mode4", 0, REG_SZ, "2")
        SetValueEx(new_key, "Compact", 0, REG_SZ, "2")

    if AskAgain=="1":
        while True:
            choise=int(input(a1))
            if choise==1:
                SetValueEx(new_key, "Mode", 0, REG_SZ, "2")
                SetValueEx(new_key, "Mode4", 0, REG_SZ, "2")
                SetValueEx(new_key, "Compact", 0, REG_SZ, "2")
                break
            if choise==2:
                break
            if choise==3:
                SetValueEx(new_key, "AskAgain", 0, REG_SZ, "0")
                break
            if choise==4:
                SetValueEx(new_key, "lang_reg", 0, REG_SZ, "0")
                SetValueEx(new_key, "Mode", 0, REG_SZ, "2")
                SetValueEx(new_key, "Mode4", 0, REG_SZ, "2")
                SetValueEx(new_key, "Compact", 0, REG_SZ, "2")
                from main import l
                l()
                break

    key = OpenKey(HKEY_CURRENT_USER, "SOFTWARE")






    Mode, regtype = QueryValueEx(new_key, "Mode")
    if Mode=="2":
        while True:
            choise=int(input(b1))
            if choise==1:
                SetValueEx(new_key, "Mode", 0, REG_SZ, "0")
                break
            if choise==2:
                SetValueEx(new_key, "Mode", 0, REG_SZ, "1")
                break


    Mode4, regtype = QueryValueEx(new_key, "Mode4")
    if Mode4=="2":
        while True:
            choise=int(input(c1))
            if choise==1:
                SetValueEx(new_key, "Mode4", 0, REG_SZ, "0")
                break
            if choise==2:
                SetValueEx(new_key, "Mode4", 0, REG_SZ, "1")
                break

    Compact, regtype = QueryValueEx(new_key, "Compact")
    if Compact=="2":
        while True:
            choise=int(input(d1))
            if choise==1:
                SetValueEx(new_key, "Compact", 0, REG_SZ, "0")
                break
            if choise==2:
                SetValueEx(new_key, "Compact", 0, REG_SZ, "1")
                break

    MainMode, regtype = QueryValueEx(new_key, "Mode")
    LogsMode, regtype = QueryValueEx(new_key, "Mode4")
    Compact, regtype = QueryValueEx(new_key, "Compact")
    return MainMode, LogsMode, Compact