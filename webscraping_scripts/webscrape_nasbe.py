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
        "https://statepolicies.nasbe.org/" +
        "health/categories/health-education/" +
        f"sexual-health-education-general-ms/{state}"
    )
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="field__item")

    f = open(f"../nasbe_policies/{state}.txt", "w+")
    for element in results[3:-2]:
        f.write(element.text)


if __name__ == "__main__":
    state_names = [
        "Alaska",
        "Alabama",
        "Arkansas",
        "Arizona",
        "California",
        "Colorado",
        "Connecticut",
        "District of Columbia",
        "Delaware",
        "Florida",
        "Georgia",
        "Guam",
        "Hawaii",
        "Iowa",
        "Idaho",
        "Illinois",
        "Indiana",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Massachusetts",
        "Maryland",
        "Maine",
        "Michigan",
        "Minnesota",
        "Missouri",
        "Mississippi",
        "Montana",
        "North Carolina",
        "North Dakota",
        "Nebraska",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "Nevada",
        "New York",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Virginia",
        "Virgin Islands",
        "Vermont",
        "Washington",
        "Wisconsin",
        "West Virginia",
        "Wyoming",
    ]
    for state in state_names:
        state = state.replace(" ", "-").lower()
        get_state_policy(state)
