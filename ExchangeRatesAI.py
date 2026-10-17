
import csv


class ExchangeRates:
    def __init__(self, filename):
        self.filename = filename
        self.usd_cad_rate = self.read_latest_rate()

    def read_latest_rate(self):
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            latest_rate = None

            for row in reader:
                rate = row.get("FXAUSDCAD")

                if rate and rate.strip():
                    latest_rate = float(rate)

        if latest_rate is None:
            raise ValueError("No USD/CAD exchange rate found.")

        return latest_rate

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in ("USD", "CAD"):
            raise ValueError("Currency must be USD or CAD.")

        if to_currency not in ("USD", "CAD"):
            raise ValueError("Currency must be USD or CAD.")

        if from_currency == to_currency:
            return amount

        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_cad_rate

        if from_currency == "CAD" and to_currency == "USD":
            return amount / self.usd_cad_rate


# Main program
rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

print(f"Latest USD/CAD rate: {rates.usd_cad_rate}")

amount = float(input("Enter the amount to convert: "))
from_currency = input("Convert from (USD or CAD): ").strip().upper()
to_currency = input("Convert to (USD or CAD): ").strip().upper()

try:
    result = rates.convert(amount, from_currency, to_currency)
    print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

except ValueError as error:
    print("Error:", error)
