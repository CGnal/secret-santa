from random import choice
import time
import os
from typing import List, Dict, Optional
from santacode.person import Person


TIMEOUT = 0.2


class SolvingError(Exception):
    pass


def solver(people: List[Person], invalid_match: Optional[Dict[Person, Person]] = None):
    """
    Solver
    :param people: list of all partecipant
    :param invalid_match: list with invalid matches
    """
    if invalid_match is None:
        invalid_match = {}
    start_time = time.time()
    while True:
        receiver = people.copy()
        matches = dict()
        for p in people:
            valid = [r for r in receiver if r != p and r not in invalid_match.get(p, ())]
            if len(valid) == 0:
                break
            rec = choice(valid)
            matches[p] = rec
            receiver.remove(rec)
        if len(matches) == len(people):
            return matches
        elif start_time + TIMEOUT < time.time():
            raise SolvingError('Could not solve.')


def saver(solved_dict: Dict[Person, Person]):
    """
    Save matches
    :param solved_dict: dict with match
    """
    if not os.path.exists('Backup'):
        os.makedirs('Backup')
    for santa, rec in solved_dict.items():
        with open('Backup/Assignment for {}.txt'.format(santa.name), 'w') as f:
            f.write('Buy a present for {}.\n'.format(rec.name))
