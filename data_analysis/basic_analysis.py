import pandas as pd

def main_csv():
    df = pd.read_csv("csv_example1.csv", delimiter=";")
    print(df.iloc[0])  # pierwszy rekord
    # print(df["userLabel"])  # wyciągamy daną kolumnę

    # print(df[df["maxTilt"] > 100])
    df["tiltPercent"] = (df["electricalAntennaTilt"] - df["minTilt"])/(df["maxTilt"] - df["minTilt"]) * 100
    print(df["tiltPercent"])

    print(df[df["tiltPercent"] > 30]["userLabel"].values)
    print(df[df["tiltPercent"] > 30]["userLabel"].unique())  # bez powtarzających się wartości

    df["radioBand"] = df["userLabel"].str[-3:]

    print(df[["radioBand", "electricalAntennaTilt"]].groupby("radioBand").mean())


def main_txt():
    df = pd.read_fwf(
        "txt_example1.txt",
        skiprows=7,
        skipfooter=4,
        widths=[15, 35, 21, 32, 24],
        parse_dates=["Cell latest setup time"]
    )
    print(list(df))
    print(df.dtypes)
    print(df.describe())
    print(df.iloc[df["Cell latest setup time"].idxmax()]["Cell Name"])

if __name__ == "__main__":
    main_csv()
