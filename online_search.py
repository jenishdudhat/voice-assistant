import webbrowser
import wikipedia


if "play" in x:  
    webbrowser.open_new(f"https://www.youtube.com/results?search_query={x[1]}")
            
elif "search" in x:
    webbrowser.open_new(f"https://www.youtube.com/results?search_query={x[1]}")

else :
    print("sorry i didnt get it")