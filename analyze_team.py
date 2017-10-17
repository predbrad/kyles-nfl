import requests

from bs4 import BeautifulSoup

def get_standings(team):
    """Gets the standings for an NFL Team"""

    return_dictionary = {
        "W":"",
        "L":"",
        "PF":"",
        "PA":"",
        "S":""
        }

    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    source_url = 'http://www.cbssports.com/nfl/standings'
    response = requests.get(source_url, timeout=10, headers={
        'User-agent': user_agent})

    doc = BeautifulSoup(response.text,'html.parser')

    trs = doc.select('tr')

    columns = ["TEAM","W","L","T","PCT","PF","PA","HOME","ROAD","DIV","PCT","AFC","PCT","NFC","STREAK"]

    for tr in trs:
        if team.lower() in str(tr).lower():
            tds = tr.select('td')
            w_index = columns.index('W')
            l_index = columns.index('L')
            streak_index = columns.index('STREAK')
            pf_index = columns.index('PF')
            pa_index = columns.index('PA')
            if len(tds) >= max([w_index,l_index,streak_index,pf_index,pa_index]):
                return_dictionary = {
                    "W":tds[w_index].getText().strip(),
                    "L":tds[l_index].getText().strip(),
                    "PF":tds[pf_index].getText().strip(),
                    "PA":tds[pa_index].getText().strip(),
                    "S":tds[streak_index].getText().strip()
                    }

    return return_dictionary


def get_lines(team):
    """Gets the betting lines for an NFL Team (current week only)"""

    return_dictionary = {
        "DATE":"",
        "FAVORITE":"",
        "LINE":"",
        "UNDERDOG":"",
        "TOTAL":""
        }

    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    source_url = 'http://www.footballlocks.com/nfl_lines.shtml'
    response = requests.get(source_url, timeout=10, headers={
        'User-agent': user_agent})

    doc = BeautifulSoup(response.text,'html.parser')

    trs = doc.select('tr')

    columns = ["DATE","FAVORITE","LINE","UNDERDOG","TOTAL"]

    for tr in trs:
        if team.lower() in str(tr).lower():
            tds = tr.select('td')
            d_index = columns.index('DATE')
            f_index = columns.index('FAVORITE')
            l_index = columns.index('LINE')
            u_index = columns.index('UNDERDOG')
            t_index = columns.index('TOTAL')
            if len(tds) >= max([d_index,f_index,l_index,u_index,t_index]):
                return_dictionary = {
                    "DATE":tds[d_index].getText().strip(),
                    "FAVORITE":tds[f_index].getText().strip(),
                    "LINE":tds[l_index].getText().strip(),
                    "UNDERDOG":tds[u_index].getText().strip(),
                    "TOTAL":tds[t_index].getText().strip()
                    }

    return return_dictionary


if __name__ == "__main__":
    """the Main function"""

    #TODO 1: Get the team from the user (let them input or pick from a list)
    #TODO 2: Get the standings of the team they're playing
    #TODO 3: Display in a nice way
    #TODO 4: Develop a model to beat vegas on the reg
    
    team='Philadelphia'
    print(get_lines(team))
    print(get_standings(team))

