import requests

def main():
   res = requests.get("http://data.fixer.io/api/latest")
   if res.status_code != 200:
      raise Exception("ERROR: API request unsuccessful")
   data = res.json()
   rate = data["rates"]["USD"]
   print("1 Euro is equal to %.3f USD" % rate)
   amount = input("Enter an amount in USD: ")
   amountEuros = float(amount) / float(rate)
   print("\nYou have %.2f Euros" % amountEuros)

if __name__ == "__main__":
   main()