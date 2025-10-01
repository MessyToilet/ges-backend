from db import init_db, clear_db
from divisions.seed import (
    seed_ibjjf_weight_classes,
    seed_adcc_weight_classes,
    seed_grappling_industries_weight_classes
    )

import sys 


if __name__ == "__main__":

    if "--init" in sys.argv:
        init_db()
    if "--clear" in sys.argv:
        clear_db() 
    if "--seed" in sys.argv:
        seed_ibjjf_weight_classes()
        seed_adcc_weight_classes()
        seed_grappling_industries_weight_classes()
    else:
        print("--init, --clear, --seed")