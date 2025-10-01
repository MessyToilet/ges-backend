from db.base import Base 
from db.session import SessionLocal, engine
from db.models import WeightStandard, WeightClass



def init_db():
    print("[-] Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("[+] Database initialized!")

def seed_ibjjf_weight_classes():
    session = SessionLocal()

    # Check if already seeded
    if session.query(WeightStandard).filter_by(name="IBJJF").first():
        print("[+] IBJJF weight classes already seeded.")
        session.close()
        return

    ibjjf = WeightStandard(name="IBJJF", description="International Brazilian Jiu-Jitsu Federation")
    session.add(ibjjf)
    session.flush()  # Get ibjjf.id

    # IBJJF MALE & FEMALE GI
    weight_classes = [
        # Male Gi
        WeightClass(name="Rooster", gender="Male", format="Gi", min_weight_kg=None, max_weight_kg=57.5, standard_id=ibjjf.id),
        WeightClass(name="Light Feather", gender="Male", format="Gi", min_weight_kg=57.5, max_weight_kg=64.0, standard_id=ibjjf.id),
        WeightClass(name="Feather", gender="Male", format="Gi", min_weight_kg=64.0, max_weight_kg=70.0, standard_id=ibjjf.id),
        WeightClass(name="Light", gender="Male", format="Gi", min_weight_kg=70.0, max_weight_kg=76.0, standard_id=ibjjf.id),
        WeightClass(name="Middle", gender="Male", format="Gi", min_weight_kg=76.0, max_weight_kg=82.3, standard_id=ibjjf.id),
        WeightClass(name="Medium Heavy", gender="Male", format="Gi", min_weight_kg=82.3, max_weight_kg=88.3, standard_id=ibjjf.id),
        WeightClass(name="Heavy", gender="Male", format="Gi", min_weight_kg=88.3, max_weight_kg=94.3, standard_id=ibjjf.id),
        WeightClass(name="Super Heavy", gender="Male", format="Gi", min_weight_kg=94.3, max_weight_kg=97.5, standard_id=ibjjf.id),
        WeightClass(name="Ultra Heavy", gender="Male", format="Gi", min_weight_kg=97.5, max_weight_kg=None, standard_id=ibjjf.id),

        # Female Gi
        WeightClass(name="Rooster", gender="Female", format="Gi", min_weight_kg=None, max_weight_kg=47.5, standard_id=ibjjf.id),
        WeightClass(name="Light Feather", gender="Female", format="Gi", min_weight_kg=47.5, max_weight_kg=52.2, standard_id=ibjjf.id),
        WeightClass(name="Feather", gender="Female", format="Gi", min_weight_kg=52.2, max_weight_kg=57.0, standard_id=ibjjf.id),
        WeightClass(name="Light", gender="Female", format="Gi", min_weight_kg=57.0, max_weight_kg=62.8, standard_id=ibjjf.id),
        WeightClass(name="Middle", gender="Female", format="Gi", min_weight_kg=62.8, max_weight_kg=69.1, standard_id=ibjjf.id),
        WeightClass(name="Medium Heavy", gender="Female", format="Gi", min_weight_kg=69.1, max_weight_kg=76.1, standard_id=ibjjf.id),
        WeightClass(name="Heavy", gender="Female", format="Gi", min_weight_kg=76.1, max_weight_kg=82.3, standard_id=ibjjf.id),
        WeightClass(name="Super Heavy", gender="Female", format="Gi", min_weight_kg=82.3, max_weight_kg=None, standard_id=ibjjf.id),
    ]

    # IBJJF MALE & FEMALE NO-GI
    weight_classes += [
    # Male NoGi
    WeightClass(name="Rooster", gender="Male", format="NoGi", min_weight_kg=None, max_weight_kg=55.5, standard_id=ibjjf.id),
    WeightClass(name="Light Feather", gender="Male", format="NoGi", min_weight_kg=55.5, max_weight_kg=61.5, standard_id=ibjjf.id),
    WeightClass(name="Feather", gender="Male", format="NoGi", min_weight_kg=61.5, max_weight_kg=67.5, standard_id=ibjjf.id),
    WeightClass(name="Light", gender="Male", format="NoGi", min_weight_kg=67.5, max_weight_kg=73.5, standard_id=ibjjf.id),
    WeightClass(name="Middle", gender="Male", format="NoGi", min_weight_kg=73.5, max_weight_kg=79.5, standard_id=ibjjf.id),
    WeightClass(name="Middle Heavy", gender="Male", format="NoGi", min_weight_kg=79.5, max_weight_kg=85.5, standard_id=ibjjf.id),
    WeightClass(name="Heavy", gender="Male", format="NoGi", min_weight_kg=85.5, max_weight_kg=91.5, standard_id=ibjjf.id),
    WeightClass(name="Super Heavy", gender="Male", format="NoGi", min_weight_kg=91.5, max_weight_kg=97.5, standard_id=ibjjf.id),
    WeightClass(name="Ultra Heavy", gender="Male", format="NoGi", min_weight_kg=97.5, max_weight_kg=None, standard_id=ibjjf.id),

    # Female NoGi
    WeightClass(name="Rooster", gender="Female", format="NoGi", min_weight_kg=None, max_weight_kg=46.5, standard_id=ibjjf.id),
    WeightClass(name="Light Feather", gender="Female", format="NoGi", min_weight_kg=46.5, max_weight_kg=51.5, standard_id=ibjjf.id),
    WeightClass(name="Feather", gender="Female", format="NoGi", min_weight_kg=51.5, max_weight_kg=56.5, standard_id=ibjjf.id),
    WeightClass(name="Light", gender="Female", format="NoGi", min_weight_kg=56.5, max_weight_kg=61.5, standard_id=ibjjf.id),
    WeightClass(name="Middle", gender="Female", format="NoGi", min_weight_kg=61.5, max_weight_kg=66.5, standard_id=ibjjf.id),
    WeightClass(name="Middle Heavy", gender="Female", format="NoGi", min_weight_kg=66.5, max_weight_kg=71.5, standard_id=ibjjf.id),
    WeightClass(name="Heavy", gender="Female", format="NoGi", min_weight_kg=71.5, max_weight_kg=76.5, standard_id=ibjjf.id),
    WeightClass(name="Super Heavy", gender="Female", format="NoGi", min_weight_kg=76.5, max_weight_kg=None, standard_id=ibjjf.id),
    ]


    session.add_all(weight_classes)
    session.commit()
    session.close()
    print("[+] IBJJF weight classes seeded.")