def calc_efficiency(df):
    df["efficiency"] = df["egg_output_total"] / df["blood_input_ml"]
    df["eggs_per_hour"] = df["egg_output_total"] / df["time_hours"]
    return df