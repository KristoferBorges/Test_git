import pyautogui
import pyperclip
# import time

pyautogui.PAUSE = 0.2

# pyautogui.write("Hello world")
# pyautogui.click(x=0, y=0, button="right", clicks=2)
# pyautogui.press()
# pyautogui.hotkey()
# time.sleep(5)

texto = "Bom dia! Meu nome é Kristofer e estou procurando minha primeira oportunidade profissional. " \
        "Sou apaixonado por programação e pratico diariamente. Gostaria de me conectar com você e solicitar, " \
        "se possível, uma análise do meu perfil para identificar áreas de melhoria."


pyautogui.click(x=1049, y=297)
pyautogui.click(x=1049, y=277)
pyautogui.click(x=773, y=329)
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1173, y=592)
