import win32com.client
import time

shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("{RIGHT}")

while(True):
	shell.SendKeys("{RIGHT}")
	time.sleep(1)
