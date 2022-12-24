import webbrowser 
  
# Take query from user 
query = input("Search Google: ") 
  
# Open the browser and search 
webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)