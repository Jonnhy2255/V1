import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# Dictionnaire des équipes avec leurs URL correspondantes pour les résultats, fixtures et stats
teams_urls = {
    "Bournemouth": {
        "results": "https://www.espn.com/soccer/team/results/_/id/349/afc-bournemouth",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/349/afc-bournemouth",
        "stats": "https://africa.espn.com/football/team/stats/_/id/349/league/ENG.1/view/performance"
    },
    "Arsenal": {
        "results": "https://www.espn.com/soccer/team/results/_/id/359/arsenal",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/359/arsenal",
        "stats": "https://africa.espn.com/football/team/stats/_/id/359/league/ENG.1/view/performance"
    },
    "Aston Villa": {
        "results": "https://www.espn.com/soccer/team/results/_/id/362/aston-villa",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/362/aston-villa",
        "stats": "https://africa.espn.com/football/team/stats/_/id/362/league/ENG.1/view/performance"
    },
    "Brentford": {
        "results": "https://www.espn.com/soccer/team/results/_/id/337/brentford",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/337/brentford",
        "stats": "https://africa.espn.com/football/team/stats/_/id/337/league/ENG.1/view/performance"
    },
    "Brighton": {
        "results": "https://www.espn.com/soccer/team/results/_/id/331/brighton-hove-albion",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/331/brighton-hove-albion",
        "stats": "https://africa.espn.com/football/team/stats/_/id/331/league/ENG.1/view/performance"
    },
    "Chelsea": {
        "results": "https://www.espn.com/soccer/team/results/_/id/363/chelsea",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/363/chelsea",
        "stats": "https://africa.espn.com/football/team/stats/_/id/363/league/ENG.1/view/performance"
    },
    "Crystal Palace": {
        "results": "https://www.espn.com/soccer/team/results/_/id/384/crystal-palace",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/384/crystal-palace",
        "stats": "https://africa.espn.com/football/team/stats/_/id/384/league/ENG.1/view/performance"
    },
    "Everton": {
        "results": "https://www.espn.com/soccer/team/results/_/id/368/everton",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/368/everton",
        "stats": "https://africa.espn.com/football/team/stats/_/id/368/league/ENG.1/view/performance"
    },
    "Fulham": {
        "results": "https://www.espn.com/soccer/team/results/_/id/370/fulham",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/370/fulham",
        "stats": "https://africa.espn.com/football/team/stats/_/id/370/league/ENG.1/view/performance"
    },
    "Ipswich Town": {
        "results": "https://www.espn.com/soccer/team/results/_/id/373/ipswich-town",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/373/ipswich-town",
        "stats": "https://africa.espn.com/football/team/stats/_/id/373/league/ENG.1/view/performance"
    },
    "Leicester City": {
        "results": "https://www.espn.com/soccer/team/results/_/id/375/leicester-city",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/375/leicester-city",
        "stats": "https://africa.espn.com/football/team/stats/_/id/375/league/ENG.1/view/performance"
    },
    "Liverpool": {
        "results": "https://www.espn.com/soccer/team/results/_/id/364/liverpool",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/364/liverpool",
        "stats": "https://africa.espn.com/football/team/stats/_/id/364/league/ENG.1/view/performance"
    },
    "Manchester City": {
        "results": "https://www.espn.com/soccer/team/results/_/id/382/manchester-city",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/382/manchester-city",
        "stats": "https://africa.espn.com/football/team/stats/_/id/382/league/ENG.1/view/performance"
    },
    "Manchester United": {
        "results": "https://www.espn.com/soccer/team/results/_/id/360/manchester-united",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/360/manchester-united",
        "stats": "https://africa.espn.com/football/team/stats/_/id/360/league/ENG.1/view/performance"
    },
    "Newcastle United": {
        "results": "https://www.espn.com/soccer/team/results/_/id/361/newcastle-united",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/361/newcastle-united",
        "stats": "https://africa.espn.com/football/team/stats/_/id/361/league/ENG.1/view/performance"
    },
    "Nottingham Forest": {
        "results": "https://www.espn.com/soccer/team/results/_/id/393/nottingham-forest",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/393/nottingham-forest",
        "stats": "https://africa.espn.com/football/team/stats/_/id/393/league/ENG.1/view/performance"
    },
    "Southampton": {
        "results": "https://www.espn.com/soccer/team/results/_/id/376/southampton",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/376/southampton",
        "stats": "https://africa.espn.com/football/team/stats/_/id/376/league/ENG.1/view/performance"
    },
    "Tottenham Hotspur": {
        "results": "https://www.espn.com/soccer/team/results/_/id/367/tottenham-hotspur",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/367/tottenham-hotspur",
        "stats": "https://africa.espn.com/football/team/stats/_/id/367/league/ENG.1/view/performance"
    },
    "West Ham United": {
        "results": "https://www.espn.com/soccer/team/results/_/id/371/west-ham-united",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/371/west-ham-united",
        "stats": "https://africa.espn.com/football/team/stats/_/id/371/league/ENG.1/view/performance"
    },
    "Wolverhampton Wanderers": {
        "results": "https://www.espn.com/soccer/team/results/_/id/380/wolverhampton-wanderers",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/380/wolverhampton-wanderers",
        "stats": "https://africa.espn.com/football/team/stats/_/id/380/league/ENG.1/view/performance"
    },
    "FC Heidenheim 1846": {
        "results": "https://www.espn.com/soccer/team/results/_/id/6418/1-fc-heidenheim-1846",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/6418/1-fc-heidenheim-1846",
        "stats": "https://africa.espn.com/football/team/stats/_/id/6418/league/GER.1/view/performance"
    },
    "FC Union Berlin": {
        "results": "https://www.espn.com/soccer/team/results/_/id/598/1-fc-union-berlin",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/598/1-fc-union-berlin",
        "stats": "https://africa.espn.com/football/team/stats/_/id/598/league/GER.1/view/performance"
    },
    "Bayer Leverkusen": {
        "results": "https://www.espn.com/soccer/team/results/_/id/131/bayer-leverkusen",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/131/bayer-leverkusen",
        "stats": "https://africa.espn.com/football/team/stats/_/id/131/league/GER.1/view/performance"
    },
    "Bayern Munich": {
        "results": "https://www.espn.com/soccer/team/results/_/id/132/bayern-munich",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/132/bayern-munich",
        "stats": "https://africa.espn.com/football/team/stats/_/id/132/league/GER.1/view/performance"
    },
    "Borussia Dortmund": {
        "results": "https://www.espn.com/soccer/team/results/_/id/124/borussia-dortmund",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/124/borussia-dortmund",
        "stats": "https://africa.espn.com/football/team/stats/_/id/124/league/GER.1/view/performance"
    },
    "Borussia Monchengladbach": {
        "results": "https://www.espn.com/soccer/team/results/_/id/268/borussia-monchengladbach",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/268/borussia-monchengladbach",
        "stats": "https://africa.espn.com/football/team/stats/_/id/268/league/GER.1/view/performance"
    },
    "Eintracht Frankfurt": {
        "results": "https://www.espn.com/soccer/team/results/_/id/125/eintracht-frankfurt",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/125/eintracht-frankfurt",
        "stats": "https://africa.espn.com/football/team/stats/_/id/125/league/GER.1/view/performance"
    },
    "FC Augsburg": {
        "results": "https://www.espn.com/soccer/team/results/_/id/3841/fc-augsburg",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/3841/fc-augsburg",
        "stats": "https://africa.espn.com/football/team/stats/_/id/3841/league/GER.1/view/performance"
    },
    "Holstein Kiel": {
        "results": "https://www.espn.com/soccer/team/results/_/id/7884/holstein-kiel",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/7884/holstein-kiel",
        "stats": "https://africa.espn.com/football/team/stats/_/id/7884/league/GER.1/view/performance"
    },
    "Mainz": {
        "results": "https://www.espn.com/soccer/team/results/_/id/2950/mainz",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/2950/mainz",
        "stats": "https://africa.espn.com/football/team/stats/_/id/2950/league/GER.1/view/performance"
    },
    "RB Leipzig": {
        "results": "https://www.espn.com/soccer/team/results/_/id/11420/rb-leipzig",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/11420/rb-leipzig",
        "stats": "https://africa.espn.com/football/team/stats/_/id/11420/league/GER.1/view/performance"
    },
    "SC Freiburg": {
        "results": "https://www.espn.com/soccer/team/results/_/id/126/sc-freiburg",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/126/sc-freiburg",
        "stats": "https://africa.espn.com/football/team/stats/_/id/126/league/GER.1/view/performance"
    },
    "St. Pauli": {
        "results": "https://www.espn.com/soccer/team/results/_/id/270/st-pauli",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/270/st-pauli",
        "stats": "https://africa.espn.com/football/team/stats/_/id/270/league/GER.1/view/performance"
    },
    "TSG Hoffenheim": {
        "results": "https://www.espn.com/soccer/team/results/_/id/7911/tsg-hoffenheim",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/7911/tsg-hoffenheim",
        "stats": "https://africa.espn.com/football/team/stats/_/id/7911/league/GER.1/view/performance"
    },
    "VfB Stuttgart": {
        "results": "https://www.espn.com/soccer/team/results/_/id/134/vfb-stuttgart",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/134/vfb-stuttgart",
        "stats": "https://africa.espn.com/football/team/stats/_/id/134/league/GER.1/view/performance"
    },
    "VfL Bochum": {
        "results": "https://www.espn.com/soccer/team/results/_/id/121/vfl-bochum",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/121/vfl-bochum",
        "stats": "https://africa.espn.com/football/team/stats/_/id/121/league/GER.1/view/performance"
    },
    "VfL Wolfsburg": {
        "results": "https://www.espn.com/soccer/team/results/_/id/138/vfl-wolfsburg",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/138/vfl-wolfsburg",
        "stats": "https://africa.espn.com/football/team/stats/_/id/138/league/GER.1/view/performance"
    },
    "Werder Bremen": {
        "results": "https://www.espn.com/soccer/team/results/_/id/137/werder-bremen",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/137/werder-bremen",
        "stats": "https://africa.espn.com/football/team/stats/_/id/137/league/GER.1/view/performance"
    },
    "Alavés": {
        "results": "https://www.espn.com/soccer/team/results/_/id/96/alaves",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/96/alaves",
        "stats": "https://africa.espn.com/football/team/stats/_/id/96/league/ESP.1/view/performance"
    },
    "Athletic Bilbao": {
        "results": "https://www.espn.com/soccer/team/results/_/id/93/athletic-club",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/93/athletic-club",
        "stats": "https://africa.espn.com/football/team/stats/_/id/93/league/ESP.1/view/performance"
    },
    "Atlético Madrid": {
        "results": "https://www.espn.com/soccer/team/results/_/id/1068/atletico-madrid",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/1068/atletico-madrid",
        "stats": "https://africa.espn.com/football/team/stats/_/id/1068/league/ESP.1/view/performance"
    },
    "Barcelona": {
        "results": "https://www.espn.com/soccer/team/results/_/id/83/barcelona",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/83/barcelona",
        "stats": "https://africa.espn.com/football/team/stats/_/id/83/league/ESP.1/view/performance"
    },
    "Celta Vigo": {
        "results": "https://www.espn.com/soccer/team/results/_/id/85/celta-vigo",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/85/celta-vigo",
        "stats": "https://africa.espn.com/football/team/stats/_/id/85/league/ESP.1/view/performance"
    },
    "Espanyol": {
        "results": "https://www.espn.com/soccer/team/results/_/id/88/espanyol",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/88/espanyol",
        "stats": "https://africa.espn.com/football/team/stats/_/id/88/league/ESP.1/view/performance"
    },
    "Getafe": {
        "results": "https://www.espn.com/soccer/team/results/_/id/2922/getafe",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/2922/getafe",
        "stats": "https://africa.espn.com/football/team/stats/_/id/2922/league/ESP.1/view/performance"
    },
    "Girona": {
        "results": "https://www.espn.com/soccer/team/results/_/id/9812/girona",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/9812/girona",
        "stats": "https://africa.espn.com/football/team/stats/_/id/9812/league/ESP.1/view/performance"
    },
    "Las Palmas": {
        "results": "https://www.espn.com/soccer/team/results/_/id/98/las-palmas",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/98/las-palmas",
        "stats": "https://africa.espn.com/football/team/stats/_/id/98/league/ESP.1/view/performance"
    },
    "Leganés": {
        "results": "https://www.espn.com/soccer/team/results/_/id/17534/leganes",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/17534/leganes",
        "stats": "https://africa.espn.com/football/team/stats/_/id/17534/league/ESP.1/view/performance"
    },
    "Mallorca": {
        "results": "https://www.espn.com/soccer/team/results/_/id/84/mallorca",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/84/mallorca",
        "stats": "https://africa.espn.com/football/team/stats/_/id/84/league/ESP.1/view/performance"
    },
    "Osasuna": {
        "results": "https://www.espn.com/soccer/team/results/_/id/97/osasuna",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/97/osasuna",
        "stats": "https://africa.espn.com/football/team/stats/_/id/97/league/ESP.1/view/performance"
    },
    "Rayo Vallecano": {
        "results": "https://www.espn.com/soccer/team/results/_/id/101/rayo-vallecano",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/101/rayo-vallecano",
        "stats": "https://africa.espn.com/football/team/stats/_/id/101/league/ESP.1/view/performance"
    },
    "Real Betis": {
        "results": "https://www.espn.com/soccer/team/results/_/id/244/real-betis",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/244/real-betis",
        "stats": "https://africa.espn.com/football/team/stats/_/id/244/league/ESP.1/view/performance"
    },
    "Real Madrid": {
        "results": "https://www.espn.com/soccer/team/results/_/id/86/real-madrid",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/86/real-madrid",
        "stats": "https://africa.espn.com/football/team/stats/_/id/86/league/ESP.1/view/performance"
    },
    "Real Sociedad": {
        "results": "https://www.espn.com/soccer/team/results/_/id/89/real-sociedad",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/89/real-sociedad",
        "stats": "https://africa.espn.com/football/team/stats/_/id/89/league/ESP.1/view/performance"
    },
    "Real Valladolid": {
        "results": "https://www.espn.com/soccer/team/results/_/id/95/real-valladolid",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/95/real-valladolid",
        "stats": "https://africa.espn.com/football/team/stats/_/id/95/league/ESP.1/view/performance"
    },
    "Sevilla": {
        "results": "https://www.espn.com/soccer/team/results/_/id/243/sevilla",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/243/sevilla",
        "stats": "https://africa.espn.com/football/team/stats/_/id/243/league/ESP.1/view/performance"
    },
    "Valencia": {
        "results": "https://www.espn.com/soccer/team/results/_/id/94/valencia",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/94/valencia",
        "stats": "https://africa.espn.com/football/team/stats/_/id/94/league/ESP.1/view/performance"
    },
    "Villarreal": {
        "results": "https://www.espn.com/soccer/team/results/_/id/102/villarreal",
        "fixtures": "https://www.espn.com/soccer/team/fixtures/_/id/102/villarreal",
        "stats": "https://africa.espn.com/football/team/stats/_/id/102/league/ESP.1/view/performance"
    },
    "Milan": {
    "results": "https://africa.espn.com/football/team/results/_/id/103/ac-milan",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/103/ac-milan",
    "stats": "https://africa.espn.com/football/team/stats/_/id/103/league/ITA.1/view/performance"
  },
  "Atalanta": {
    "results": "https://africa.espn.com/football/team/results/_/id/105/atalanta",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/105/atalanta",
    "stats": "https://africa.espn.com/football/team/stats/_/id/105/league/ITA.1/view/performance"
  },
  "AS Roma": {
    "results": "https://africa.espn.com/football/team/results/_/id/104/as-roma",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/104/as-roma",
    "stats": "https://africa.espn.com/football/team/stats/_/id/104/league/ITA.1/view/performance"
  },
  "Bologne": {
    "results": "https://africa.espn.com/football/team/results/_/id/107/bologna",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/107/bologna",
    "stats": "https://africa.espn.com/football/team/stats/_/id/107/league/ITA.1/view/performance"
  },
  "Cagliari": {
    "results": "https://africa.espn.com/football/team/results/_/id/2925/cagliari",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/2925/cagliari",
    "stats": "https://africa.espn.com/football/team/stats/_/id/2925/league/ITA.1/view/performance"
  },
  "Como": {
    "results": "https://africa.espn.com/football/team/results/_/id/2572/como",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/2572/como",
    "stats": "https://africa.espn.com/football/team/stats/_/id/2572/league/ITA.1/view/performance"
  },
  "Empoli": {
    "results": "https://africa.espn.com/football/team/results/_/id/2574/empoli",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/2574/empoli",
    "stats": "https://africa.espn.com/football/team/stats/_/id/2574/league/ITA.1/view/performance"
  },
  "Fiorentina": {
    "results": "https://africa.espn.com/football/team/results/_/id/109/fiorentina",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/109/fiorentina",
    "stats": "https://africa.espn.com/football/team/stats/_/id/109/league/ITA.1/view/performance"
  },
  "Genoa": {
    "results": "https://africa.espn.com/football/team/results/_/id/3263/genoa",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/3263/genoa",
    "stats": "https://africa.espn.com/football/team/stats/_/id/3263/league/ITA.1/view/performance"
  },
  "Hellas Vérone": {
    "results": "https://africa.espn.com/football/team/results/_/id/119/hellas-verona",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/119/hellas-verona",
    "stats": "https://africa.espn.com/football/team/stats/_/id/119/league/ITA.1/view/performance"
  },
  "Inter Milan": {
    "results": "https://africa.espn.com/football/team/results/_/id/110/internazionale",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/110/internazionale",
    "stats": "https://africa.espn.com/football/team/stats/_/id/110/league/ITA.1/view/performance"
  },
  "Juventus": {
    "results": "https://africa.espn.com/football/team/results/_/id/111/juventus",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/111/juventus",
    "stats": "https://africa.espn.com/football/team/stats/_/id/111/league/ITA.1/view/performance"
  },
  "Lazio": {
    "results": "https://africa.espn.com/football/team/results/_/id/112/lazio",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/112/lazio",
    "stats": "https://africa.espn.com/football/team/stats/_/id/112/league/ITA.1/view/performance"
  },
  "Lecce": {
    "results": "https://africa.espn.com/football/team/results/_/id/113/lecce",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/113/lecce",
    "stats": "https://africa.espn.com/football/team/stats/_/id/113/league/ITA.1/view/performance"
  },
  "Monza": {
    "results": "https://africa.espn.com/football/team/results/_/id/4007/monza",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/4007/monza",
    "stats": "https://africa.espn.com/football/team/stats/_/id/4007/league/ITA.1/view/performance"
  },
  "Napoli": {
    "results": "https://africa.espn.com/football/team/results/_/id/114/napoli",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/114/napoli",
    "stats": "https://africa.espn.com/football/team/stats/_/id/114/league/ITA.1/view/performance"
  },
  "Parma": {
    "results": "https://africa.espn.com/football/team/results/_/id/115/parma",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/115/parma",
    "stats": "https://africa.espn.com/football/team/stats/_/id/115/league/ITA.1/view/performance"
  },
  "Torino": {
    "results": "https://africa.espn.com/football/team/results/_/id/239/torino",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/239/torino",
    "stats": "https://africa.espn.com/football/team/stats/_/id/239/league/ITA.1/view/performance"
  },
  "Udinese": {
    "results": "https://africa.espn.com/football/team/results/_/id/118/udinese",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/118/udinese",
    "stats": "https://africa.espn.com/football/team/stats/_/id/118/league/ITA.1/view/performance"
  },
  "Venize": {
    "results": "https://africa.espn.com/football/team/results/_/id/17530/venezia",
    "fixtures": "https://africa.espn.com/football/team/fixtures/_/id/17530/venezia",
    "stats": "https://africa.espn.com/football/team/stats/_/id/17530/league/ITA.1/view/performance"
  }
    # Ajoutez ici les autres équipes
}

# Dictionnaire des ligues avec les URLs
leagues_urls = {
    'premier league': 'https://www.espn.com/soccer/table/_/league/eng.1',
    'la liga': 'https://www.espn.com/soccer/table/_/league/esp.1',
    'serie a': 'https://www.espn.com/soccer/table/_/league/ita.1',
    'bundesliga':'https://africa.espn.com/football/table/_/league/ger.1/season/2024'
}

# En-têtes HTTP pour imiter un navigateur
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Fonction pour scraper les résultats ou les fixtures d'une équipe
def scrape_team_data(team_name, action):
    url = teams_urls.get(team_name, {}).get(action, None)
    if not url:
        print(f"URL non trouvée pour {team_name} et action {action}.")
        return []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        matches = soup.find_all('tr', class_='Table__TR')

        # Créer un tableau pour les résultats ou fixtures
        table = PrettyTable()
        table.field_names = ["Date", "Équipe 1", "Équipe 2", "Compétition", "Score", "Statut"]

        valid_results = []

        for match in matches:
            date = match.find('div', class_='matchTeams').text.strip() if match.find('div', class_='matchTeams') else "N/A"
            teams = match.find_all('a', class_='AnchorLink Table__Team')
            if len(teams) == 2:
                team1 = teams[0].text.strip()
                team2 = teams[1].text.strip()
            else:
                team1 = team2 = "N/A"
            competition = match.find_all('a', class_='AnchorLink')[1].text.strip() if len(match.find_all('a', 'AnchorLink')) > 1 else "N/A"
            score = match.find('span').text.strip() if match.find('span') else "N/A"
            status = match.find_all('a', class_='AnchorLink')[-1].text.strip() if match.find_all('a', 'AnchorLink') else "N/A"

            if date != "N/A" and team1 != "N/A" and team2 != "N/A" and score != "N/A":
                valid_results.append((date, team1, team2, competition, score, status))

        valid_results = valid_results[:5]  # Limiter à 5 résultats

        for result in valid_results:
            table.add_row(result)

        print(f"\n{action.capitalize()} pour {team_name}:")
        print(table)

        return valid_results

    except Exception as e:
        print(f"Une erreur est survenue pour {team_name}: {e}")
        return []

# Fonction pour scraper les statistiques d'une équipe
def scrape_team_stats(team_name):
    url = teams_urls.get(team_name, {}).get('stats', None)
    if not url:
        print(f"URL non trouvée pour {team_name} et action stats.")
        return {}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraction du tableau principal des statistiques
        stats_table = soup.find('table', class_='Table')
        if not stats_table:
            print("Tableau de statistiques non trouvé.")
            return {}

        stats = {}
        rows = stats_table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                stat_name = cols[0].text.strip()
                stat_value = cols[1].text.strip()
                stats[stat_name] = stat_value

        print(f"\nStatistiques pour {team_name}:")
        for stat_name, stat_value in stats.items():
            print(f"{stat_name}: {stat_value}")

        return stats

    except Exception as e:
        print(f"Une erreur est survenue pour {team_name}: {e}")
        return {}

# Fonction pour obtenir le classement d'une équipe à partir de son nom
def get_team_position(team_name):
    for league_name, url in leagues_urls.items():
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extraction des données de classement
            table_rows = soup.find_all('tr', class_='Table__TR')

            for row in table_rows:
                position = row.find('span', class_='team-position').text if row.find('span', class_='team-position') else None
                team = row.find('span', class_='hide-mobile').text if row.find('span', 'hide-mobile') else None
                if position and team:
                    if team_name.lower() in team.lower():
                        return int(position), league_name.capitalize()

        except Exception as e:
            print(f"Une erreur est survenue lors de la récupération du classement pour {league_name}: {e}")

    print(f"L'équipe '{team_name}' n'a pas été trouvée dans les ligues suivies.")
    return None, None

# Fonction pour analyser un match entre deux équipes avec des données plus complètes
def analyze_match(team1, team2):
    print(f"Collecte des données pour {team1} et {team2}...")

    # Récupérer les résultats récents des deux équipes
    results_team1 = scrape_team_data(team1, 'results')
    results_team2 = scrape_team_data(team2, 'results')

    # Récupérer les positions dans la ligue
    position_team1, league_team1 = get_team_position(team1)
    position_team2, league_team2 = get_team_position(team2)

    # Récupérer les statistiques des deux équipes
    stats_team1 = scrape_team_stats(team1)
    stats_team2 = scrape_team_stats(team2)

    if not results_team1 or not results_team2:
        print("Impossible de récupérer les résultats pour l'une ou les deux équipes.")
        return

    if position_team1 is None or position_team2 is None:
        print("Impossible de récupérer les positions pour l'une ou les deux équipes.")
        return

    # Afficher les positions des deux équipes
    print(f"\n{team1} est à la position {position_team1} dans {league_team1}.")
    print(f"{team2} est à la position {position_team2} dans {league_team2}.")

    # Calculer les probabilités de victoire pour chaque équipe
    def calculate_win_probabilities(results, team_name):
        total_matches = len(results)
        wins = sum(1 for result in results if result[1] == team_name and result[4].split('-')[0] > result[4].split('-')[1])
        draws = sum(1 for result in results if result[4].split('-')[0] == result[4].split('-')[1])
        losses = total_matches - wins - draws

        win_prob = (wins / total_matches) * 100 if total_matches > 0 else 0
        draw_prob = (draws / total_matches) * 100 if total_matches > 0 else 0
        loss_prob = (losses / total_matches) * 100 if total_matches > 0 else 0

        return win_prob, draw_prob, loss_prob

    win_prob_team1, draw_prob_team1, loss_prob_team1 = calculate_win_probabilities(results_team1, team1)
    win_prob_team2, draw_prob_team2, loss_prob_team2 = calculate_win_probabilities(results_team2, team2)

    # Calculer les probabilités de buts
    def calculate_goals_probabilities(results):
        total_goals = 0
        total_matches = len(results)

        for result in results:
            score = result[4]
            if '-' in score:
                goals = score.split('-')
                if len(goals) == 2:
                    total_goals += int(goals[0]) + int(goals[1])

        avg_goals = total_goals / total_matches if total_matches > 0 else 0

        prob_0_5 = 0
        prob_1_5 = 0
        prob_2_5 = 0

        for result in results:
            score = result[4]
            if '-' in score:
                goals = score.split('-')
                if len(goals) == 2:
                    goals_scored = int(goals[0]) + int(goals[1])
                    if goals_scored > 0:
                        prob_0_5 += 1
                    if goals_scored >= 2:
                        prob_1_5 += 1
                    if goals_scored >= 3:
                        prob_2_5 += 1

        prob_0_5 = (prob_0_5 / total_matches) * 100 if total_matches > 0 else 0
        prob_1_5 = (prob_1_5 / total_matches) * 100 if total_matches > 0 else 0
        prob_2_5 = (prob_2_5 / total_matches) * 100 if total_matches > 0 else 0

        return prob_0_5, prob_1_5, prob_2_5

    goals_prob_team1 = calculate_goals_probabilities(results_team1)
    goals_prob_team2 = calculate_goals_probabilities(results_team2)

    # Ajuster les probabilités en fonction des positions dans la ligue
    position_factor = (position_team2 - position_team1) / max(position_team1, position_team2) if position_team1 and position_team2 else 0
    win_prob_team1 += position_factor * 10
    win_prob_team2 -= position_factor * 10

    # Afficher les résultats de l'analyse
    print(f"\nAnalyse pour le match entre {team1} et {team2}:")
    print(f"Chance de victoire pour {team1}: {win_prob_team1:.2f}%")
    print(f"Chance de victoire pour {team2}: {win_prob_team2:.2f}%")
    print(f"Probabilités de buts dans le match :")
    print(f"  +0.5 buts : {max(goals_prob_team1[0], goals_prob_team2[0]):.2f}%")
    print(f"  +1.5 buts : {max(goals_prob_team1[1], goals_prob_team2[1]):.2f}%")
    print(f"  +2.5 buts : {max(goals_prob_team1[2], goals_prob_team2[2]):.2f}%")

# Fonction principale
def main():
    while True:
        action = input("\nTapez 'results' pour les résultats, 'fixtures' pour les fixtures, 'stats' pour les statistiques, 'rankings' pour connaître la position d'une équipe, 'analyze' pour analyser un match, ou 'quit' pour quitter: ").lower()

        if action == 'quit':
            print("Merci d'avoir utilisé le script v8 de Pronostics IA. Que Dieu facilite nos pronostics🙏!")
            break
        elif action in ['results', 'fixtures', 'stats']:
            team_name = input("Entrez le nom de l'équipe: ").strip()
            if team_name in teams_urls:
                if action == 'stats':
                    scrape_team_stats(team_name)
                else:
                    scrape_team_data(team_name, action)
            else:
                print(f"Équipe non trouvée: {team_name}. Veuillez vérifier le nom de l'équipe.")
        elif action == 'rankings':
            team_name = input("Entrez le nom de l'équipe pour connaître sa position: ").strip()
            position, league = get_team_position(team_name)
            if position:
                print(f"L'équipe '{team_name}' se trouve à la position {position} dans la ligue {league}.")
            else:
                print("Équipe non trouvée.")
        elif action == 'analyze':
            team1 = input("Entrez le nom de la première équipe: ").strip()
            team2 = input("Entrez le nom de la deuxième équipe: ").strip()

            if team1 in teams_urls and team2 in teams_urls:
                analyze_match(team1, team2)
            else:
                print("Une ou les deux équipes n'ont pas été trouvées. Veuillez vérifier les noms des équipes.")
        else:
            print("Action invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
