def calc_efficiency(df):
    required = {egg_output_total", "blood_input_ml", "time_hours"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if not inplace:
        df = df.copy()
    
    eggs = df["egg_output_total"]
    blood = df["blood_input_ml"]
    time = df["time_hours"]

    if (blood <= 0).any():
        raise ValueError("blood_input_ml must be greater than zero.")
    if (time <= 0).any():
        raise ValueError("time_hours must be greater than zero.")
    if (eggs < 0).any():
        raise ValueError("egg_output_total must be non-negative.")
    
    df["eggs_per_ml"] = eggs / blood
    df[eggs_per_hour"] = eggs / time
       
    df.attrs.setdefault("derived_features", {}).update({
        "eggs_per_ml": "egg_output_total / blood_input_ml",
        "eggs_per_hour": "egg_output_total / time_hours",
    })
    return df
