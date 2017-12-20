import pyautogui
import time

position = [(755, 270),(755, 420),(755, 570),(755, 720),(755, 870)] # Youtube Video positions. Different for different resolutions

pyautogui.moveTo(345, 141, duration=3)  # position of search box
pyautogui.click()
pyautogui.typewrite('Hello world!\n') # string to search
time.sleep(3)

for item in position:    # for each video positon 
	time.sleep(3)
	pyautogui.moveTo(item, duration=3)
	pyautogui.click()
	time.sleep(3)
	pyautogui.moveTo(442, 1035, duration=3)   # comment box position
	pyautogui.click()
	pyautogui.typewrite('Hello world!')       # the comment
	time.sleep(3)
	pyautogui.moveTo(1160, 1068, duration=3)  # comment button
	pyautogui.click()
	time.sleep(3)
	pyautogui.moveTo(81, 74, duration=3)      # back button
	pyautogui.click()
	time.sleep(3)