import random
ions = ["Ammonium", "Hydroxide", "Nitrite", "Nitrate", "Ethanoate", "Hydrogencarbonate", "HydrogenSulfate", "Permanganate", "Dihydrogenphosphate", "Hydride", "Bromide", "Chloride", "Iodide", "Hypochlorite", "Chlorite", "Chlorate", "Perchlorate", "Carbonate", "Sulfite", "Sulfate", "Chromate", "Dichromate", "Oxide", "Sulfide", "Hydrogenphosphate", "Phosphate", "Nitride", "Nitrogen Dioxide", "Phosphoric Acid"]
formula = ["NH\u2084\u207A", "OH\u207B", "NO\u2083\u207B", "NO\u2084\u207B", "CH\u2083COO\u207B", "HCO\u2083\u207B", "HSO\u2084\u207B", "MNO\u2084\u207B", "H\u2082PO\u2084\u207B", "H\u207B", "Br\u207B", "Cl\u207B", "I\u207B", "ClO\u207B", "ClO\u2083\u207B", "ClO\u2083\u207B", "ClO\u2084\u207B", "CO\u2083\u207B\u207B", "SO\u2083\u207B\u207B", "SO\u2084\u207B\u207B", "CrO\u2084\u207B\u207B", "Cr\u2082O\u2087\u207B\u207B", "O\u207B\u207B", "S\u207B\u207B", "HPO\u2084\u207B\u207B", "PO\u2084\u207B\u207B\u207B", "N\u207B\u207B\u207B", "NO\u2082\u207A", "H\u2083PO\u2084"]
if len(ions) != len(formula):
    raise ValueError("error")


while True:
    index = random.randint(0, len(ions) - 1)
    selected_ion = ions[index]
    selected_formula = formula[index]
    input(f"Question: {selected_ion}\n")
    print(f"Answer: {selected_formula}\n")
    user_input = input("next ")
    if user_input == 'no':
        break