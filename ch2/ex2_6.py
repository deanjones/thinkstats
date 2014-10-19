from ch1.ex1_3 import *

preg = load_pregnancies()
all_first = get_first_babies(preg)
all_others = get_others(preg)

EARLY = 37
LATE = 41

def get_early(all):
    return all[all['prglength'] <= EARLY]

def get_on_time(all):
    return all[(all['prglength']) > EARLY & (all['prglength'] < LATE)]

def get_late(all):
    return all[all['prglength'] >= LATE]

def get_relative_risk(first, others):
    prob_first = len(first) / float(len(all_first))
    prob_others = len(others) / float(len(all_others))
    return prob_first / prob_others

if __name__ == '__main__':
    early_first = get_early(all_first)
    early_others = get_early(all_others)
    on_time_first = get_on_time(all_first)
    on_time_others = get_on_time(all_others)
    late_first = get_late(all_first)
    late_others = get_late(all_others)

    relative_risk_early = get_relative_risk(early_first, early_others)
    relative_risk_on_time = get_relative_risk(on_time_first, on_time_others)
    relative_risk_late = get_relative_risk(late_first, late_others)

    print 'relative risk early =', relative_risk_early
    print 'relative risk on time =', relative_risk_on_time
    print 'relative risk late =', relative_risk_late

