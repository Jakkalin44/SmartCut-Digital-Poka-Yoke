
import pyautogui
import time

job_code = "Abcdf2221"

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

print("SmartCut Automation Test")

windows = [
    w for w in pyautogui.getWindowsWithTitle(
        "Untitled - Notepad"
    )
    if w.title == "Untitled - Notepad"
]

if len(windows) != 1:
    print("Cancelled: Notepad window not found or ambiguous")

else:
    notepad = windows[0]

    try:
        if notepad.isMinimized:
            notepad.restore()

        notepad.activate()
        time.sleep(2)

        active = pyautogui.getActiveWindow()

        if active and active._hWnd == notepad._hWnd:

            print("Correct window detected")
            print("Sending:", job_code)

            pyautogui.write(
                job_code,
                interval=0.3
            )

            print("Typing command completed")
            print("Verify text in Notepad manually")

        else:
            print("Cancelled: Wrong active window")

    except pyautogui.FailSafeException:
        print("Emergency stop!")

    except Exception as e:
        print("Automation error:", e)
