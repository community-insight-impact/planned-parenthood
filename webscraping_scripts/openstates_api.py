import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_metadata(jurisdiction: str, identifier: str):
    """Gets the metadata for a policy

    Parameters
    ----------
    jurisdiction : str
        jurisdiction of policy
    identifier : str
        identifier of policy
    """
    endpoint = "https://v3.openstates.org/bills"
    query_params = {
        "apikey": api_key,
        "jurisdiction": jurisdiction,
        "identifier": identifier,
        "include": "sources"
    }
    response = requests.get(endpoint, params=query_params)
    res = response.json()["results"]

    formatted_results = []
    for results in res:
        formatted_results.append(
            {
                'openstates_url': results['openstates_url'],
                'state': results['jurisdiction']['name'],
                'title': results['title'],
                'identifier': results['identifier'],
                'session': results['session'],
                'organization': results['from_organization']['name'],
                'first_action_date': results['first_action_date'],
                'latest_action_date': results['latest_action_date'],
                'sources': results['sources']
            }
        )
    results_df = pd.DataFrame.from_dict(formatted_results)
    results_df.to_csv("./openstates_api_results.csv")

if __name__ == "__main__":
    get_metadata()