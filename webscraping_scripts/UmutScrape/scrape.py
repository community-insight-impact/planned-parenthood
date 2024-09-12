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
    print(page)
    print(type(page))
    if page == None:
        print(state)
        print("State Not Found") 
        return 0

    soup = BeautifulSoup(page.content, "html.parser")
    f = open(f"stateData/{state}.txt", "w")
    main_body = soup.find("section", class_= "cf")
    for tag in main_body:
        f.write(tag.text + "\n")
        # print(tag.text)
    
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
        # "guam",
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
        # "virgin-islands",
        "vermont",
        "washington",
        "wisconsin",
        "west-virginia",
        "wyoming",
    ]

get_state_policy("puerto-rico")
# for state in state_names:
#     get_state_policy(state)
