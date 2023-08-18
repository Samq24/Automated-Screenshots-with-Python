import os
import pyautogui
import time
import keyboard

desktop_path = os.path.expanduser(r"C:\folder_of_your_choice")

def screenshot(destination_folder):
    name = int(round(time.time() * 1000))
    name = os.path.join(destination_folder, '{}.jpg'.format(name))
    
    print(f"Captura en: {name}")
    img = pyautogui.screenshot()
    img.save(name, "JPEG")
    img.show()

print("Presiona Ctrl + 'q' para tomar una captura de pantalla. Presiona Esc para salir.")

while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
        screenshot(desktop_path)
        time.sleep(1) 

    if keyboard.is_pressed('esc'):
        print("Saliendo...")
        break
