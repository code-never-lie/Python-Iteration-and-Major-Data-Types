'''
Created on April 5, 2022

@author: Ahmadraza161
'''
import prompt
import goody
from collections import defaultdict
from prompt import for_bool
# Use these global variables to index the list associated with each name in thedictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man'm1', and
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple,but the
# preference list it contains is mutated, which is not allowed in a named tuple.
match = 0  # Index 0 of list associate with name is match (str)
prefs = 1  # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file: open) -> {str: [str, [str]]}:
    chain_dict = defaultdict(list)

    for text in (open_file):
        text = text.rstrip().split(';')
    chain_dict[text[0]].append(None)
    chain_dict[text[0]].append(text[1:])
    open_file.close()
    return dict(chain_dict)


def dict_as_str(d: {str: [str, [str]]}, key: callable = None, reverse:
                bool = False) -> str:

    step_list = ''
    for value in sorted(d.keys(), key=key, reverse=reverse):
        step_list = step_list + ' ' + value + " -> " + str(d[value]) + "\n"

    return step_list


def who_prefer(order: [str], p1: str, p2: str) -> str:
    return order[min(order.index(p1), order.index(p2))]


def extract_matches(men: {str: [str, [str]]}) -> {(str, str)}:
    return {(a, men[a][0]) for a in men}


def make_match(men: {str: [str, [str]]}, women: {str: [str, [str]]}, trace: bool = False) -> {(str, str)}:

    def formula():
        unmatched = set()
    change_men = men.copy()
    for a, b in change_men.items():
        if b[0] is None:
            unmatched.add(a)
    if trace:
        print('\nWomen Preferences(unchanging)\n', dict_as_str(women), sep='')
        print('Men Preferences (current)\n', dict_as_str(men), sep='')
        print('unmatched men =', unmatched)
    while len(unmatched) > 0:
        current = set()
    preference = ''
    current = unmatched.pop()
    preference = change_men[current][1][0]

    if women[preference][0] is None:
        if trace:
            print('\n{} proposes to {}, who is unmatched and acceptsthe proposal\n'.format(
                current, preference))
            change_men[current][0] = preference
            women[preference][0] = current
            change_men[current][1].pop(
                (change_men[current][1].index(preference)))
        else:
            winner = (who_prefer(women[preference] [1], women[preference][0], current))
            if winner == current:
                if trace:
                    print('\n{} proposes to {}, who is matched and accepts the proposal, rejecting match with {} '.format(
                        current, preference, women[preference][0]))
    unmatched.add(women[preference][0])
    change_men[women[preference][0]][0] = None
    women[preference][0] = winner
    change_men[winner][0] = preference
    change_men[winner][1].pop(change_men[winner][1].index(preference))
    if trace:
            print('\n{} proposes to {}, who is matched andrejects the proposal(likes current match better)'.format( current, preference))
            unmatched.add(current)
            change_men[current][1].pop(
                change_men[current][1].index(preference))
    if trace:
        if len(unmatched) > 0:
            print('\nMen Preferences(current)\n', dict_as_str(men), sep='')
            print('unmatched men =', unmatched)
    else:
        print('algorithm halted: ', end='')
    return extract_matches(change_men)

    return formula()


if __name__ == '__main__':
    # Write script here
    file = goody.safe_open('Type some file name storing preferences of men  ','r','Illegal file name')
    second_file = goody.safe_open('Type some file name storing preferences of  women ','r','Illegal file name')
    men_pref = read_match_preferences(file)
    women_pref = read_match_preferences(second_file)
    print('\nMen Preferences\n', dict_as_str(men_pref), sep='')
    print('Women Preferences\n', dict_as_str(women_pref), sep='')
    Trace = for_bool('Trace this Algorithm', True)
    if Trace is False:
        print()
    print('matches =', make_match(men_pref, women_pref, Trace))
    print()
    # For running batch self-tests
    #import driver
    #driver.default_file_name = "bsc2.txt"
    # driver.default_show_traceback = True
    # driver.default_show_exception = True
