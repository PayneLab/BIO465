import pandas as pd
import requests
import os


class BIO465:
    """
    BIO 465 is a container object that gets content associated with
    the BIO465 course at Brigham Young University
    """

    def __init__(self):
        self.dataframes = []
        self.homeworks = []
        self.labs = []
        self.lab_links = {'bacterial growth': "https://byu.box.com/shared/static/b0gn4i6v4h9a4owilv8of5m6x5tj82u7.xlsx"}

    """Queries box to get whatever link is within the lab_links parameter"""

    def get_lab(self, lab_string: str) -> pd.array:
        """
        :type lab_string: str
        """
        ErrorMessage = "Lab does not exist, returning empty pandas array."
        if not isinstance(lab_string, str):
            print(ErrorMessage)
            return pd.array([])
        lab_string = lab_string.lower()
        if lab_string not in self.lab_links.keys():
            print(ErrorMessage)
            return pd.array([])

        lab_link = self.lab_links[lab_string]
        response = requests.get(lab_link, allow_redirects=True, stream=True)  # query box to get the file
        xl = "lab.xlsx"
        with open(xl, "wb") as xl_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    xl_file.write(chunk)

        df = pd.read_excel(open(xl, 'rb'))
        os.remove('./' + xl)
        if lab_string == 'bacterial growth':
            df = df.drop(columns=["Min_MSGF", "Peptides", "Ref1", "Ref2", "Ref3", "Ref4", "Spectra"])
            df = df.set_index(["Protein"])
            df = df.transpose()
            df = df.reset_index()
            temp_cols = df["index"].str.split('_', n=1, expand=True)
            plate_type = temp_cols[0]
            time_plate = temp_cols[1].str.split('.', n=1, expand=True)
            df = df.assign(oxidation=plate_type, time=time_plate[0], plate=time_plate[1])
            df = df.set_index(["experimental condition", "time point", "replicate"])
            df = df.sort_index()
            df = df.transpose()
        return df


if __name__ == "__main__":
    b = BIO465()
    df_oxidation = [col.split('_')[0] for col in df if col.startswith("O2") or col.startswith("An")]
