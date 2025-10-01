from db import init_db
from divisions import seed_ibjjf_weight_classes

if __name__ == "__main__":
    init_db()
    seed_ibjjf_weight_classes()
