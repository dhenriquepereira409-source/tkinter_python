import pyautogui
from time import sleep
#REALIZAR LOGIN
pyautogui.click(1188,181, duration=2)
pyautogui.press('enter')
sleep(3)
pyautogui.click(961,618, duration=2)
pyautogui.write('douglas123')
pyautogui.press('enter')
sleep(2)
pyautogui.press('enter')
#CLICAR NOVOS PRODUTOS
pyautogui.click(47,46, duration=1)
#ADIONAR PRODUTOS
with open('itens_aleatorios.txt', 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(',')[0]
        nome = linha.split(',')[1]
        qntd = linha.split(',')[2]
        preco = linha.split(',')[3]

        pyautogui.click(231,85, duration=1) #ID
        pyautogui.write(id_prod)
        pyautogui.click(234,147, duration=1) #NOME
        pyautogui.write(nome)
        pyautogui.click(229,214, duration=1) #QUANTIDADE
        pyautogui.write(qntd)
        pyautogui.click(232,281, duration=1) #PREÇO
        pyautogui.write(preco)
        pyautogui.click(235,328) #SALVAR
        sleep(2)
        pyautogui.press('enter')