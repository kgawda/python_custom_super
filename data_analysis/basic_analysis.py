import pandas as pd

def main():
    df = pd.read_csv("csv_example1.csv", delimiter=";")
    print(df.iloc[0])  # pierwszy rekord
    # print(df["userLabel"])  # wyciągamy daną kolumnę

    # print(df[df["maxTilt"] > 100])
    df["tiltPercent"] = (df["electricalAntennaTilt"] - df["minTilt"])/(df["maxTilt"] - df["minTilt"]) * 100
    print(df["tiltPercent"])

    print(df[df["tiltPercent"] > 30]["userLabel"].values)
    print(df[df["tiltPercent"] > 30]["userLabel"].unique())  # bez powtarzających się wartości


if __name__ == "__main__":
    main()
