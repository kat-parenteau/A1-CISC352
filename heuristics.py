# =============================
# Student Names: Kathryn Parenteau, Lauren Hunter, Charlotte Smith
# Group ID: Group 9
# Date: January 29th, 2026
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
    ''' A variable ordering heuristic that chooses the next variable to be assigned according to the Degree
    heuristic (DH). ord dh returns the variable that is involved in the largest number of constraints,
    which have other unassigned variables. '''

    # initialize tracking for the variable with the most constraints
    next_var_len = -1
    next_var = None

    # iterate through all unassigned variables
    for var in csp.get_all_unasgn_vars():
        con_count = 0
        # count constraints involving this variable with other unassigned variables
        for c in csp.get_cons_with_var(var):
            if c.get_n_unasgn() >= 2: # unassigned variables OTHER than the current var
                con_count += 1
        # update the next variable if this one has more constraints
        if con_count > next_var_len:
            next_var_len = con_count
            next_var = var
    
    return next_var



def ord_mrv(csp):
    ''' A variable ordering heuristic that chooses the next variable to be assigned according to 
    the Minimum-Remaining-Value (MRV) heuristic ord mrv returns the variable with the most constrained
    current domain (i.e., the variable with the fewest legal values remaining) '''

    # initialize the minimum domain size to infinity
    next_var_len = float('inf')
    # initialize the next variable to None
    next_var = None

    # iterate through all unassigned variables
    for var in csp.get_all_unasgn_vars():
        # check if the current variable's domain size is less than the current minimum
        if var.cur_domain_size() < next_var_len:
            # update the minimum domain size
            next_var_len = var.cur_domain_size()
            # update the next variable
            next_var = var
    
    # return the variable with the smallest domain size
    return next_var


