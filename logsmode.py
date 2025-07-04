from winreg import CreateKey, QueryValueEx, HKEY_CURRENT_USER

def LogsMode(planks):
    new_key = CreateKey(HKEY_CURRENT_USER, "SOFTWARE\MinecraftCalc")
    LogsMode, regtype = QueryValueEx(new_key, "Mode4")
    if LogsMode=="1":
        logs=""
        if planks%4==0:
            logs=str(planks//4)
        if planks%4>0:
            logs=str((planks//4)+1)
        return int(logs)
    if LogsMode=="0":
        return int(planks)