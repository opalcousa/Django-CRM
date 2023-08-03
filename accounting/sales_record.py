from dataclasses import dataclass
from faker import Faker
import datetime

fake = Faker()

@dataclass
class SalesRecord:
    date: datetime.date
    customer_name: str
    product_sold: str
    total_price: float

def generate_random_sales_record(start_date, end_date):
    date = fake.date_between_dates(date_start=start_date, date_end=end_date)
    customer_name = fake.name()
    product_sold = fake.word()
    total_price = round(fake.random_number(digits=2, fix_len=True) * 0.01, 2)
    return SalesRecord(date, customer_name, product_sold, total_price)
