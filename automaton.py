import random
from AutomataTheory import *

class WordGenerator:

    def __init__(self, regex) -> None:
        if not regex:
            raise ValueError("Empty Regular Expression")
        self.automaton = self.generate_automaton(regex)
        self.transition_list = self.build_transition_list()
        pass

    def generate_automaton(self, regex):
        nfaObj = NFAfromRegex(regex)
        nfa = nfaObj.getNFA()
        dfaObj = DFAfromNFA(nfa)
        dfa = dfaObj.getDFA()
        minDFA = dfaObj.getMinimisedDFA()
        return minDFA


    def build_transition_list(self):
        transitions = {}
        for state in self.automaton.states:
            transitions[state] = [None] if state in self.automaton.finalstates else []
        for fromstate, tostates in list(self.automaton.transitions.items()):
                for state in tostates:
                    for char in tostates[state]:
                        transitions[fromstate].append({state: char})
        return transitions

    def generate_word(self, decision_list, word="", state=0):

        if state in self.automaton.finalstates and decision_list[state] is None:
            return word

        next_state = list(decision_list[state].keys())[0]
        word += list(decision_list[state].values())[0]

        return self.generate_word(decision_list, word, next_state)


    def build_decision_list(self, choice_fun = random.choice):
        decisions = {}
        for key, value in self.transition_list.items():
            decisions[key] = None if len(value) == 0 else choice_fun(value)
        return decisions

