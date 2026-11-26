
def protein_energy_temp():
  temp_k = float(input("Enter temperature in Kelvin (T): "))
  enthalpy = float(input("Enter enthalpy change ΔH (kJ/mol): "))
  entropy = float(input("Enter entropy change ΔS (kJ/mol·K): "))

  def calculate_free_energy(enthalpy, entropy):
    return enthalpy - (temp_k * entropy)

  delta_g = calculate_free_energy(enthalpy, entropy)
  stability = "stable" if delta_g < 0 else "unstable"

  print(f"\nΔG = {delta_g:.2f} kJ/mol")
  return stability


result = protein_energy_temp()
print(f"Protein stability: {result}")


# import random
# def protein_energy_temp(T=298):
#     def calculate_free_energy(enthalpy, entropy):
#         return enthalpy - T * entropy
#
#     dH = random.uniform(-100, 100)        # kJ/mol
#     dS = random.uniform(-0.2, 0.2)        # kJ/(mol*K)
#     dG = calculate_free_energy(dH, dS)
#     print(f" dH={dH:.2f}, dS={dS:.4f}, dG={dG:.2f} kJ/mol")
#     return "stable" if dG < 0 else "not stable"
#
# print("   ", protein_energy_temp())