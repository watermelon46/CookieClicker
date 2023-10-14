# Hi! If you don't understand Russian - just use translator. Good luck!
# This is a BETA, It can contain many bugs
# Настройки по умолчанию
device="pc"
lang="EN"
print("\n" * 100)
from time import sleep
# Настройки игры.
allowcfg=True # Использовать систему конфигураций. Обязателен файл gamecfg.txt в директории игры.
olddesign=False # Использовать старый, кривой дизайн из CC! 1.6 и ранее. Новый дизайн содержит символы ╔║╙



# Загрузка конфигурации

if allowcfg==True:
    cfg=open("gamecfg.txt")
    lines = cfg.readlines()
    if lines[0]=="1":
        loadcfg = input("Load configuration? Don't type anything and press enter to load cfg, or type 'Never' and press enter to never see this question.")
        if loadcfg=="Never":
            cfg.truncate(0)
            cfg.write("0\n2\n2\n2")
    elif lines[0]=="0":
        print("Loading your configuration, please wait...")
        if lines[1]=="0":
            lang="EN"
        if lines[1]=="1":
            lang="RU"
        elif lines[1]=="2":
            lang=("Choose language [RU/EN], cfg file fon't contains it: ")
        elif lines[2]=="0":
            device="pc"
        elif lines[2]=="1":
            device="mobile"
        elif lines[2]=="2":
            device=input("Choose device [pc/mobile], cfg file don't contains it: ")
        if lang!="RU" and lang!="EN":
            lang=="EN"
            print("Language is incorrect")
        if device!="pc" and device!="mobile":
            device=="pc"
            print("Device is incorrect")
        # определение необработанных значений и запись их в файл
        if device=="pc":
            rawdevice=0
        elif device=="mobile":
            rawdevice=1
        if lang=="RU":
            rawlang=1
        if lang=="EN":
            rawlang=0
        cfg.truncate(0)
        cfg.write("1\n"+rawlang+"\n"+rawdevice)
    elif lines[0]==2:
        cfg.truncate(0)
        cfg.write("1\n2\n2\n2")

else:
    print("Configuration file didn't exist, loading anyway.")
# скрипт на выбор языка
lang=input("Choose language (EN or RU): ")
if lang!="RU" and lang!="EN":
    lang="EN"
device=input("What is your device (pc or mobile)? ")
if device!="mobile" and device!="pc":
    device="pc"
# установка начальных значений у переменных
cookies=-1
coins=0
boosters=0
clickers=0
avc=0
watermelons=0
shopinput=""
# приветственный текст
if device=="pc":
    print(" _____             _    _      _____ _ _      _             ")
    print("/  __ \           | |  (_)    /  __ \ (_)    | |            ")
    print("| /  \/ ___   ___ | | ___  ___| /  \/ |_  ___| | _____ _ __ ")
    print("| |    / _ \ / _ \| |/ / |/ _ \ |   | | |/ __| |/ / _ \ '__|")
    print("| \__/\ (_) | (_) |   <| |  __/ \__/\ | | (__|   <  __/ |   ")
    print(" \____/\___/ \___/|_|\_\_|\___|\____/_|_|\___|_|\_\___|_|   ")
elif device=="mobile":
    print("CookieClicker! v1.7 openbeta 1")
if lang=="RU":
    print("Сделано Холинимом\nКоманды:\nEnter (клавиша) - клик\nshop - открыть магазин\nexchange - обменять печенье на монеты")
    input("Нажми Enter два раза чтобы начать :D\n")
elif lang=="EN":
    print("Made by Holinim\nCommands:\nEnter - click\nshop - open shop\nexchange - exchange cookies for coins")
    input("Press Enter twice to start :D\n")
# код кликера
while True:
        userinput=input()
        if userinput=="":
            cookies+=1+boosters
            print("\n"*1000) # отдаление текста сверху
            if lang=="RU":
                if device == "pc":
                    print(
                        "                     ...~555555YYYYYYYY55YY5555~......\n                ....~YYYYYYYYYY????????YY??YYYYYJYYYY!....\n            ....75YYYYYYJ77??777777YY7777777?????JYYYYYY57..\n          ..?5YYYYYYJ7??7!!77~~^~~~77~~!!!!??5GJ77777JYYYY5?..\n        .:?555YYJ?7~!7?YJ77~~~~~~~~~~~~!7??Y5PB?~~!!77???JYY5J:.\n      ::J555YY?7?Y?!~~~~~~~7!~~^^^^^^~~^^YP55557~!7!~!7?YJ7?YY5J\n      J555YY?7?J7~!7!~~^^^~Y?^^^^^^^^^^^^Y555?7!~~~!7~^~77777?5J::\n    :^J5YY?7!~7J7~~~~^^~~^^~~^^:^^^~~^^^^^^~~?J7~~^7Y7:^~!J?7?YY5J\n    J555?77?!~!7!~~^^^^^^^^^^^^^^^^^^^^~~^^^^^^~~~~~~!!!~7JJ777?5Y^:\n  ^^Y5YYJJ7!!~7J!^^^^:::^^^~~^^^^^^^^^^^^::^^^^^^~~~~!7!~~!!777?YY5Y.\n .Y555?7?J!^~~~~~^^^^^^^^^^^^::^^~~7777^^::^^^^^^^^^^^^~~~!!~!?77?5Y\n  J555?7!!~~!7~^~!!!7?!^^^^::::^~??PGPPJ?^::^::^^^:^^!?????7~~777?5Y~~\n~~Y5JJ?777~~7J!~7JYPGBY:::::::^YY??JJY5GB~:^^::^^^^^^?GPPGB5!!~!7?JY55\n5555JJ7!~~~~^^?55PGB5J7^^:::::^YY55Y5PPYJ^:::::^^^^^~7YY5PGPYJ~~!!7?Y5\n55JJJJ!~~~~~^:7JJ?JJ!::^^::::::^^?JJJJ?^:::::::::^^^^~!7?JJJY?~~!7JJ55\n5Y?7777!~~^^^::::::::::^^::::::::::::::::::^^::::^^^:^^^^~~~!!~!7?JJ55\n5Y?777!!~^^^!?~::^:::::::::::::^^::::::::::^^::::^^!?!^^~~~~!!!77?JJ55\n55JJ?7??~^^^?Y!::::::::::::::::^^:::::::::::::::::^!?!^~~~~!??777?5555\n5555?7??7!~^~!^::::^^::::::::::::::::::::::::::7JJY!::^^~~^!5Y777?5555\n5555?7~~!!JYYYYY!::^:::^^^^::^^::::::^^::::::7Y5PPP5Y!:^~~~!J?7?JY5Y~~\n^~Y5?7777!YPPPGB?::::::^^::::::::::::^^::::?Y5P555Y5P5Y?~~~!7?YY555J\n  Y5YY?7!!?JYYPB?:!J!:::~YYYYYYYJ^:::::::::5BYJJJY55YPBY~!777?55555Y.\n .Y555?777??5GJ7~:~!~:::!PPPPPPGP^:::::::::5BJ?JYY5PGY77777?YY555Y^:\n  :^Y5YY?7??77!~^^^^^:::~JJJJ55GP^:^^^^::::~!YPPGPGJ!~:^!!7?555J^:\n    ::J5YY?7?J7~~~7J7^^^^~7PPPPGP^^^^^:^^^^^^!777?J!^~!?JJYY555J\n      ::J5YYJ??7!~!7!~~^^^~77!!!!77^^^^~~!7~~~~~~!77777J55555J::\n        .:?5YYYYJ777!~!7!~~~~~~~~!!~~~~JY!!~~!77777JYYYYYY5?:.\n          ..?5YYYYJ?77?YJ77~~~~~~77!~~~??77777?JYYYYYY57.::.\n            ....75YYYYY????YJ7777??YY?7??!!7?YYYYY5!....\n                ....~YYJYYY55YYYYYY55YYYYJJJYYY~...\n                     ...~5555555555555Y:.......                       ")  # ASCII арт печенья
                elif device == "mobile":
                    print("Клик! 🍪")
                if olddesign==False:
                    print("╔ Твои печеньки:", cookies, "\n║ Твои монеты:", coins, "\n║ Твои бустеры:", boosters, "\n║Твои кликеры:", clickers, "\n╙Твои арбузы:", watermelons)
            elif lang=="EN":
                if device == "pc":
                    print(
                        "                     ...~555555YYYYYYYY55YY5555~......\n                ....~YYYYYYYYYY????????YY??YYYYYJYYYY!....\n            ....75YYYYYYJ77??777777YY7777777?????JYYYYYY57..\n          ..?5YYYYYYJ7??7!!77~~^~~~77~~!!!!??5GJ77777JYYYY5?..\n        .:?555YYJ?7~!7?YJ77~~~~~~~~~~~~!7??Y5PB?~~!!77???JYY5J:.\n      ::J555YY?7?Y?!~~~~~~~7!~~^^^^^^~~^^YP55557~!7!~!7?YJ7?YY5J\n      J555YY?7?J7~!7!~~^^^~Y?^^^^^^^^^^^^Y555?7!~~~!7~^~77777?5J::\n    :^J5YY?7!~7J7~~~~^^~~^^~~^^:^^^~~^^^^^^~~?J7~~^7Y7:^~!J?7?YY5J\n    J555?77?!~!7!~~^^^^^^^^^^^^^^^^^^^^~~^^^^^^~~~~~~!!!~7JJ777?5Y^:\n  ^^Y5YYJJ7!!~7J!^^^^:::^^^~~^^^^^^^^^^^^::^^^^^^~~~~!7!~~!!777?YY5Y.\n .Y555?7?J!^~~~~~^^^^^^^^^^^^::^^~~7777^^::^^^^^^^^^^^^~~~!!~!?77?5Y\n  J555?7!!~~!7~^~!!!7?!^^^^::::^~??PGPPJ?^::^::^^^:^^!?????7~~777?5Y~~\n~~Y5JJ?777~~7J!~7JYPGBY:::::::^YY??JJY5GB~:^^::^^^^^^?GPPGB5!!~!7?JY55\n5555JJ7!~~~~^^?55PGB5J7^^:::::^YY55Y5PPYJ^:::::^^^^^~7YY5PGPYJ~~!!7?Y5\n55JJJJ!~~~~~^:7JJ?JJ!::^^::::::^^?JJJJ?^:::::::::^^^^~!7?JJJY?~~!7JJ55\n5Y?7777!~~^^^::::::::::^^::::::::::::::::::^^::::^^^:^^^^~~~!!~!7?JJ55\n5Y?777!!~^^^!?~::^:::::::::::::^^::::::::::^^::::^^!?!^^~~~~!!!77?JJ55\n55JJ?7??~^^^?Y!::::::::::::::::^^:::::::::::::::::^!?!^~~~~!??777?5555\n5555?7??7!~^~!^::::^^::::::::::::::::::::::::::7JJY!::^^~~^!5Y777?5555\n5555?7~~!!JYYYYY!::^:::^^^^::^^::::::^^::::::7Y5PPP5Y!:^~~~!J?7?JY5Y~~\n^~Y5?7777!YPPPGB?::::::^^::::::::::::^^::::?Y5P555Y5P5Y?~~~!7?YY555J\n  Y5YY?7!!?JYYPB?:!J!:::~YYYYYYYJ^:::::::::5BYJJJY55YPBY~!777?55555Y.\n .Y555?777??5GJ7~:~!~:::!PPPPPPGP^:::::::::5BJ?JYY5PGY77777?YY555Y^:\n  :^Y5YY?7??77!~^^^^^:::~JJJJ55GP^:^^^^::::~!YPPGPGJ!~:^!!7?555J^:\n    ::J5YY?7?J7~~~7J7^^^^~7PPPPGP^^^^^:^^^^^^!777?J!^~!?JJYY555J\n      ::J5YYJ??7!~!7!~~^^^~77!!!!77^^^^~~!7~~~~~~!77777J55555J::\n        .:?5YYYYJ777!~!7!~~~~~~~~!!~~~~JY!!~~!77777JYYYYYY5?:.\n          ..?5YYYYJ?77?YJ77~~~~~~77!~~~??77777?JYYYYYY57.::.\n            ....75YYYYY????YJ7777??YY?7??!!7?YYYYY5!....\n                ....~YYJYYY55YYYYYY55YYYYJJJYYY~...\n                     ...~5555555555555Y:.......                       ")  # ASCII арт печенья
                elif device == "mobile":
                    print("Click! 🍪")
                if olddesign==False:
                    print("╔ Your cookies:", cookies, "\n║ Your coins:", coins, "\n║ Your booster:", boosters, "\n║ Your clickers:",clickers, "\n╙ Your watermelons:", watermelons)
        elif userinput=="shop": # запуск скрипта магазина
            if lang=="RU":
                if olddesign==False:
                    print("╔ Твои печеньки -", cookies, "печенек\n║ Твои монеты -", coins, "монет\n║ Автокликер (5 минут) (1) - 10 монет\n║ Бустер печенек (2) - 50 монет\n╙ Арбуз (3) - 60 монет\nЧтобы купить, введите код продукта.") # список товаров
                    shopinput=input("Код продукта: ")
            elif lang=="EN":
                if olddesign == False:
                    print("╔ Your cookies -", cookies, "\n║ Your coins -", coins, "\n║ Autoclicker (5 minutes) (1) - 10 coins\n║ Cookie Booster (2) - 50 coins\n╙ Watermelon (3) - 60 coins")  # список товаров
                shopinput=input("Product code: ")
            if shopinput=="1":
                if coins<10: # проверка на количество монет
                    if lang == "RU":
                        print("Не хвататает монет!")
                    elif lang == "EN":
                        print("Not enough coins!")
                else: # подтверждение покупки
                    clickers+=1
                    coins-=10
                    if lang == "RU":
                        print("Успешно! Чтобы активировать кликер, пропишите clicker")
                    elif lang == "EN":
                        print("Success! To activate clicker, input clicker")
            elif shopinput=="2":
                if coins<20:
                    if lang == "RU":
                        print("Не хвататает монет!")
                    elif lang == "EN":
                        print("Not enough coins!")
                boosters+=1
                coins-=10
                if lang == "RU":
                    print("Успешно!")
                elif lang == "EN":
                    print("Success!")
            elif shopinput=="3":
                if coins<60:
                    if lang == "RU":
                        print("Не хвататает монет!")
                    elif lang == "EN":
                        print("Not enough coins!")
                watermelons+=1
                coins-=60
                if lang == "RU":
                    print("Успешно!")
                elif lang == "EN":
                       print("Success!")
        elif userinput=="clicker": # скрипт кликера
            if clickers>0: # проверка на наличие кликеров
                clickers-=1 # снятие одного кликера из инвентаря
                if lang == "RU:":
                    print("Кликер включен на 5 минут. Пока он включен, вы не можете кликать самостоятельно.")
                elif lang == "EN":
                    print("The clicker is on for 5 minutes. While it's on, you can't click on your own.")
                for i in range(2392): # скрипт кликера (8 кликов в секунду)
                    sleep(0.125) #задержка
                    cookies+=1
                    if lang == "RU:":
                        print("Клик! Ваши печеньки:", cookies)
                    elif lang == "EN":
                        print("Click! Your cookies:", cookies)
                if lang == "RU":
                    print("Кликер отключен!")
                elif lang == "EN":
                    print("Clicker disabled!")
            else:
                if lang == "RU":
                    print("У вас нет кликеров!")
                elif lang == "EN":
                    print("You don't have clickers!")
        elif userinput=="exchange": # скрипт обмена печенья на монеты (курс: 1 печенька = 0.01 монета)
            if lang == "RU":
                print("Печеньки были переведены в", cookies/100, "монет (без учета монет полученных благодаря арбузам.)")
            elif lang == "EN":
                print("Cookies were converted into", cookies/100, "coins (excluding coins received thanks to watermelons.)")
            coins+=cookies/100
            coins+=watermelons/100
            cookies=0
        elif userinput == "save":  # скрипт сохранения прогресса
            if lang == "RU":
                input("СОЗДАЙТЕ ФАЙЛ С НАЗВАНИЕМ ccsave.txt, ИНАЧЕ ИГРА КРАШНЕТСЯ. ПОСЛЕ СОЗДАНИЯ ФАЙЛА НАЖМИТЕ ENTER.")
            elif lang == "EN":
                input(
                    "CREATE A FILE WITH THE NAME ccsave.txt, OTHERWISE THE GAME WILL CRASH. AFTER CREATING THE FILE, PRESS ENTER.")
            savefile = open("ccsave.txt", "w")
            savefile.write(str(cookies) + "\n" + str(round(coins)) + "\n" + str(boosters) + "\n" + str(clickers) + "\n" + str(
                watermelons))
            if lang == "RU:":
                print("Файл сохранения создан с названием ccsave.txt")
            elif lang == "EN":
                print("The save file was saved with the name ccsave.txt.")
            savefile.close()
        elif userinput == "load":
            if lang == "RU":
                input("УБЕДИТЕСЬ В НАЛИЧИИ ФАЙЛА С СОХРАНЕНИЕМ (ccsave.txt)! В ИНОМ СЛУЧАЕ ИГРА МОЖЕТ КРАШНУТЬСЯ! НАЖМИТЕ ENTER, ЕСЛИ ФАЙЛ С СОХРАНЕНИЕМ ИМЕЕТСЯ!")
            elif lang == "EN":
                input("MAKE SURE THERE IS A SAVE FILE (ccsave.txt )! OTHERWISE, THE GAME MAY CRASH! PRESS ENTER IF THERE IS A SAVE FILE!")
            loadfile = open("ccsave.txt", "r")
            lines = loadfile.readlines()
            cookies = int(lines[0].replace("\n", ""))
            coins = int(lines[1].replace("\n", ""))
            boosters = int(lines[2].replace("\n", ""))
            clickers = int(lines[3].replace("\n", ""))
            watermelons = int(lines[4].replace("\n", ""))