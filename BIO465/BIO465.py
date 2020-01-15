import pandas


class BIO465:
    """
    BIO 465 is a container object that gets content associated with
    the BIO465 course at Brigham Young University
    """

    def __init__(self):
        self.dataframes = []
        self.homeworks = []
        self.labs = []
        self.lab_links = {
            0: "homework1.com"
        }

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
        # read the file
        # use pandas to convert to data frame
        # return data frame
        pass
