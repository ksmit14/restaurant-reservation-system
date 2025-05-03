import datetime
import uuid

# Sample tables with capacity
TABLES = [
    {"id": 1, "capacity": 2, "reserved": False},
    {"id": 2, "capacity": 2, "reserved": False},
    {"id": 3, "capacity": 4, "reserved": False},
    {"id": 4, "capacity": 4, "reserved": False},
    {"id": 5, "capacity": 6, "reserved": False},
    {"id": 6, "capacity": 8, "reserved": False},
]

REGISTERED_USERS = []
RESERVATIONS = []

HIGH_TRAFFIC_DAYS = ["07-04", "12-25", "12-31"]  # MM-DD format


# --------- User Class -------------
class User:
    def __init__(self, name, phone, email, is_registered=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.is_registered = is_registered
        self.mailing_address = ""
        self.billing_address = ""
        self.preferred_diner_no = str(uuid.uuid4())[:8]
        self.points = 0
        self.payment_method = ""

    def register(self):
        self.mailing_address = input("Enter mailing address: ")
        same = input("Is billing address the same? (yes/no): ").lower()
        if same == "no":
            self.billing_address = input("Enter billing address: ")
        else:
            self.billing_address = self.mailing_address
        self.payment_method = input("Preferred payment method (cash/credit/check): ")
        self.is_registered = True
        REGISTERED_USERS.append(self)
        print(f"Registration complete! Your Diner # is {self.preferred_diner_no}")


# --------- Reservation Logic ----------
def find_tables_for_guests(num_guests):
    available = [t for t in TABLES if not t["reserved"]]
    available.sort(key=lambda x: x["capacity"])

    # Exact or nearest single table
    for table in available:
        if table["capacity"] >= num_guests:
            return [table]

    # Combine tables
    combinations = []
    for i in range(len(available)):
        temp = []
        total = 0
        for j in range(i, len(available)):
            temp.append(available[j])
            total += available[j]["capacity"]
            if total >= num_guests:
                combinations.append(temp)
                return combinations[0]  # Return first valid combo

    return []


def is_high_traffic(date_str):
    try:
        d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return d.strftime("%m-%d") in HIGH_TRAFFIC_DAYS
    except ValueError:
        return False


def make_reservation():
    print("\n--- Make a Reservation ---")
    name = input("Your name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    guests = int(input("Number of guests: "))

    user = User(name, phone, email)
    high_traffic = is_high_traffic(date)

    if high_traffic:
        print("Note: This is a high-traffic day. Credit card required.")
        cc = input("Enter valid credit card (dummy input): ")

    tables = find_tables_for_guests(guests)
    if not tables:
        print("Sorry, no available tables for the requested size.")
        return

    for t in tables:
        t["reserved"] = True

    print(f"Reserved table(s): {[t['id'] for t in tables]}")
    if len(tables) > 1:
        print("Owner will be notified to combine tables.")

    RESERVATIONS.append({
        "user": user,
        "tables": tables,
        "date": date,
        "time": time,
        "guests": guests,
        "high_traffic": high_traffic
    })

    reg_prompt = input("Would you like to register and earn dining points? (yes/no): ").lower()
    if reg_prompt == "yes":
        user.register()

    print("Reservation complete. No-show will incur a $10 fee.\n")


# --------- Entry Point --------------
def main():
    while True:
        print("\n--- Welcome to the Restaurant Reservation System ---")
        print("1. Make a Reservation")
        print("2. View Reservations")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            make_reservation()
        elif choice == "2":
            for r in RESERVATIONS:
                print(f"{r['user'].name} - {r['date']} at {r['time']} for {r['guests']} guests. Tables: {[t['id'] for t in r['tables']]}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
