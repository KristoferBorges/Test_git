import pyautogui
import pyperclip
# import time

pyautogui.PAUSE = 0.2

# pyautogui.write("Hello world")
# pyautogui.click(x=0, y=0, button="right", clicks=2)
# pyautogui.press()
# pyautogui.hotkey()
# time.sleep(5)

texto = "Bom dia, me chamo Kristofer e estou em busca da minha primeira oportunidade. Trabalho com programação, " \
        "praticando diariamente. Gostaria de me conectar contigo e pedir, se possível, que analisasse meu perfil e " \
        "verificasse como posso melhorar. Estou disponível para entrevistas ou processos seletivos!"


pyautogui.click(x=1049, y=277)
pyautogui.click(x=773, y=329)
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1173, y=592)
