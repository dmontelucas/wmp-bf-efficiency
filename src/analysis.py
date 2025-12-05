import statsmodels.api as sm

def run_regression(df):
    X = df[["blood_input_ml", "temperature", "humidity_pct"]]
    y = df["egg_output_total"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    return model