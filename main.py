from colorama import Fore, init
import pyautogui as pg
import subprocess
import time
import sys
import os

quiet = False # Modo silencioso
valid = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

def jilog(text):
    if not quiet == True:
        print(f"{Fore.BLUE}[{Fore.LIGHTBLUE_EX}+{Fore.BLUE}] {Fore.RESET}{text}")
    
def cls():
    os.system("cls" if os.name == "nt" else "clear")

def setup():
    cls()
    jilog(f"Yos coded this with love <3")
    time.sleep(2)
    main()

def ejecutar(lineas=None):
    loopline = None

    for line in range(len(lineas)):
        key = lineas[line].strip()
        jilog(f"[KEY]> ({len(key)} / {len(key.split('+'))}) {key}") # Imprime la key

        if key[0] == "'": # Raw
            key = key[1::]
            pg.write(key,0.01)
            continue
        
        elif key[0] == "\\": # Especial
            cmd = key[1::]
            if cmd == "pause":
                input("Program paused. Press enter to continue...")
                continue
            elif cmd == "loop":
                loopline = line
            elif len(cmd.split(" ")) > 1: # Especial dobles
                cmd = cmd.split(" ")
                if cmd[0] == "sleep": # Sleep
                    time.sleep(float(cmd[1]))
                    continue
                elif cmd[0] == "mv": # Mover cursor
                    pg.moveTo(int(cmd[1]), int(cmd[2]))       
                    continue
        
        elif len(key.split("+")) > 1: # Combinaciones
            cmds = key.split("+")
            for k in cmds:
                pg.keyDown(k)
            for k in cmds:
                pg.keyUp(k)
            continue

        # Clicks
        elif key == "click" or key == "\\lclick":
            pg.click(button='left')
            continue

        elif key == "\\rclick":
            pg.click(button='right')
            continue
        
        elif key.lower() in valid: # Single
            pg.press(key.lower()) 
            continue

        else: # Keystroke
            pg.write(key,0.01)
            continue

    if loopline != None:
        ejecutar(lineas=lineas[loopline::])

def main(keysfilename="keys.txt"):
    cls()
    jilog("=================================\n          MyRubber - Yos\n=================================\n")
    jilog(f"Trying to read {keysfilename}")
    
    while not os.path.exists(keysfilename):
        jilog(f"{keysfilename} not found. Enter keystroke filename...")
        keysfilename = input(f"{Fore.CYAN}[FILENAME]> {Fore.RESET}")
    cls()
    
    with open(keysfilename, 'r') as f:
        lineas = f.readlines() 

    ejecutar(lineas=lineas)

if __name__ == "__main__":
    init()
    args = sys.argv # Aquí iría el argparse
    if len(args)-1 > 0: # Aquí si hay un nombre de archivo
        kfn = args[1] # Keys filename
        if len(args)-1 > 1:
            if args[2] == "q":
                quiet = True
        main(keysfilename=kfn)
    else:
        setup()