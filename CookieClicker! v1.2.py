# импорт библиотек
import time
# установка начальных значений у переменных
cookies=0
coins=0
booster=0
clickers=0
# приветственный текст
print("_________                __   .__         _________ .__  .__        __                 \n\_   ___ \  ____   ____ |  | _|__| ____   \_   ___ \|  | |__| ____ |  | __ ___________ \n/    \  \/ /  _ \ /  _ \|  |/ /  |/ __ \  /    \  \/|  | |  |/ ___\|  |/ // __ \_  __ \ \n\     \___(  <_> |  <_> )    <|  \  ___/  \     \___|  |_|  \  \___|    <\  ___/|  | \/\n \______  /\____/ \____/|__|_ \__|\___  >  \______  /____/__|\___  >__|_ \\___  >__|   \n        \/                   \/       \/          \/             \/     \/    \/           v1.1")# ASCII арт нвазния игры
print("Made by Holinim\nCommands:\nEnter - click\nshop - opens a store.\nexchange - exchange cookies to coins\npromocode - use promocode")
input("Press Enter 2 times to start :D\n")
# код кликера
while True:
        userinput=input()
        if userinput=="":
            time.sleep(0.1)
            cookies+=1+booster
            print("\n"*1000) # отдаление текста сверху
            print("                     ...~555555YYYYYYYY55YY5555~......\n                ....~YYYYYYYYYY????????YY??YYYYYJYYYY!....\n            ....75YYYYYYJ77??777777YY7777777?????JYYYYYY57..\n          ..?5YYYYYYJ7??7!!77~~^~~~77~~!!!!??5GJ77777JYYYY5?..\n        .:?555YYJ?7~!7?YJ77~~~~~~~~~~~~!7??Y5PB?~~!!77???JYY5J:.\n      ::J555YY?7?Y?!~~~~~~~7!~~^^^^^^~~^^YP55557~!7!~!7?YJ7?YY5J\n      J555YY?7?J7~!7!~~^^^~Y?^^^^^^^^^^^^Y555?7!~~~!7~^~77777?5J::\n    :^J5YY?7!~7J7~~~~^^~~^^~~^^:^^^~~^^^^^^~~?J7~~^7Y7:^~!J?7?YY5J\n    J555?77?!~!7!~~^^^^^^^^^^^^^^^^^^^^~~^^^^^^~~~~~~!!!~7JJ777?5Y^:\n  ^^Y5YYJJ7!!~7J!^^^^:::^^^~~^^^^^^^^^^^^::^^^^^^~~~~!7!~~!!777?YY5Y.\n .Y555?7?J!^~~~~~^^^^^^^^^^^^::^^~~7777^^::^^^^^^^^^^^^~~~!!~!?77?5Y\n  J555?7!!~~!7~^~!!!7?!^^^^::::^~??PGPPJ?^::^::^^^:^^!?????7~~777?5Y~~\n~~Y5JJ?777~~7J!~7JYPGBY:::::::^YY??JJY5GB~:^^::^^^^^^?GPPGB5!!~!7?JY55\n5555JJ7!~~~~^^?55PGB5J7^^:::::^YY55Y5PPYJ^:::::^^^^^~7YY5PGPYJ~~!!7?Y5\n55JJJJ!~~~~~^:7JJ?JJ!::^^::::::^^?JJJJ?^:::::::::^^^^~!7?JJJY?~~!7JJ55\n5Y?7777!~~^^^::::::::::^^::::::::::::::::::^^::::^^^:^^^^~~~!!~!7?JJ55\n5Y?777!!~^^^!?~::^:::::::::::::^^::::::::::^^::::^^!?!^^~~~~!!!77?JJ55\n55JJ?7??~^^^?Y!::::::::::::::::^^:::::::::::::::::^!?!^~~~~!??777?5555\n5555?7??7!~^~!^::::^^::::::::::::::::::::::::::7JJY!::^^~~^!5Y777?5555\n5555?7~~!!JYYYYY!::^:::^^^^::^^::::::^^::::::7Y5PPP5Y!:^~~~!J?7?JY5Y~~\n^~Y5?7777!YPPPGB?::::::^^::::::::::::^^::::?Y5P555Y5P5Y?~~~!7?YY555J\n  Y5YY?7!!?JYYPB?:!J!:::~YYYYYYYJ^:::::::::5BYJJJY55YPBY~!777?55555Y.\n .Y555?777??5GJ7~:~!~:::!PPPPPPGP^:::::::::5BJ?JYY5PGY77777?YY555Y^:\n  :^Y5YY?7??77!~^^^^^:::~JJJJ55GP^:^^^^::::~!YPPGPGJ!~:^!!7?555J^:\n    ::J5YY?7?J7~~~7J7^^^^~7PPPPGP^^^^^:^^^^^^!777?J!^~!?JJYY555J\n      ::J5YYJ??7!~!7!~~^^^~77!!!!77^^^^~~!7~~~~~~!77777J55555J::\n        .:?5YYYYJ777!~!7!~~~~~~~~!!~~~~JY!!~~!77777JYYYYYY5?:.\n          ..?5YYYYJ?77?YJ77~~~~~~77!~~~??77777?JYYYYYY57.::.\n            ....75YYYYY????YJ7777??YY?7??!!7?YYYYY5!....\n                ....~YYJYYY55YYYYYY55YYYYJJJYYY~...\n                     ...~5555555555555Y:.......                       ") # ASCII арт печенья
            print("Your cookies:", cookies, "\nYour coins:", coins, "\nYour booster:", booster, "\nYour clickers:", clickers)
        elif userinput=="shop": # запуск скрипта магазина
            print("Your cookies -", cookies, "cookies\nYour coins -", coins, "coins\nAutoClicker(1) - 10 coins\nCookie Booster(2) - 50 coins\nTo buy, input product code.") # список товаров
            shopinput=input("Product code: ") # ввод кода продукта
            if shopinput=="1":
                if coins<10: # проверка на количество монет
                    print("Not enough coins")
                else: # подтверждение покупки
                    clickers+=1
                    coins-=10
                    print("Successful! To start clicker input clicker")
            elif shopinput=="2":
                if coins<20:
                    print("Not enough coins!")
                else:
                    booster+=1
                    coins-=10
                    print("Successful!")
        elif userinput=="clicker": # скрипт кликера
            if clickers>0: # проверка на наличие кликеров
                clickers-=1 # снятие одного кликера из инвентаря
                print("Clicker for 5 minutes! For this time you can't disable clicker")
                for i in range(2392): # скрипт кликера (8 кликов в секунду)
                    time.sleep(0.125) #задержка
                    cookies+=1
                    print("Click! Cookies:", cookies) # уведомление у клике
                print("Clicker disabled!") # уведомление о отлючении кликера
            else:
                print("You don't have clickers!")
        elif userinput=="exchange": # скрипт обмена печенья на монеты (курс: 1 печенька = 0.01 монета)
            print("Cookies exchanged to", cookies/100, "coins.") # уведомление о обмене
            coins+=cookies / 100
            cookies=0
