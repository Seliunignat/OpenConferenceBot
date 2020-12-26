##
import pyautogui
import os

from time import sleep


html = "https://vk.com/doc194236506_571722849?hash=a55cdb88aa3c5b6697&dl=7e4828624d9931519f"
edurfe = "https://edurfe.bsu.by/"
edurfe_Physics = "https://edurfe.bsu.by/mod/bigbluebuttonbn/view.php?id=5422"
edurfe_Physics_join = "https://edurfe.bsu.by/mod/bigbluebuttonbn/bbb_view.php?action=join&id=5422&bn=924"
edurfe_Chislaki = "https://edurfe.bsu.by/mod/bigbluebuttonbn/view.php?id=5409"
edurfe_Chislaki_join = "https://edurfe.bsu.by/mod/bigbluebuttonbn/bbb_view.php?action=join&id=5409&bn=923"
edurfe_TheorVer = "https://edurfe.bsu.by/mod/bigbluebuttonbn/view.php?id=5437"
edurfe_TheorVer_join = "https://edurfe.bsu.by/mod/bigbluebuttonbn/bbb_view.php?action=join&id=5437&bn=925"
edurfe_Programming = "https://edurfe.bsu.by/mod/bigbluebuttonbn/view.php?id=713"
edurfe_Programming_join = "https://edurfe.bsu.by/mod/bigbluebuttonbn/bbb_view.php?action=join&id=713&bn=49"
chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

sleepTime = 4

Subject_index = 2  # <<<<<------- Выбор пердмета <<<<---------
"""
1 - Физика
2 - Числаки
3 - ТеорВер
4 - Прога
5 - 
6 - 
"""
Subject = [edurfe_Physics, edurfe_Physics_join, edurfe_Chislaki, edurfe_Chislaki_join, edurfe_TheorVer, edurfe_TheorVer_join, edurfe_Programming, edurfe_Programming_join]
##
# пауза и досрочное прекращение
pyautogui.PAUSE = 2.0
pyautogui.FAILSAFE = True
##
# разрешение и позиция
print(pyautogui.size())
print(pyautogui.position())
##
# перемещение мыши
os.startfile(chrome)  #Открываем хром

#pyautogui.moveTo(1745, 1055, duration=0.5)
#pyautogui.click()
#pyautogui.moveTo(1745, 900, duration=0.5)
#pyautogui.click()
sleep(sleepTime)

pyautogui.moveTo(219, 65, duration=0.5)
pyautogui.click()
pyautogui.typewrite(Subject[Subject_index*2 - 2]) #вводим ссылку на раздел лекции по физике
pyautogui.press("enter")
sleep(sleepTime) #ждем

pyautogui.moveTo(1320, 670, duration=0.5) #нажимаем Log in
pyautogui.click()
sleep(sleepTime) #ждем

pyautogui.moveTo(219, 65, duration=0.5)
pyautogui.click()
pyautogui.typewrite(Subject[Subject_index*2-1])
pyautogui.press("enter")
sleep(sleepTime) #ждем

pyautogui.moveTo(1920/2 + 80, 1080/2 + 20, duration=0.5)
pyautogui.click()
