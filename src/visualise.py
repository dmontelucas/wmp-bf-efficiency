import matplotlib.pyplot as mplt

def plot_efficiency_hist(df):
    mplt.hist(df["efficiency"], bins=20)
    mplt.xlabel("Efficiency")
    mplt.ylabel("Frequency")
    mplt.title("WMP Blood-Feeding to Egg Efficiency")
    mplt.show()