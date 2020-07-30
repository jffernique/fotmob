import requests
from bs4 import BeautifulSoup
import re
from re import search
from lxml import html
import time


xx = int(input('Combien de matchs sans 2 ou 3 buts : '))
ele=[]
leagues = {'https://www.fotmob.com/leagues/223/table': 'J. League',
           'https://www.fotmob.com/leagues/268/table': 'Serie A',
           'https://www.fotmob.com/leagues/40/table': 'First Division A',
           'https://www.fotmob.com/leagues/46/table': 'Superligaen',
           'https://www.fotmob.com/leagues/47/table': 'Premier League',
           'https://www.fotmob.com/leagues/48/table': 'Championship',
           'https://www.fotmob.com/leagues/53/table': 'Ligue 1',
           'https://www.fotmob.com/leagues/54/table': '1. Bundesliga',
           'https://www.fotmob.com/leagues/55/table': 'Serie A',
           'https://www.fotmob.com/leagues/57/table': 'Eredivisie',
           'https://www.fotmob.com/leagues/59/table': 'Eliteserien',
           'https://www.fotmob.com/leagues/61/table': 'Primeira Liga',
           'https://www.fotmob.com/leagues/63/table': 'Premier League',
           'https://www.fotmob.com/leagues/64/table': 'Premiership',
           'https://www.fotmob.com/leagues/67/table': 'Allsvenskan',
           'https://www.fotmob.com/leagues/69/table': 'Super League',
           'https://www.fotmob.com/leagues/71/table': 'Super Lig',
           'https://www.fotmob.com/leagues/85/table': '1. Division',
           'https://www.fotmob.com/leagues/86/table': 'Serie B',
           'https://www.fotmob.com/leagues/87/table': 'LaLiga',
           'https://www.fotmob.com/leagues/110/table': 'Ligue 2',
           'https://www.fotmob.com/leagues/112/table': 'Superliga',
           'https://www.fotmob.com/leagues/113/table': 'A-League',
           'https://www.fotmob.com/leagues/116/table': 'Premier League',
           'https://www.fotmob.com/leagues/120/table': 'Super League',
           'https://www.fotmob.com/leagues/121/table': 'Primera Division',
           'https://www.fotmob.com/leagues/122/table': '1. Liga',
           'https://www.fotmob.com/leagues/123/table': 'Championship',
           'https://www.fotmob.com/leagues/126/table': 'Premier Division',
           'https://www.fotmob.com/leagues/127/table': 'Ligat HaAl',
           'https://www.fotmob.com/leagues/130/table': 'MLS',
           'https://www.fotmob.com/leagues/140/table': 'LaLiga2',
           'https://www.fotmob.com/leagues/146/table': '2. Bundesliga',
           'https://www.fotmob.com/leagues/176/table': 'Super Liga',
           'https://www.fotmob.com/leagues/182/table': 'Super Liga',
           'https://www.fotmob.com/leagues/189/table': 'Liga I',
           'https://www.fotmob.com/leagues/196/table': 'Ekstraklasa',
           'https://www.fotmob.com/leagues/38/table': 'Bundesliga'

           }
countrys = {'https://www.fotmob.com/leagues/223/table': 'Japan',
            'https://www.fotmob.com/leagues/268/table': 'Brazil',
            'https://www.fotmob.com/leagues/40/table': 'Belgium',
            'https://www.fotmob.com/leagues/46/table': 'Danemark',
            'https://www.fotmob.com/leagues/47/table': 'UK',
            'https://www.fotmob.com/leagues/48/table': 'UK',
            'https://www.fotmob.com/leagues/53/table': 'France',
            'https://www.fotmob.com/leagues/54/table': 'Germany',
            'https://www.fotmob.com/leagues/55/table': 'Italy',
            'https://www.fotmob.com/leagues/57/table': 'Nederland',
            'https://www.fotmob.com/leagues/59/table': 'Norway',
            'https://www.fotmob.com/leagues/61/table': 'Portugal',
            'https://www.fotmob.com/leagues/63/table': 'Russia',
            'https://www.fotmob.com/leagues/64/table': 'Scotland',
            'https://www.fotmob.com/leagues/67/table': 'Sweden',
            'https://www.fotmob.com/leagues/69/table': 'Switzerland',
            'https://www.fotmob.com/leagues/71/table': 'Turkey',
            'https://www.fotmob.com/leagues/85/table': 'Danemark',
            'https://www.fotmob.com/leagues/86/table': 'Italy',
            'https://www.fotmob.com/leagues/87/table': 'Spain',
            'https://www.fotmob.com/leagues/110/table': 'France',
            'https://www.fotmob.com/leagues/112/table': 'Argentina',
            'https://www.fotmob.com/leagues/113/table': 'Australia',
            'https://www.fotmob.com/leagues/116/table': 'Wales',
            'https://www.fotmob.com/leagues/120/table': 'China',
            'https://www.fotmob.com/leagues/121/table': 'Costa Rica',
            'https://www.fotmob.com/leagues/122/table': 'Czech Republic',
            'https://www.fotmob.com/leagues/123/table': 'Scotland',
            'https://www.fotmob.com/leagues/126/table': 'Ireland',
            'https://www.fotmob.com/leagues/127/table': 'Israel',
            'https://www.fotmob.com/leagues/140/table': 'Spain',
            'https://www.fotmob.com/leagues/146/table': 'Germany',
            'https://www.fotmob.com/leagues/176/table': 'Slovakia',
            'https://www.fotmob.com/leagues/182/table': 'Serbia',
            'https://www.fotmob.com/leagues/189/table': 'Romania',
            'https://www.fotmob.com/leagues/196/table': 'Poland',
            'https://www.fotmob.com/leagues/130/table': 'MLS',
            'https://www.fotmob.com/leagues/38/table': 'Austria'

            }
links = ['https://www.fotmob.com/leagues/223/table',
         'https://www.fotmob.com/leagues/268/table',
         'https://www.fotmob.com/leagues/40/table',
         'https://www.fotmob.com/leagues/46/table',
         'https://www.fotmob.com/leagues/47/table',
         'https://www.fotmob.com/leagues/48/table',
         'https://www.fotmob.com/leagues/53/table',
         'https://www.fotmob.com/leagues/54/table',
         'https://www.fotmob.com/leagues/55/table',
         'https://www.fotmob.com/leagues/57/table',
         'https://www.fotmob.com/leagues/59/table',
         'https://www.fotmob.com/leagues/61/table',
         'https://www.fotmob.com/leagues/63/table',
         'https://www.fotmob.com/leagues/64/table',
         'https://www.fotmob.com/leagues/67/table',
         'https://www.fotmob.com/leagues/69/table',
         'https://www.fotmob.com/leagues/71/table',
         'https://www.fotmob.com/leagues/85/table',
         'https://www.fotmob.com/leagues/86/table',
         'https://www.fotmob.com/leagues/87/table',
         'https://www.fotmob.com/leagues/110/table',
         'https://www.fotmob.com/leagues/112/table',
         'https://www.fotmob.com/leagues/113/table',
         'https://www.fotmob.com/leagues/116/table',
         'https://www.fotmob.com/leagues/120/table',
         'https://www.fotmob.com/leagues/121/table',
         'https://www.fotmob.com/leagues/122/table',
         'https://www.fotmob.com/leagues/123/table',
         'https://www.fotmob.com/leagues/126/table',
         'https://www.fotmob.com/leagues/127/table',
         'https://www.fotmob.com/leagues/140/table',
         'https://www.fotmob.com/leagues/146/table',
         'https://www.fotmob.com/leagues/176/table',
         'https://www.fotmob.com/leagues/182/table',
         'https://www.fotmob.com/leagues/189/table',
         'https://www.fotmob.com/leagues/196/table',
         'https://www.fotmob.com/leagues/130/table',
         'https://www.fotmob.com/leagues/38/table'
         ]
for link in links:
    lin=link+"/undefined"
    webpage=requests.get(lin)
    league = leagues[link]
    country = countrys[link]
    #print(webpage.text)

    print("----------------------------------------------------------")
    print("Teams Of " + league + " => Country:" + country)
    print("----------------------------------------------------------")
    soup = BeautifulSoup(webpage.content, 'html.parser')
    #print(soup)
    ele = soup.find_all("div",{"class" : re.compile('.*emrg6e0.*')})
    #print(len(ele))

    #print (ele)
    for element in ele:
        eliminate = 0
        goals = []
        a = element.find("a",href=True)
        #print (a['href'])
        team_fixture = ("https://www.fotmob.com"+a['href']).replace('overview','fixtures')
        team_fixtures = requests.get(team_fixture)
        driver2=BeautifulSoup(team_fixtures.content,'html.parser')
        #driver2=html.fromstring(team_fixtures.content)
        #print (driver2.prettify())


        #league_names = driver2.find_elements_by_xpath("//span[@class='css-1pcgt64-league']")
        league_names = driver2.find_all("span",{"class" : "css-1pcgt64-league"})
        #print ("-----------------")
        #print(league_names)
        #league_names = driver2.xpath('//span[@class="css-1pcgt64-league"]/text()')
        #cards = driver2.find_all({'a' : '''ispastmatch="1"'''})
        #cards = driver2.find_all('div',{'a' : 'ispastmatch="1"'})
        cards =driver2.find_all('a',{'class': 'css-3mgmk0-FixtureTileDetailedCSS e1ltb3e20'})



        #print("-----------------")
        #print(cards)
        #cards = driver2.xpath('[@a="ispastmatch="1""]')

        matches = []
        for card in cards:
           # print (card)
            matches.append(card.find_all("span")[4])
        x = 0
        for match in matches:
            if search(league, league_names[x].text):
                if "-" in match.text:
                    score = match.text
                    goals_array = score.split(" - ")
                    home = int(goals_array[0])
                    away = int(goals_array[1])
                    goals.append(home + away)
            x += 1
        for goal in goals[-xx:]:
            if goal == 3 or goal == 2:
                eliminate = 1

        if len(goals) > 0 and eliminate == 0:
            print("Team : " + a.text)
            if len(goals) > xx:
                print(goals[-xx:])
            else:
                print(goals)
print("Scrap finish.....")
