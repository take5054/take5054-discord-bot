def aa(text, path):
    if text == '1':
        temp = '░░░░░██████╗░░██████╗░░░░░░░░░██╔════╝░██╔════╝░░░░░░░░░██║░░██╗░██║░░██╗░░░░░░░░░██║░░╚██╗██║░░╚██╗░░░░░░░░╚██████╔╝╚██████╔╝░░░░░░░░░╚═════╝░░╚═════╝░░░░░'
    elif text == '2':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀▀▀░█▀▀▀░█▐▌█░█▀█░█░█░░░░█░▀█░█░▀█░█▐▌█░█▀▀░▀░▀░░░░▀▀▀▀░▀▀▀▀░▝▀▀▘░▀░░░▀░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    elif text == '3':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▄░▄█░█░█▀▀░░░░░░░░░░░░░░░█░▀░█░█░█░░░░░░░░░░░░░░░░░▀░░░▀░▀░▀▀▀░░░░░░░░░█▄░▄█░█░░█░▀█▀░█▀▀░█▀▄░░░░█░▀░█░█░░█░░█░░█▀▀░█░█░░░░▀░░░▀░▀▀▀▀░░▀░░▀▀▀░▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    elif text == '4':
        temp = '━━━┏━┓━┏┓┏━━┓┏━━━┓┏━━━┓━━━━━━┃┃┗┓┃┃┗┫┣┛┃┏━┓┃┃┏━━┛━━━━━━┃┏┓┗┛┃━┃┃━┃┃━┗┛┃┗━━┓━━━━━━┃┃┗┓┃┃━┃┃━┃┃━┏┓┃┏━━┛━━━━━━┃┃━┃┃┃┏┫┣┓┃┗━┛┃┃┗━━┓━━━━━━┗┛━┗━┛┗━━┛┗━━━┛┗━━━┛━━━'
    elif text == '5':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▄░█░▀█▀░░░░░░░░░░░░░░░░░░█░▀█░░█░░░░░░░░░░░░░░░░░░░▀░░▀░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    elif text == '6':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀▀▀░█▀▀▀░░█▀▀░▀▀█░░█░░░░░█░▀█░█░▀█░░█▀▀░▄▀░░░▀░░░░░▀▀▀▀░▀▀▀▀░░▀▀▀░▀▀▀░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    elif text == '7':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀█░█▀█░█▀█░█▀█░▀█▀░░░░░░░█░█░█▀▀░█▀▀░█▄█░░█░░░░░░░░▀▀▀░▀░░░▀░░░▀░▀░▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    elif text == '8':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░UNINSTALLING░VALORANT░░░░░░░░░░░░░▇▇▇▇▇▇▇▇▇▇▇▇▇▇▢░░░░░░░░░░░░░╭━╮╭━╮╭╮░╱░░░░░░░░░░░░░░░░╰━┫╰━┫╰╯╱╭╮░░░░░░░░░░░░░░░╰━╯╰━╯░╱░╰╯░░░░░░░░░░░░░░░░░COMPLETE░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    elif text == '9':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    elif text == '10':
        temp = '░░█████╗░███████╗██╗░░██╗░░██╔══██╗██╔════╝██║░██╔╝░░███████║█████╗░░█████═╝░░░██╔══██║██╔══╝░░██╔═██╗░░░██║░░██║██║░░░░░██║░╚██╗░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░'
    elif text == '11':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█▀█░█░█░░░░░░░░░░░░░░░░█░░█░█░█░█░░░░░░░░░░░░░░░░▀░░▀▀▀░▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▄░█░█▀█░█▀█░█▀▄░░░░░░░░░░█░▀█░█░█░█░█░█▀█░░░░░░░░░░▀░░▀░▀▀▀░▀▀▀░▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    elif text == '12':
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀▀░█░█░█▀▀░█░▄░░░░░░░░░░░█▀▀░█░█░█░░░█▀▄░░░░░░░░░░░▀░░░▀▀▀░▀▀▀░▀░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█▀█░█░█░█░█░░░░░░░░░░░░█░░█░█░█░█░▀░▀░░░░░░░░░░░░▀░░▀▀▀░▀▀▀░▀░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    else:
        temp = '░░░░░░░░░░░░░░░░░░░░░░░░░░'
        q = 0
        num = len(text)
        for i in range(3):
            temp += '░'
            for j in range(num):
                if text[j] == 'A':
                    if i == 0:
                        temp += '█▀█'
                    elif i == 1:
                        temp += '█▄█'
                    else:
                        temp += '▀░▀'
                elif text[j] == 'B':
                    if i == 0:
                        temp += '█▀▄'
                    elif i == 1:
                        temp += '█▀█'
                    else:
                        temp += '▀▀░'
                elif text[j] == 'C':
                    if i == 0:
                        temp += '█▀▀'
                    elif i == 1:
                        temp += '█░░'
                    else:
                        temp += '▀▀▀'
                elif text[j] == 'D':
                    if i == 0:
                        temp += '█▀▄'
                    elif i == 1:
                        temp += '█░█'
                    else:
                        temp += '▀▀░'
                elif text[j] == 'E':
                    if i == 0:
                        temp += '█▀▀'
                    elif i == 1:
                        temp += '█▀▀'
                    else:
                        temp += '▀▀▀'
                elif text[j] == 'F':
                    if i == 0:
                        temp += '█▀▀'
                    elif i == 1:
                        temp += '█▀▀'
                    else:
                        temp += '▀░░'
                elif text[j] == 'G':
                    if i == 0:
                        temp += '█▀▀▀'
                    elif i == 1:
                        temp += '█░▀█'
                    else:
                        temp += '▀▀▀▀'
                elif text[j] == 'H':
                    if i == 0:
                        temp += '█░█'
                    elif i == 1:
                        temp += '█▀█'
                    else:
                        temp += '▀░▀'
                elif text[j] == 'I':
                    if i == 0:
                        temp += '▀█▀'
                    elif i == 1:
                        temp += '░█░'
                    else:
                        temp += '▀▀▀'
                elif text[j] == 'J':
                    if i == 0:
                        temp += '▀█▀'
                    elif i == 1:
                        temp += '░█░'
                    else:
                        temp += '▀▀░'
                elif text[j] == 'K':
                    if i == 0:
                        temp += '█░▄'
                    elif i == 1:
                        temp += '█▀▄'
                    else:
                        temp += '▀░▀'
                elif text[j] == 'L':
                    if i == 0:
                        temp += '█░░'
                    elif i == 1:
                        temp += '█░░'
                    else:
                        temp += '▀▀▀'
                elif text[j] == 'M':
                    if i == 0:
                        temp += '█▄░▄█'
                    elif i == 1:
                        temp += '█░▀░█'
                    else:
                        temp += '▀░░░▀'
                elif text[j] == 'N':
                    if i == 0:
                        temp += '█▄░█'
                    elif i == 1:
                        temp += '█░▀█'
                    else:
                        temp += '▀░░▀'
                elif text[j] == 'O':
                    if i == 0:
                        temp += '█▀█'
                    elif i == 1:
                        temp += '█░█'
                    else:
                        temp += '▀▀▀'
                elif text[j] == 'P':
                    if i == 0:
                        temp += '█▀█'
                    elif i == 1:
                        temp += '█▀▀'
                    else:
                        temp += '▀░░'
                elif text[j] == 'Q':
                    if i == 0:
                        temp += '█▀█░'
                    elif i == 1:
                        temp += '█░█░'
                    else:
                        temp += '▀▀▀▀'
                elif text[j] == 'R':
                    if i == 0:
                        temp += '█▀▄'
                    elif i == 1:
                        temp += '█▀▄'
                    else:
                        temp += '▀░▀'
                elif text[j] == 'S':
                    if i == 0:
                        temp += '█▀▀'
                    elif i == 1:
                        temp += '▀▀█'
                    else:
                        temp += '▀▀▀'
                elif text[j] == 'T':
                    if i == 0:
                        temp += '▀█▀'
                    elif i == 1:
                        temp += '░█░'
                    else:
                        temp += '░▀░'
                elif text[j] == 'U':
                    if i == 0:
                        temp += '█░█'
                    elif i == 1:
                        temp += '█░█'
                    else:
                        temp += '▀▀▀'
                elif text[j] == 'V':
                    if i == 0:
                        temp += '█░█'
                    elif i == 1:
                        temp += '█░█'
                    else:
                        temp += '░▀░'
                elif text[j] == 'W':
                    if i == 0:
                        temp += '█▐▌█'
                    elif i == 1:
                        temp += '█▐▌█'
                    else:
                        temp += '░▀▀░'
                elif text[j] == 'X':
                    if i == 0:
                        temp += '█░█'
                    elif i == 1:
                        temp += '░█░'
                    else:
                        temp += '█░█'
                elif text[j] == 'Y':
                    if i == 0:
                        temp += '█░█'
                    elif i == 1:
                        temp += '░█░'
                    else:
                        temp += '░█░'
                elif text[j] == 'Z':
                    if i == 0:
                        temp += '▀▀█'
                    elif i == 1:
                        temp += '▄▀░'
                    else:
                        temp += '▀▀▀'
                else:
                    temp += '░░░'
                temp += '░'
            k = len(temp)
            if k > (i + 2) * 26:
                q = 1
                temp = 'ERROR：文章が長すぎます！'
                break
            if k <= (i + 2) * 26:
                while (True):
                    temp += '░'
                    k += 1
                    if k == (i + 2) * 26:
                        break
        if q != 1:
            temp += '░░░░░░░░░░░░░░░░░░░░░░░░░░'
    return temp