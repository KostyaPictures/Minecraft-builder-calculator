from winreg import CreateKey, QueryValueEx, HKEY_CURRENT_USER







def Compact(ToConvert):
    from main import current_lang
    if current_lang=="1":
        a1="You don't need any blocks, or there is a mistake"
        b1=" Double chests "
        b2=" Chests "
        b3=" Stacks "
    if current_lang=="2":
        a1="Блоков не понадобится, либо произошла ошибка"
        b1=" Двойных сундуков "
        b2=" Сундуков "
        b3=" Стаков "

    
    new_key = CreateKey(HKEY_CURRENT_USER, "SOFTWARE\MinecraftCalc")
    Compact, regtype = QueryValueEx(new_key, "Compact")


    if ToConvert==0:
        return a1
    elif ToConvert<0 or type(ToConvert)!=int:
        return "Error: Non-Natural \"ToConvert\" value. (compact.py)"
    elif Compact=="1":
        Converted=""
        if ToConvert/3456>=1:
            Converted+=str(ToConvert//3456)+b1
            ToConvert%=3456
        if ToConvert/1728>=1 and ToConvert!=0:
            Converted+=str(ToConvert//1728)+b2
            ToConvert%=1728
        if ToConvert/64>=1 and ToConvert!=0:
            Converted+=str(ToConvert//64)+b3
            ToConvert%=64
        if ToConvert>=1:
            Converted+=str(ToConvert)+" "

        return Converted
    elif Compact=="0":
        return ToConvert
    else:
        return ToConvert