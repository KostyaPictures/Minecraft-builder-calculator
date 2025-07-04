from winreg import *

def ask():
    new_key = CreateKey(HKEY_CURRENT_USER, "SOFTWARE\MinecraftCalc")
    try:
        lang_reg, regtype = QueryValueEx(new_key, "lang_reg")
    except FileNotFoundError:
        SetValueEx(new_key, "lang_reg", 0, REG_SZ, "0")
    
    if lang_reg=="0":
        while True:
            print("select your language//выберите язык\nen/ru    анг/рус")
            lang=input()
            if lang=="ru" or lang=="en" or lang=="анг" or lang=="рус":
                break
        if lang=="en" or lang=="анг":
            SetValueEx(new_key, "lang_reg", 0, REG_SZ, "1")
        if lang=="ru" or lang=="рус":
            SetValueEx(new_key, "lang_reg", 0, REG_SZ, "2")
    
    lang_reg, regtype = QueryValueEx(new_key, "lang_reg")
    return lang_reg