# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:46:30 2020

@author: krishna reddy
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'YearsExperience':2})

print(r.json())