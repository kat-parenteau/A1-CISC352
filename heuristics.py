# =============================
# Student Names:
# Group ID:
# Date:
# =============================
# CISC 352
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   the propagators

1. ord_dh (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned 
      according to the Degree heuristic

2. ord_mv (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned 
      according to the Minimum-Remaining-Value heuristic


var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    Variables and constraints of the problem. The assigned Variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' A variable ordering heuristic that chooses the next variable to be assigned according to the MinimumRemaining-Value (MRV) heuristic. ord mrv returns the variable with the most constrained current
    domain (i.e., the variable with the fewest legal values remaining). '''
    next_var_len = float('inf')
    next_var = None

    for var in csp.get_unasgn_vars:
        domains = var.cur_domain()
        if len(domains) < next_var_len:
            next_var = var
            next_var_len = len(domains)
    
    return next_var

    # IMPLEMENT
    #pass

def ord_mrv(csp):
    ''' A variable ordering heuristic that chooses the next variable to be assigned according to the Degree
    heuristic (DH). ord dh returns the variable that is involved in the largest number of constraints,
    which have other unassigned variables. '''
    # NOT COMPLETED 
    next_var_len = 0
    next_var = None

    for var in csp:
        c = csp.get_cons_with_var(var)
        if len(c) > next_var_len:
            next_var_len = len(c)
            next_var = var
    return next_var

    # IMPLEMENT
    pass
