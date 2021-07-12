import win32com.client
import time

shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("{DOWN}")

while(True):
	shell.SendKeys("{DOWN}")
	time.sleep(1.5)
