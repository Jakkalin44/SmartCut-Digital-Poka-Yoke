import pyautogui
import pyperclip
import time

job_code = "Abcdf2221"

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

print("SmartCut Clipboard Automation")

# Find Notepad window
windows = [
    w for w in pyautogui.getWindowsWithTitle(
        "Untitled - Notepad"
    )
    if w.title == "Untitled - Notepad"
]

if len(windows) != 1:
    print("Cancelled: Notepad not found or ambiguous")

else:
    notepad = windows[0]

    try:
        # Copy Job Code
        pyperclip.copy(job_code)

        # Verify Clipboard
        if pyperclip.paste() != job_code:
            print("Cancelled: Clipboard verification failed")

        else:
            print("Clipboard verified!")

            if notepad.isMinimized:
                notepad.restore()

            # Activate Notepad
            notepad.activate()
            time.sleep(2)

            active = pyautogui.getActiveWindow()

            if active and active._hWnd == notepad._hWnd:
                print("Correct window detected")

                # Paste using Ctrl + V
                pyautogui.hotkey("ctrl", "v")

                print("Paste command completed")
                print("Verify the result in Notepad")

            else:
                print("Cancelled: Wrong active window")

    except pyautogui.FailSafeException:
        print("Emergency stop activated!")

    except Exception as e:
        print("Automation error:", e)
