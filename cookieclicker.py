import pyautogui
import time
import keyboard
import random

pixels_to_look = [
	((1830, 300), (148, 144, 133)),
	((1830, 350), (147, 144, 129)),
	((1830, 400), (144, 142, 129)),
	((1830, 450), (171, 171, 155)),
	((1830, 500), (148, 145, 130)),
	((1830, 550), (154, 150, 139)),
	((1830, 600), (142, 140, 127)),
	((1830, 650), (174, 171, 152)),
	((1830, 700), (138, 137, 120)),
	((1830, 760), (146, 143, 128)),
	((1670, 180), (146, 96, 45))
	# ((1830, 400), (144, 142, 129)),
	# ((1830, 400), (144, 142, 129)),
]
time.sleep(1)

running = True
prev = time.time()
clicking = True
def keyboard_event(scan_code):
	global running
	running = False
	keyboard.clear_all_hotkeys();

def reset_timer(scan_code):
	global prev
	prev = time.time()

def pause_clicking(scan_code):
	global clicking
	clicking = False

def resume_clicking(scan_code):
	global clicking
	clicking = True

def main():
	global prev
	pyautogui.FAILSAFE = False
	keyboard.hook_key("esc", keyboard_event, True)
	keyboard.hook_key("ctrl", reset_timer, False)
	keyboard.on_press_key("alt", pause_clicking, True)
	keyboard.on_release_key("alt", resume_clicking, True)
	wait_time = random.uniform(10, 60*20)
	while running:
		if time.time() - prev >= wait_time:
			prev = time.time()
			wait_time = random.uniform(10, 60*20)
			cont = True
			while cont:
				img = pyautogui.screenshot()
				cont = False
				for item in reversed(pixels_to_look):
					if img.getpixel(item[0]) == item[1]:
						proceed_click(item[0])
						cont = True
						break
		proceed_click((330, 500), clicks=5)

def proceed_click(xy, **kwargs):
	if clicking:
		pyautogui.click(xy[0], xy[1], **kwargs)
		pyautogui.click(330, 500, clicks=1)

if __name__ == "__main__":
	main()