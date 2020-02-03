import time
import requests
import json
requests.packages.urllib3.disable_warnings()
from .apiconf import api_confirmedcase, api_deathscase, api_recovercase, api_countrycase

def get_confirmed_case():
    try:
       headers = {'charset':'utf-8','Content-Type':'application/json', 'Accept':'application/json' }
       url = api_confirmedcase
       get_resp = requests.get(url, headers=headers, verify=False)
       if get_resp.status_code == 200:
          return get_resp
       else:
          return
    except requests.exceptions.ConnectionError:
       return

def get_death_case():
    try:
       headers = {'charset':'utf-8','Content-Type':'application/json', 'Accept':'application/json' }
       url = api_deathscase
       get_resp = requests.get(url, headers=headers, verify=False)
       if get_resp.status_code == 200:
          return get_resp
       else:
          return
    except requests.exceptions.ConnectionError:
       return

def get_recover_case():
    try:
       headers = {'charset':'utf-8','Content-Type':'application/json', 'Accept':'application/json' }
       url = api_recovercase
       get_resp = requests.get(url, headers=headers, verify=False)
       if get_resp.status_code == 200:
          return get_resp
       else:
          return
    except requests.exceptions.ConnectionError:
       return

def get_country_case():
    try:
       headers = {'charset':'utf-8','Content-Type':'application/json', 'Accept':'application/json' }
       url = api_countrycase
       get_resp = requests.get(url, headers=headers, verify=False)
       if get_resp.status_code == 200:
          return get_resp
       else:
          return
    except requests.exceptions.ConnectionError:
       return

def scheduled_task(task_id):
   for i in range(1):
      time.sleep(1)
      print('Task {} running iteration {}'.format(task_id, i)) 
      print("[Tracking-Apps] Crawling Scheduler")
      print("==================================")
      res = get_confirmed_case()
      data = res.json()
      print("Global Confirmed Case: %d" % data['features'][0]['attributes']['value'])
      confirm = data['features'][0]['attributes']['value']
      res = get_death_case()
      data = res.json()
      print("Global Deaths Case: %d" % data['features'][0]['attributes']['value'])
      death = data['features'][0]['attributes']['value']
      res = get_recover_case()
      data = res.json()
      print("Global Recover Case: %d" % data['features'][0]['attributes']['value'])
      recover = data['features'][0]['attributes']['value']
      print("==================================")
      f = open('./data/global.csv','w')
      f.write("Confirmed,Deaths,Recover\n")
      f.write("%d,%d,%d\n" % (confirm, death, recover))
      f.close()
      res = get_country_case()
      data = res.json()
      countrylen = len(data['features'])
      f = open('./data/country.csv','w')
      f.write("Country,Confirmed,Deaths,Recover\n")
      for n in range (countrylen):
         details = data['features'][n]['attributes']
         #print data['features'][n]['attributes']
         if details['Recovered'] is None and details['Deaths'] is None:
            print("Country: " + details['Country_Region'] + "\t Confirmed: %d" % details['Confirmed'] + "\t Deaths: None" + "\t Recovered: None")
            country = details['Country_Region']
            confirm = details['Confirmed']
            death = 0
            recover = 0
         elif details['Recovered'] is None and details['Deaths'] is not None:
            print("Country: " + details['Country_Region'] + "\t Confirmed: %d" % details['Confirmed'] + "\t Deaths: %d" % details['Deaths'] + "\t Recovered: None")
            country = details['Country_Region']
            confirm = details['Confirmed']
            death = details['Deaths']
            recover = 0
         elif details['Recovered'] is not None and details['Deaths'] is None:
            print("Country: " + details['Country_Region'] + "\t Confirmed: %d" % details['Confirmed'] + "\t Deaths: None" + "\t Recovered: %d" % details['Recovered'])
            country = details['Country_Region']
            confirm = details['Confirmed']
            death = 0
            recover = details['Recovered']
         else:
            print("Country: " + details['Country_Region'] + "\t Confirmed: %d" % details['Confirmed'] + "\t Deaths: %d" % details['Deaths'] + "\t Recovered: %d" % details['Recovered'])
            country = details['Country_Region']
            confirm = details['Confirmed']
            death = details['Deaths']
            recover = details['Recovered']
         print("===========================================================================================")
         f.write("%s,%d,%d,%d\n" % (country, confirm, death, recover))
      f.close()
