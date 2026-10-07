import pandas as pd
import numpy as np

from faker import Faker
from pathlib import Path

# Initialising Faker
fake = Faker("en_IN")
# This will generate indian styles names

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "data" / "incoming"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# For 50 customers
NUM_CUSTOMERS = 50

customers = []

for i in range(1, NUM_CUSTOMERS + 1):
    customer = {
        "customer_id": f"C{i:03d}",
        "name": fake.name(),
        "age": np.random.randint(21, 70),
        "city": np.random.choice([
            "Pune",
            "Mumbai",
            "Delhi",
            "Bangalore",
            "Hyderabad",
            "Chennai",
            "Ahmedabad",
            "Kolkata"
        ]),
        "occupation": np.random.choice([
            "Engineer",
            "Doctor",
            "Teacher",
            "Business Owner",
            "Accountant",
            "Lawyer",
            "Designer",
            "Sales Manager"
        ])
    }

    customers.append(customer)

    customers_df = pd.DataFrame(customers)
    # Above is conversion of that Dictionary customers into Dataframe

    customers_df.to_csv(
        OUTPUT_DIR / "customer.csv",
        index=False
    )

    NUM_POLICIES = 50

policies = []

for i in range(1, NUM_POLICIES + 1):

    start_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    policy = {
        "policy_id": f"P{i:03d}",
        "customer_id": np.random.choice(customers_df["customer_id"]),
        "policy_type": np.random.choice([
            "Motor",
            "Health",
            "Home",
            "Travel"
        ]),
        "start_date": start_date,
        "premium": np.random.randint(5000, 50000)
    }

    policies.append(policy)

policies_df = pd.DataFrame(policies)

policies_df["start_date"] = pd.to_datetime(
    policies_df["start_date"]
)

policies_df["end_date"] = (
    policies_df["start_date"] 
    + pd.DateOffset(years=1)
)

policies_df.to_csv(
    OUTPUT_DIR / "policies.csv",
    index=False
)

NUM_CLAIMS = 50

claims = []

for i in range(1, NUM_CLAIMS + 1):

    policy = policies_df.sample(1).iloc[0]

    claim_date = fake.date_between(
        start_date=policy["start_date"],
        end_date="today"
    )

    claim = {
        "claim_id": f"CL{i:03d}",
        "policy_id": policy["policy_id"],
        "claim_date": claim_date,
        "claim_type": np.random.choice([
            "Accident",
            "Theft",
            "Hospitalization",
            "Property Damage",
            "Travel Delay"
        ]),
        "claim_amount": np.random.randint(
            5000,
            250000
        ),
        "claim_status": np.random.choice([
            "Approved",
            "Rejected",
            "Under Investigation"
        ])
    }

    claims.append(claim)

claims_df = pd.DataFrame(claims)

claims_df.to_csv(
    OUTPUT_DIR / "claims.csv",
    index=False
)
print("   ")
print(f"Customers: {len(customers_df)}")
print(f"Policies: {len(policies_df)}")
print(f"Claims: {len(claims_df)}")
print(f"Output: {OUTPUT_DIR}")