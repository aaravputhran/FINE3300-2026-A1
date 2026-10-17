'''
ExchangeRates.py
FINE 3300 - Assignment #1, Part 1

ExchangeRates class that reads the Bank of Canada annual exchange
rate file and converts an amount between USD and CAD using the
latest USD/CAD rate (the last row of the file).
'''

class ExchangeRates:
    def __init__(self, file_name="BankOfCanadaExchangeRate.2026.csv"):
        # Private members (double underscore), as in the Bond class
        self.__file_name = file_name
        self.__usd_cad = 0.0

        # Read the file and store each row as a list of values
        rows = []
        file = open(self.__file_name, "r", encoding="utf-8-sig")
        for line in file:
            rows.append(line.strip().split(","))
        file.close()

        # The first row holds the column names; loop through it to find USD/CAD
        header = rows[0]
        usd_column = 0
        for i in range(len(header)):
            if header[i] == "FXAUSDCAD":
                usd_column = i

        # The last row holds the latest rate (CAD per 1 USD)
        latest_row = rows[-1]
        self.__date = latest_row[0]
        self.__usd_cad = float(latest_row[usd_column])

    def get_rate(self):
        # Public method to see the rate being used
        return self.__usd_cad

    def get_date(self):
        # Public method to see the date of the rate being used
        return self.__date

    def convert(self, amount, from_currency, to_currency):
        # USD -> CAD: multiply by the rate
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.__usd_cad
        # CAD -> USD: divide by the rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.__usd_cad
        # Same currency: no conversion needed
        else:
            return amount


if __name__ == "__main__":
    # Build the full path to the CSV so it is found in the same folder as this script
    import os
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "BankOfCanadaExchangeRate.2026.csv")

    rates = ExchangeRates(file_path)
    print("Latest USD/CAD rate ({}): {}".format(rates.get_date(), rates.get_rate()))

    # Prompt the user (inputs are assumed to be valid)
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the 'from' currency (USD or CAD): ").upper()
    to_currency = input("Enter the 'to' currency (USD or CAD): ").upper()

    converted = rates.convert(amount, from_currency, to_currency)

    # Output rounded to the nearest penny with dollar signs and currency codes
    print("${:,.2f} {} = ${:,.2f} {}".format(amount, from_currency, converted, to_currency))