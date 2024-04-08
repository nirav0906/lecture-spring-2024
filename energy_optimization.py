from pulp import LpProblem, LpVariable, LpMinimize, lpSum

def optimize_energy_allocation(Pwind, Ppv, Load):
    """
    Optimize energy allocation to minimize cost.
    """
    time = list(range(24))

    # Create a linear programming problem
    prob = LpProblem("Cost Optimization", LpMinimize)

    # Define variables
    x_wind = LpVariable.dicts("Wind", time, lowBound=0, cat="Continuous")
    x_pv = LpVariable.dicts("PV", time, lowBound=0, cat="Continuous")
    x_fuel_cell = LpVariable.dicts("FuelCell", time, lowBound=0, cat="Continuous")

    # Define objective function (minimize cost)
    prob += lpSum(0.4 * x_wind[i] + 0.35 * x_pv[i] + 0.9 * x_fuel_cell[i] for i in time)

    # Constraints
    for i in time:
        prob += x_wind[i] + x_pv[i] + x_fuel_cell[i] >= Load[i]
        prob += x_wind[i] <= Pwind[i]
        prob += x_pv[i] <= Ppv[i]

    # Solve the problem
    prob.solve()

    # Extract optimal energy allocation
    optimal_allocation = {}
    for i in time:
        optimal_allocation[i] = {
            "Wind": x_wind[i].value(),
            "PV": x_pv[i].value(),
            "FuelCell": x_fuel_cell[i].value()
        }

    return optimal_allocation
