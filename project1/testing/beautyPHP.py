import re
import requests
from bs4 import BeautifulSoup

def update_php(url):
    # Send a GET request to the URL
    response = requests.get(url)

<<<<<<< HEAD
print(result_php)
=======
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Define the version string pattern
        version_pattern = re.compile(r'PHP 8\.2\.\d+')

        # Find all occurrences of the version string pattern in the page
        occurrences = soup.body(text=version_pattern.search)

        # If there are occurrences, return the first one
        if occurrences:
            latest_version = occurrences[0].strip()
            return latest_version
        else:
            return "No version strings matching 'PHP 8.2.x' found on the PHP official website."
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"

# Example usage:
url = "https://www.php.net/"
result_php = update_php(url)
print(result_php)
>>>>>>> d582d6c1a458db795853f1467476bb0bc78c81b8
