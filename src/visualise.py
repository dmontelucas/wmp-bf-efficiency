import matplotlib.pyplot as mplt
import numpy as np

def plot_efficiency_hist(
        df,
        column="eggs_per_ml",
        bins=20,
        ax=None,
):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    
    data = df[column].to_numpy()

    if not np.isinfinite(data).all():
        raise ValueError(f"Column '{column}' contains NaN or infinite values.")
    
    if ax is None:
        fig, ax = mplt.subplots()
    
    ax.hist(data, bins=bins)
    ax.set_xlabel("Eggs produced per ml of blood")
    ax.set_ylabel("Frequency")
    ax.set_title("WMP Blood-Feeding to Egg Production Efficiency")

    return ax
    
