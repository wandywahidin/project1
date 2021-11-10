import requests
from bs4 import BeautifulSoup


def get_data():
    content = requests.get('https://bmkg.go.id')
    soup = BeautifulSoup(content.text, 'html.parser')
    resultDiv = soup.find('div', {'class', "col-md-6 col-xs-6 gempabumi-detail no-padding"})
    result = resultDiv.findChildren('li')
    dateTime = None
    magnitude = None
    depth = None
    location = None
    epicenter = None
    felt = None

    i = 0  # Index
    for res in result:  # Variable res in varible result
        if i == 0:  # Index no 1
            dateTime = res.text  # Only Text in variable dateTime
        if i == 1:  # Index no 2
            magnitude = res.text  # Only Text in variable magnitude
        elif i == 2:
            depth = res.text
        elif i == 3:
            epicenter = res.text
        elif i == 4:
            location = res.text
        elif i == 5:
            felt = res.text
        i = i + 1

    output = dict()
    output['dateTime'] = dateTime
    output['magnitude'] = magnitude
    output['depth'] = depth
    output['epicenter'] = epicenter
    output['location'] = location
    output['felt'] = felt
    return output


def print_data(result):
    print('Latest Earthquake From BMKG')
    print(f"Date and Time {result['dateTime']}")
    print(f"Magnitude {result['magnitude']}")
    print(f"Depth {result['depth']}")
    print(f"Epicenter {result['epicenter']}")
    print(f"Location {result['location']}")
    print(f"Felt {result['felt']}")
