# Поиск в ширину
# Breadth-First-Search

from collections import deque

graph = dict()
graph['me'] = ['Al', 'Mab', 'Blo']
graph['Al'] = []
graph['Blo'] = ['Lee', 'Jack']
graph['Mab'] = ['Lee', 'Loony']
graph['Loony'] = ['Braub', 'Cloa', "Ased", 'Morm']


def person_is_seller(person):
    return person[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph.get(name, [])
    searched = list()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a Mango seller!')
                return True
            else:
                search_queue += graph.get(person, [])
                searched.append(person)
    return False


search('me')
