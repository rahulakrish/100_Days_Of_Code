# with open("C:\Users\e40050338\Documents\Python\Day 45 - Web Scraping with Beautiful Soup\bs4-start\website.html",encoding='utf-8') as file:
#     contents = file.read()
#     print(contents)
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'website.html')

print(script_dir)
print(file_path)

