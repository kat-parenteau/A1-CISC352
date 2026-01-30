# =============================
# Student Names: Kathryn Parenteau, Lauren Hunter, Charlotte Smith
# Group ID: Group 9
# Date: January 29th, 2026
# =============================
# CISC 352
# cagey_csp.py
# desc:
#

import itertools

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all Variables in the given csp. If you are returning an entire grid's worth of Variables
they should be arranged linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional Variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 0.5/3 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
| n^2-n | n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '%' for modular addition
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import CSP, Variable, Constraint

def binary_ne_grid(cagey_grid):
    ''' A model of a Cagey grid (without cage constraints) built using only binary not-equal constraints for
    both the row and column constraints '''

    # (n, [cages])

    # n - is the size of the grid,
    # cages - is a list of tuples defining all cage constraints on a given grid.

    # Binary not equal: the values in each row and column must be different
    # Goal: turn a cagey_grid into a csp (reminder: some operations are ? (unknown))

    # An example of a 3x3 puzzle would be defined as:
    # (3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

    # Variable: a variable, with a name, and a domain (set of variables it can be)
    # Constraint: a name, and scope. Satisfying tuples are added later (a set of satisfying tuples ((i.e., each tuple specifies a value 
    #    for each variable in the scope such that this sequence of values satisfies the constraints))
    # CSP: adding all vars into a csp. A name, and a list of vars (optional). Constraints must be added later

    # For this cagey, the variables should be all of the squares in the grid.

    # Should the scope be the size of the cage? (n, the dimension)

    # Loop through all the squares and create vars for them
    # [(3,[(1,1), (2,1)],"+"), (1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")]

    n = list(cagey_grid)[0]
    variables = []

    # Loop through all squares and create a variable for each
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            domain = list(range(1, n + 1))
            var = Variable(f"Cell({row},{col})", domain)
            variables.append(var)

    # Create a csp of the variables
    csp = CSP("binary_ne", variables)

    # Define satisfactory tuples (rows and cols can't equal each other)
    sat_tuples = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b:
                sat_tuples.append((a, b))

    # Column constraints
    for col in range(n):
        for row1 in range(n):
            for row2 in range(row1 + 1, n):
                var1 = variables[row1 * n + col]
                var2 = variables[row2 * n + col]
                con = Constraint(f"Column({col},[{row1},{row2}])", [var1, var2])
                # Calculate satisfying tuples
                con.add_satisfying_tuples(sat_tuples)
                csp.add_constraint(con)

    # Row constraints
    for row in range(n):
        for col1 in range(n):
            for col2 in range(col1 + 1, n):
                var1 = variables[row * n + col1]
                var2 = variables[row * n + col2]
                con = Constraint(f"Row({row},[{col1},{col2}])", [var1, var2])
                # Calculate satisfying tuples
                con.add_satisfying_tuples(sat_tuples)
                csp.add_constraint(con)
    

    # Retrun csp, vars
    return csp, variables



def nary_ad_grid(cagey_grid):
    ''' A model of a Cagey grid (without cage constraints) built using only n-ary all-different constraints
    for both the row and column constraints. '''

    n = list(cagey_grid)[0]
    variables = []

    # Loop through all squares and create a variable for each
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            domain = list(range(1, n + 1))
            var = Variable(f"Cell({row},{col})", domain)
            variables.append(var)

    # Define csp
    csp = CSP("nary_ad", variables)

    # All possible permutations
    sat_tuples = list(itertools.permutations(range(1, n + 1), n))

    # Column constraints
    for col in range(n):
        col_vars = []
        # Loop through rows and get column variables
        for row in range(n):
            col_vars.append(variables[row*n + col])
        # Create consdtraint
        con = Constraint(f"Row({row}), Col({col})", col_vars)
        # Calculate satisfying tuples
        con.add_satisfying_tuples(sat_tuples)
        csp.add_constraint(con)

    # Row constraints
    for row in range(n):
        row_vars = []
        # Loop through columns and get row variables
        for col in range(n):
            row_vars.append(variables[row*n + col])
        # Create constraint
        con = Constraint(f"Row({row}), Col({col})", row_vars)
        # Calculate satisfying tuples
        con.add_satisfying_tuples(sat_tuples)
        csp.add_constraint(con)

    # Return csp and vars
    return csp, variables


def cagey_csp_model(cagey_grid):
    ''' A model built using your choice of (1) binary not-equal, or (2) n-ary all-different constraints for the
    grid, together with (3) cage constraints. That is, you will choose one of the previous two grid models
    and expand it to include cage constraints '''
    def cagey_csp_model(cagey_grid):
    # Build base grid CSP (binary ne)
    csp, board_vars = binary_ne_grid(cagey_grid)
    n, cages = cagey_grid
    all_vars = list(board_vars)
    domain = ['+', '-', '*', '/', '%']

    # Go through each cage
    for i, (target, cells, op_char) in enumerate(cages):
        # Find cell variables for this cage
        cage_cell_vars = [board_vars[(row - 1) * n + (col - 1)] for (row, col) in cells]

        # Create operator variable
        parts = []
        for (row, col) in cells:
            parts.append('Var-Cell(%d,%d)' % (row, col))
        
        cell_parts = ', '.join(parts)
        op_name = 'Cage_op(%s:%s:[%s])' % (target, op_char, cell_parts)

        if op_char == '?':
            op_var = Variable(op_name, domain)
        else:
            op_var = Variable(op_name, [op_char])

        csp.add_var(op_var)
        all_vars.append(op_var)

        # Cage constraint scope = cell variables + operator variable
        scope = cage_cell_vars + [op_var]
        con = Constraint('Cage_%d' % i, scope)

        # Domains don't change between cells
        cell_domains = [range(1, n + 1)] * len(cage_cell_vars)
        sat_tuples = []
        
        # Try all value assignments
        for vals in itertools.product(*cell_domains):
            for op_val in op_var.domain():
                found = False
                for permutation in itertools.permutations(vals):
                    if op_val == '+':
                        result = sum(permutation)
                    elif op_val == '*':
                        result = 1
                        for v in permutation:
                            result *= v
                    elif op_val == '-':
                        result = permutation[0]
                        for v in permutation[1:]:
                            result -= v
                    elif op_val == '/':
                        result = permutation[0]
                        ok = True
                        for v in permutation[1:]:
                            if v == 0 or (result % v) != 0:
                                ok = False
                                break
                            result //= v
                        if not ok:
                            result = None
                    elif op_val == '%':
                        result = sum(permutation) % n
                    else:
                        result = None

                    if result is not None and result == target:
                        sat_tuples.append(tuple(list(vals) + [op_val]))
                        found = True
                        break
                if found:
                    break
        
        # Finalize constraint
        con.add_satisfying_tuples(sat_tuples)
        csp.add_constraint(con)
    
    return csp, all_vars
