import time
import webbrowser

breaks = 3
break_count = 0
print("This program started on "+time.ctime())
while True:
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=YtCcKCwpC7A")
    break_count+=1
    
