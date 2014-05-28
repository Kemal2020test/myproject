from selenium import webdriver
import unittest


browser = webdriver.Firefox()

# User checks the homepage
browser.get('http://localhost:8000')

#She sees page title, which is To-Do Lists
assert 'To-Do Lists' in browser.title, 'browser title was' + browser.title

#She enters a new to-do item

#She types "Buy peacock feathers"

#When she hits enter, the page says:
# 1: "Buy peacock feathers"

#There is a textbox blank available for new entries all the time

#She enters "Another one"

#Her list is stored , when she comes back with a specific URL she can see her list

browser.quit()