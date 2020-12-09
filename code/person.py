import re
import numpy as np
import pandas as pd
import logging


class Person:
    """Person representation"""
    def __init__(self, name: str, surname: str, email: str, address: str, number: str, gender: str = "m"):
        """
        :param name: name
        :param email: email
        :param gender: gender
        """
        self.name = name
        self.surname = surname
        self.email = email
        self.gender = gender
        self.address = address
        self.number = number


def get_person_from_name(people_list: list, name: str):
    """
    Given a name get the corresponding Person class

    :param people_list: people list
    :param name: string with one or more person name. It is read from Excel file.
    """
    final_list = []
    name_list = re.split(', |,', name.rstrip())
    for name in name_list:
        condition = [p for p in people_list if name == p.name + p.surname]
        if len(condition) == 0:
            logging.warning("Cannot avoid match with %s. This participant is not found, check "
                            "the spelling." % name)
        else:
            final_list.extend(condition)
    return final_list


def get_conditions(people_dft: pd.DataFrame):
    """
    Get people list and invalid match list
    :param people_dft: dataframe with name, email, gender and condition for each participant
    """
    people_list = []
    conditions_list = {}
    for i, name in enumerate(people_dft.index):
        new_person = Person(name, people_dft.iloc[i]["cognome"], people_dft.iloc[i]["email"],
                            people_dft.iloc[i]["indirizzo"], people_dft.iloc[i]["telefono"], people_dft.iloc[i]["gender"])
        people_list.append(new_person)
        if people_dft.iloc[i]["match non validi"] is not np.nan:
            conditions_list[new_person] = people_dft.iloc[i]["match non validi"]

    invalid_match = {k: get_person_from_name(people_list, v) for k, v in conditions_list.items() if not pd.isnull(v)}
    return people_list, invalid_match
