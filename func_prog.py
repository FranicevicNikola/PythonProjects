import collections
from functools import reduce
import itertools
from pprint import pprint
import concurrent.futures


Footballer = collections.namedtuple('Footballer', [
    'name',
    'position',
    'born',
    'BallondOr'])

Footballers = (
    Footballer(name='Messi', position='CF', born=1988, BallondOr=True),
    Footballer(name='Ronaldo', position='ST', born=1985, BallondOr=True),
    Footballer(name='Ibrahimović', position='ST', born=1982, BallondOr=False))


fs = tuple(filter(lambda x: x.BallondOr is True, Footballers))


names_and_ages = tuple(map(
    lambda x: {'name': x.name.upper(), 'age': 2020 - x.born},
    Footballers
))

pprint(names_and_ages)


total_age = reduce(lambda acc, val: acc + val['age'], names_and_ages, 0)
pprint(total_age)


def reducer(acc, val):
    acc[val.position].append(val.name)
    return acc


footballer_by_pos = reduce(reducer, Footballers, collections.defaultdict(list))
pprint(footballer_by_pos)

footballer_by_pos2 = {
    item[0]: list(item[1])
    for item in itertools.groupby(Footballers, lambda x: x.position)
}
pprint(footballer_by_pos2)


#  MULTIPROCESING
with concurrent.futures.ProcessPoolExecutor() as executor:
    result = executor.map()
