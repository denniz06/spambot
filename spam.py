import time
import pyautogui

time.sleep(5)

# words.txt sizin bir kelime listeniz olmalı

# words.txt is must your word list

a = open("words.txt", 'r')

for word in a:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

#  Çalıştırmak için whatsapp, discord, instagram vs. gibi sitelerde mesajlaşma çubuğuna
# tıklayıp başka hiçbir yere tıklamadan enter tuşuna basarsanız kelimeler bitene kadar spam atacaktır.

#  To run whatsapp, discord, instagram etc. to the messaging bar on sites such as
# if you click and press enter without clicking anywhere else, it will spam until the words are 
# finished.

