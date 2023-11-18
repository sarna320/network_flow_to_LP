from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")

# For s
sA = solver.NumVar(0, 10, "sA")
sB = solver.NumVar(0, 13, "sB")
sC = solver.NumVar(0, 22, "sC")

# For A
AD = solver.NumVar(0, 8, "AD")
AE = solver.NumVar(0, 10, "ED")

# For B
BD = solver.NumVar(0, 10, "BD")
BE = solver.NumVar(0, 13, "BE")

# For C
CD = solver.NumVar(0, 10, "CD")
CE = solver.NumVar(0, 8, "CD")

# For D
DF = solver.NumVar(0, 16, "DF")
DG = solver.NumVar(0, 6, "DG")
DH = solver.NumVar(0, 10, "DH")
DE = solver.NumVar(0, 20, "DE")

# For E
EF = solver.NumVar(0, 7, "EF")
EG = solver.NumVar(0, 4, "EG")
EH = solver.NumVar(0, 2, "EH")

# For F
Ft = solver.NumVar(0, 15, "Ft")

# For G
Gt = solver.NumVar(0, 10, "Gt")

# For H
Ht = solver.NumVar(0, 10, "Ht")

# print("Number of variables =", solver.NumVariables())

# constraints
solver.Add(sA + sB + sC == 35)
solver.Add(AD + AE - sA == 0)
solver.Add(BD + BE - sB == 0)
solver.Add(CD + CE - sC == 0)
solver.Add(DF + DG + DH + DE - AD - BD - CD == 0)
solver.Add(EF + EG + EH - DE - AE - BE - CE == 0)
solver.Add(Ft - DF - EF == 0)
solver.Add(Gt - DG - EG == 0)
solver.Add(Ht - DH - EH == 0)

# print("Number of constraints =", solver.NumConstraints())

# Objective function:
solver.Minimize(
    3 * AD
    + 6 * AE
    + 6 * BD
    + 3 * BE
    + 4 * CD
    + 5 * CE
    + 5 * DF
    + 7 * DG
    + 3 * DH
    + 2 * DE
    + 5 * EF
    + 4 * EG
    + 2 * EH
)

print(f"Solving with {solver.SolverVersion()}")
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Solution:")
    print(f"Objective value = {solver.Objective().Value():0.1f}")
    print(f"sA = {sA.solution_value():0.1f}")
    print(f"sB = {sB.solution_value():0.1f}")
    print(f"sB = {sB.solution_value():0.1f}")
    print(f"AD = {AD.solution_value():0.1f}")
    print(f"AE = {AE.solution_value():0.1f}")
    print(f"BD = {BD.solution_value():0.1f}")
    print(f"BE = {BE.solution_value():0.1f}")
    print(f"CD = {CD.solution_value():0.1f}")
    print(f"CE = {CE.solution_value():0.1f}")
    print(f"DF = {DF.solution_value():0.1f}")
    print(f"DG = {DG.solution_value():0.1f}")
    print(f"DH = {DH.solution_value():0.1f}")
    print(f"DE = {DE.solution_value():0.1f}")
    print(f"EF = {EF.solution_value():0.1f}")
    print(f"EG = {EG.solution_value():0.1f}")
    print(f"EH = {EH.solution_value():0.1f}")
    print(f"Ft = {sA.solution_value():0.1f}")
    print(f"Gt = {sA.solution_value():0.1f}")
    print(f"Ht = {sA.solution_value():0.1f}")

else:
    print("The problem does not have an optimal solution.")
