
import pyautogui
import pyperclip
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3


def send_to_notepad(job_code):

    # 1. Validate input
    if not isinstance(job_code, str) or not job_code.strip():
        return False, "Invalid Job Code"

    job_code = job_code.strip()

    try:
        # 2. Find Notepad window
        all_windows = pyautogui.getAllWindows()

        windows = [
            w for w in all_windows
            if w.title and (
                "Notepad" in w.title
                or "Untitled" in w.title
                or job_code in w.title
            )
        ]

        if len(windows) == 0:
            return False, "Notepad window not found"

        if len(windows) > 1:
            return False, "Multiple matching windows found"

        notepad = windows[0]

        # 3. Copy Job Code
        pyperclip.copy(job_code)

        # 4. Verify Clipboard
        if pyperclip.paste() != job_code:
            return False, "Clipboard verification failed"

        # 5. Restore window if minimized
        if notepad.isMinimized:
            notepad.restore()
            time.sleep(1)

        # 6. Activate Notepad
        notepad.activate()
        time.sleep(2)

        # 7. Verify active window
        active = pyautogui.getActiveWindow()

        if active is None:
            return False, "Cannot detect active window"

        if active._hWnd != notepad._hWnd:
            return False, "Notepad activation failed"

        # 8. Paste Job Code
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

        return True, "Job Code paste command completed. Verify in Notepad."

    except pyautogui.FailSafeException:
        return False, "Emergency stop activated"

    except Exception as e:
        return False, f"Automation error: {type(e).__name__}: {e}"
