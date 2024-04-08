from energy_optimization import optimize_energy_allocation

time = list(range(24))
Pwind = [130, 150, 140, 160, 100, 120, 150, 180, 170, 160, 120, 130, 150, 176, 185, 120, 130, 140, 170, 190, 120, 170, 130, 150]
Ppv = [0, 0, 0, 0, 0, 5, 10, 30, 60, 100, 130, 140, 150, 140, 130, 100, 60, 30, 10, 5, 0, 0, 0, 0]
Load = [160, 140, 150, 120, 110, 100, 170, 180, 200, 220, 230, 240, 240, 230, 220, 210, 210, 220, 230, 240, 250, 200, 190, 180]

def test_energy_allocation():
    optimal_result = optimize_energy_allocation(Pwind, Ppv, Load)
    for hour, allocation in optimal_result.items():
        print(f"Hour {hour}: Wind = {allocation['Wind']:} Wh, PV = {allocation['PV']:} Wh, Fuel Cell = {allocation['FuelCell']:} Wh")
        assert isinstance(optimal_result, (int, float))
        assert optimal_result > 0