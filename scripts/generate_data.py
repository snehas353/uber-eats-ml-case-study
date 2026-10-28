import os
import numpy as np
import pandas as pd

np.random.seed(42)

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

NUM_CUSTOMERS = 1000
NUM_RESTAURANTS = 100
NUM_DRIVERS = 150
NUM_ORDERS = 5000

CITIES = ["Bengaluru", "Mumbai", "Delhi", "Hyderabad", "Pune"]

# 1. Customers
customers = pd.DataFrame({
    "customer_id": [f"C{i:04d}" for i in range(1, NUM_CUSTOMERS + 1)],
    "age": np.random.randint(18, 71, NUM_CUSTOMERS),
    "gender": np.random.choice(
        ["Female", "Male", "Other"], NUM_CUSTOMERS,
        p=[0.48, 0.48, 0.04]
    ),
    "city": np.random.choice(CITIES, NUM_CUSTOMERS),
    "signup_date": pd.to_datetime(
        np.random.choice(
            pd.date_range("2023-01-01", "2025-12-31"),
            NUM_CUSTOMERS
        )
    )
})

# 2. Restaurants
restaurants = pd.DataFrame({
    "restaurant_id": [f"R{i:03d}" for i in range(1, NUM_RESTAURANTS + 1)],
    "restaurant_name": [
        f"Restaurant_{i:03d}" for i in range(1, NUM_RESTAURANTS + 1)
    ],
    "category": np.random.choice(
        ["Indian", "Chinese", "Italian", "Fast Food", "Healthy", "Desserts"],
        NUM_RESTAURANTS
    ),
    "restaurant_rating": np.round(
        np.random.uniform(2.5, 5.0, NUM_RESTAURANTS), 1
    ),
    "prep_time_minutes": np.random.randint(10, 41, NUM_RESTAURANTS),
    "city": np.random.choice(CITIES, NUM_RESTAURANTS)
})

# 3. Drivers
drivers = pd.DataFrame({
    "driver_id": [f"D{i:03d}" for i in range(1, NUM_DRIVERS + 1)],
    "vehicle_type": np.random.choice(
        ["Bike", "Scooter", "Car"], NUM_DRIVERS,
        p=[0.25, 0.60, 0.15]
    ),
    "driver_rating": np.round(
        np.random.uniform(3.0, 5.0, NUM_DRIVERS), 1
    ),
    "experience_months": np.random.randint(1, 73, NUM_DRIVERS)
})

# 4. Orders
order_ids = [f"O{i:05d}" for i in range(1, NUM_ORDERS + 1)]

order_timestamps = pd.to_datetime(
    np.random.choice(
        pd.date_range("2025-01-01", "2025-12-31 23:00:00", freq="h"),
        NUM_ORDERS
    )
)

order_amounts = np.round(
    np.random.uniform(150, 1500, NUM_ORDERS), 2
)

tip_amounts = np.round(
    order_amounts * np.random.uniform(0, 0.20, NUM_ORDERS), 2
)

orders = pd.DataFrame({
    "order_id": order_ids,
    "customer_id": np.random.choice(customers["customer_id"], NUM_ORDERS),
    "restaurant_id": np.random.choice(restaurants["restaurant_id"], NUM_ORDERS),
    "order_timestamp": order_timestamps,
    "order_amount": order_amounts,
    "tip_amount": tip_amounts,
    "weather": np.random.choice(
        ["Clear", "Rainy", "Cloudy", "Stormy"], NUM_ORDERS,
        p=[0.50, 0.20, 0.25, 0.05]
    ),
    "traffic_condition": np.random.choice(
        ["Low", "Medium", "High"], NUM_ORDERS,
        p=[0.30, 0.45, 0.25]
    ),
    "order_status": np.random.choice(
        ["Delivered", "Cancelled", "Preparing", "On the Way"],
        NUM_ORDERS, p=[0.90, 0.05, 0.02, 0.03]
    )
})

# 5. Deliveries
prep_lookup = restaurants.set_index("restaurant_id")["prep_time_minutes"]
prep_time = orders["restaurant_id"].map(prep_lookup).to_numpy()

distance = np.round(np.random.uniform(1, 15, NUM_ORDERS), 2)

traffic_delay = orders["traffic_condition"].map({
    "Low": 0, "Medium": 8, "High": 18
}).to_numpy()

weather_delay = orders["weather"].map({
    "Clear": 0, "Cloudy": 3, "Rainy": 10, "Stormy": 20
}).to_numpy()

base_delivery_time = (
    prep_time + distance * 3 + traffic_delay + weather_delay
)

random_variation = np.random.normal(
    loc=0, scale=5, size=NUM_ORDERS
)

delivery_minutes = np.maximum(
    10, base_delivery_time + random_variation
).round().astype(int)

delivery_status = orders["order_status"].map({
    "Delivered": "Delivered",
    "Cancelled": "Cancelled",
    "Preparing": "Pending",
    "On the Way": "In Transit"
})

deliveries = pd.DataFrame({
    "delivery_id": [f"DL{i:05d}" for i in range(1, NUM_ORDERS + 1)],
    "order_id": order_ids,
    "driver_id": np.random.choice(drivers["driver_id"], NUM_ORDERS),
    "delivery_distance_km": distance,
    "preparation_time_minutes": prep_time,
    "delivery_time_minutes": np.where(
        orders["order_status"].eq("Delivered"),
        delivery_minutes, np.nan
    ),
    "delivery_status": delivery_status
})

# 6. Payments
payment_statuses = np.random.choice(
    ["Completed", "Failed", "Pending", "Refunded"],
    NUM_ORDERS,
    p=[0.88, 0.04, 0.03, 0.05]
)

# Cancelled orders are refunded in this synthetic dataset
payment_statuses = np.where(
    orders["order_status"].eq("Cancelled"),
    "Refunded",
    payment_statuses
)

payments = pd.DataFrame({
    "payment_id": [f"P{i:05d}" for i in range(1, NUM_ORDERS + 1)],
    "order_id": order_ids,
    "payment_method": np.random.choice(
        ["Card", "UPI", "Cash", "Wallet"], NUM_ORDERS
    ),
    "payment_status": payment_statuses,
    "payment_amount": np.round(
        orders["order_amount"] + orders["tip_amount"], 2
    )
})

# 7. Reviews: only delivered orders can receive reviews
delivered_ids = orders.loc[
    orders["order_status"].eq("Delivered"), "order_id"
].to_numpy()

review_count = int(len(delivered_ids) * 0.35)

reviewed_ids = np.random.choice(
    delivered_ids, review_count, replace=False
)

review_texts = [
    "Fast delivery and tasty food",
    "Food was good but delivery was slow",
    "Excellent experience",
    "Order arrived late",
    "Packaging could be improved",
    "Great restaurant and service"
]

review_order_timestamps = (
    orders.set_index("order_id")
    .loc[reviewed_ids, "order_timestamp"]
    .reset_index(drop=True)
)

reviews = pd.DataFrame({
    "review_id": [f"RV{i:05d}" for i in range(1, review_count + 1)],
    "order_id": reviewed_ids,
    "review_rating": np.random.randint(1, 6, review_count),
    "review_text": np.random.choice(review_texts, review_count),
    "review_timestamp": (
        review_order_timestamps
        + pd.to_timedelta(
            np.random.randint(1, 49, review_count), unit="h"
        )
    )
})

# Save all seven datasets
datasets = {
    "customers": customers,
    "restaurants": restaurants,
    "drivers": drivers,
    "orders": orders,
    "deliveries": deliveries,
    "payments": payments,
    "reviews": reviews
}

for name, df in datasets.items():
    file_path = os.path.join(OUTPUT_DIR, f"{name}.csv")
    df.to_csv(file_path, index=False)
    print(f"{name}.csv: {df.shape[0]} rows, {df.shape[1]} columns")

print("\nAll seven synthetic datasets generated successfully!")
