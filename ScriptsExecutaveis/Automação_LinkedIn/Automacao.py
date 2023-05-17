import pyautogui
# import time

pyautogui.PAUSE = 1

# pyautogui.write("Hello world")
# pyautogui.click(x=0, y=0, button="right", clicks=2)
# pyautogui.press()
# pyautogui.hotkey()
# time.sleep(5)

texto = "Bom dia, me chamo Kristofer e estou em busca da minha primeira oportunidade. Trabalho com programação, " \
        "praticando diariamente. Gostaria de me conectar contigo e pedir, se possível, que analisasse meu perfil e " \
        "verificasse como posso melhorar. Estou disponível para entrevistas ou processos seletivos!"

pyautogui.hotkey("alt", "tab")
pyautogui.click(x=1050, y=306)
pyautogui.click(x=785, y=328)
pyautogui.write(texto)
pyautogui.click(x=1174, y=600)
