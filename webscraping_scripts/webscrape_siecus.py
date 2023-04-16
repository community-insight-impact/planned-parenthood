import requests
from bs4 import BeautifulSoup

def get_state_policy(state: str):
    """Saves txt files with the inputted state's policy

    Parameters
    ----------
    state : str
        name of the state
    """
    URL = (
        "https://siecus.org/state_profile/" +
        f"{state}-fy21-state-profile/"
    )
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    for link in soup.find_all('a')[10:]:
        print(link.string)
        print(link.get('href'))
    
if __name__ == "__main__":
    state_names = [
        "alaska",
        "alabama",
        "arkansas",
        "arizona",
        "california",
        "colorado",
        "connecticut",
        "district-of-columbia",
        "delaware",
        "florida",
        "georgia",
        "hawaii",
        "iowa",
        "idaho",
        "illinois",
        "indiana",
        "kansas",
        "kentucky",
        "louisiana",
        "massachusetts",
        "maryland",
        "maine",
        "michigan",
        "minnesota",
        "missouri",
        "mississippi",
        "montana",
        "north-carolina",
        "north-dakota",
        "nebraska",
        "new-hampshire",
        "new-jersey",
        "new-mexico",
        "nevada",
        "new-york",
        "ohio",
        "oklahoma",
        "oregon",
        "pennsylvania",
        "puerto-rico"
        "rhode-island",
        "south-carolina",
        "south-dakota",
        "tennessee",
        "texas",
        "utah",
        "virginia",
        "vermont",
        "washington",
        "wisconsin",
        "west-virginia",
        "wyoming",
    ]
    
    for state in state_names:
        get_state_policy(state)
