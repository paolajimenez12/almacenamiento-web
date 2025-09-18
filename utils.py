import pandas as pd

def load_example_data():
    data = {
        "Sistema": ["A", "B", "C", "D"],
        "Capacidad (GB)": [120, 300, 500, 80]
    }
    return pd.DataFrame(data)

def calculate_metrics(df):
    total = df["Capacidad (GB)"].sum()
    mean = df["Capacidad (GB)"].mean()
    max_val = df["Capacidad (GB)"].max()
    return {"total": total, "mean": mean, "max": max_val}

def simulate_expansion(df, growth_percent, years):
    total = df["Capacidad (GB)"].sum()
    rows = []
    for year in range(1, years + 1):
        total *= (1 + growth_percent / 100)
        rows.append({"Año": year, "Capacidad proyectada": total})
    return pd.DataFrame(rows)
