import pandas as pd
import requests


class BIO465:
    """
    BIO 465 is a container object that gets content associated with
    the BIO465 course at Brigham Young University
    """

    def __init__(self):
        self.dataframes = []
        self.homeworks = []
        self.labs = []
        self.lab_links = ["https://byu.box.com/shared/static/b0gn4i6v4h9a4owilv8of5m6x5tj82u7.xlsx"]

    """ retrieves a list of Lab objects from the instantiated class """

    def get_labs(self) -> list:
        return self.labs

    """ retrieves a list of Homework objects from the instantiated class """
    def get_homeworks(self) -> list:
        return self.homeworks

    """ retrieves a list of pandas data frame objects from the instantiated class """

    def get_dataframes(self) -> list:
        return self.dataframes

    """Queries box to get whatever link is within the lab_links parameter"""

    def get_lab(self, lab_number: int) -> pandas.array:
        # query box to get the file
        lab_link = self.lab_links[lab_number]
        response = requests.get(lab_link, allow_redirects=True, stream=True)
        xl = "lab1.xlsx"

        with open(xl, "wb") as xl_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    xl_file.write(chunk)

        df = pd.read_excel(open('tmp.xlsx', 'rb'))
        print(df)

        with requests.Session() as session:  # Use a session object to save cookies

            # Send initial GET request and parse the request token out of the response
            get_response = session.get(lab_link)
            #soup = bs4.BeautifulSoup(get_response.text, "html.parser")
            #token_tag = soup.find(id="request_token")
            #token = token_tag.get("value")
        response.raise_for_status()  # Raises a requests.HTTPError if the response code was unsuccessful
        # read the file into file object
        # use pandas to convert to data frame
        # return data frame
        pass
