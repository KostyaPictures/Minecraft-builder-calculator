from winreg import CreateKey, QueryValueEx, HKEY_CURRENT_USER


import lang

def l():
    global current_lang
    current_lang=lang.ask()
l()

if current_lang=="1":
    a1="You can craft:\neither "
    a2=" Stairs, \nor "
    a3=" Slabs, \nor "
    a4=" Fences (Need to craft "
    a5=" blocks into sticks), \nor "
    a6=" Gates (spend half of it on sticks), \nor "
    a7=" Doors, \nor "
    a8=" Trapdoors, \nor "
    a9=" Pressure plates, \nor "
    a10=" Buttons, \nor "
    a11=" Walls."
    b1="If you need "
    b2=" Stairs, then you need "
    b3_5_8_12_14_16_18="Blocks, \n"+"If you need "
    b4=" Slabs, then you need "
    b6=" Fences, then you need "
    b7="Blocks (spend "
    b8=" blocks on sticks), \n"+"If you need "
    b9=" Gates, then you need "
    b10="Blocks (spend half of it on sticks), \n"+"If you need "
    b11=" Doors, then you need "
    b13=" Trapdoors, then you need "
    b15=" Pressure plates, then you need "
    b17=" Buttons, then you need "
    b19=" Walls, then you need "
    b20="Blocks"
if current_lang=="2":
    a1="Вы можете скрафтить:\nлибо "
    a2=" Ступенек, \nлибо "
    a3=" Плит, \nлибо "
    a4=" Заборов (при этом скрафтив из "
    a5=" блоков палки), \nлибо "
    a6=" Калиток (потратив половину на палки), \nлибо "
    a7=" Дверей, \nлибо "
    a8=" Люков, \nлибо "
    a9=" Нажимных пластин, \nлибо "
    a10=" Кнопок, \nлибо "
    a11=" Стен."
    b1="Если вам нужно "
    b2=" Ступенек, то вам понадобится "
    b3_5_8_12_14_16_18="Блоков, \n"+"Если вам нужно "
    b4=" Плит, то вам понадобится "
    b6=" Заборов, то вам понадобится "
    b7="Блоков (при этом потратив "
    b8=" из них на палки), \n"+"Если вам нужно "
    b9=" Калиток, то вам понадобится "
    b10="Блоков (при этом потратив половину из них на палки), \n"+"Если вам нужно "
    b11=" Дверей, то вам понадобится "
    b13=" люков, то вам понадобится "
    b15=" нажимных пластин, то вам понадобится "
    b17=" кнопок, то вам понадобится "
    b19=" Стен, то вам понадобится "
    b20="Блоков"


import setts
import compact as cp
import logsmode as lm
import mainmode as mm

MainMode, LogsMode, Compact = setts.ask()




#MainMode:
#   0 - n blocks
#   1 - n crafted
#LogsMode:
#   0 - planks
#   1 - //4 (logs)
#Compact (cp.Compact(ToConvert)):
#   0 - False
#   1 - True


userInput=int(input())
stairs, slabs, fences, sticks, gates, doors, traps, plates, buttons, walls = mm.MainMode(userInput)

stairs=lm.LogsMode(stairs)
slabs=lm.LogsMode(slabs)
fences=lm.LogsMode(fences)
sticks=lm.LogsMode(sticks)
gates=lm.LogsMode(gates)
doors=lm.LogsMode(doors)
traps=lm.LogsMode(traps)
plates=lm.LogsMode(plates)
buttons=lm.LogsMode(buttons)
walls=lm.LogsMode(walls)

if MainMode=="0":
    print(a1+str(cp.Compact(stairs))+a2+str(cp.Compact(slabs))+a3+str(cp.Compact(fences))+a4+str(cp.Compact(sticks))+a5+str(cp.Compact(gates))+a6+str(cp.Compact(doors))+a7+str(cp.Compact(traps))+a8+str(cp.Compact(plates))+a9+str(cp.Compact(buttons))+a10+str(cp.Compact(walls))+a11)
if MainMode=="1":
    print(b1+str(userInput)+b2+str(cp.Compact(stairs))+b3_5_8_12_14_16_18+str(userInput)+b4+str(cp.Compact(slabs))+b3_5_8_12_14_16_18+str(userInput)+b6+str(cp.Compact(fences))+b7+str(cp.Compact(sticks))+b8+str(userInput)+b9+str(cp.Compact(gates))+b10+str(userInput)+b11+str(cp.Compact(doors))+b3_5_8_12_14_16_18+str(userInput)+b13+str(cp.Compact(traps))+b3_5_8_12_14_16_18+str(userInput)+b15+str(cp.Compact(plates))+b3_5_8_12_14_16_18+str(userInput)+b17+str(cp.Compact(buttons))+b3_5_8_12_14_16_18+str(userInput)+b19+str(cp.Compact(walls))+b20)