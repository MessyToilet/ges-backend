from db.session import SessionLocal
from db.models import WeightStandard, WeightClass


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


def seed_adcc_weight_classes():
    session = SessionLocal()

    if session.query(WeightStandard).filter_by(name="ADCC").first():
        print("[+] ADCC weight classes already seeded.")
        session.close()
        return

    adcc = WeightStandard(name="ADCC", description="Abu Dhabi Combat Club Submission Wrestling World Championship")
    session.add(adcc)
    session.flush()

    weight_classes = [
        WeightClass(name="Under 66kg", gender="Male", format="NoGi", min_weight_kg=None, max_weight_kg=66.0, standard_id=adcc.id),
        WeightClass(name="Under 77kg", gender="Male", format="NoGi", min_weight_kg=66.0, max_weight_kg=77.0, standard_id=adcc.id),
        WeightClass(name="Under 88kg", gender="Male", format="NoGi", min_weight_kg=77.0, max_weight_kg=88.0, standard_id=adcc.id),
        WeightClass(name="Under 99kg", gender="Male", format="NoGi", min_weight_kg=88.0, max_weight_kg=99.0, standard_id=adcc.id),
        WeightClass(name="Over 99kg", gender="Male", format="NoGi", min_weight_kg=99.0, max_weight_kg=None, standard_id=adcc.id),

        WeightClass(name="Under 60kg", gender="Female", format="NoGi", min_weight_kg=None, max_weight_kg=60.0, standard_id=adcc.id),
        WeightClass(name="Over 60kg", gender="Female", format="NoGi", min_weight_kg=60.0, max_weight_kg=None, standard_id=adcc.id),
    ]

    session.add_all(weight_classes)
    session.commit()
    session.close()
    print("[+] ADCC weight classes seeded.")


def seed_grappling_industries_weight_classes():
    session = SessionLocal()

    if session.query(WeightStandard).filter_by(name="Grappling Industries").first():
        print("[+] Grappling Industries weight classes already seeded.")
        session.close()
        return

    gi_standard = WeightStandard(
        name="Grappling Industries",
        description="Round-robin format with Gi and NoGi divisions"
    )
    session.add(gi_standard)
    session.flush()

    weight_classes = [
        # Male Gi
        WeightClass(name="Rooster", gender="Male", format="Gi", max_weight_kg=57.5, standard_id=gi_standard.id),
        WeightClass(name="Light Feather", gender="Male", format="Gi", min_weight_kg=57.5, max_weight_kg=64.0, standard_id=gi_standard.id),
        WeightClass(name="Feather", gender="Male", format="Gi", min_weight_kg=64.0, max_weight_kg=70.0, standard_id=gi_standard.id),
        WeightClass(name="Light", gender="Male", format="Gi", min_weight_kg=70.0, max_weight_kg=76.0, standard_id=gi_standard.id),
        WeightClass(name="Middle", gender="Male", format="Gi", min_weight_kg=76.0, max_weight_kg=82.3, standard_id=gi_standard.id),
        WeightClass(name="Medium Heavy", gender="Male", format="Gi", min_weight_kg=82.3, max_weight_kg=88.3, standard_id=gi_standard.id),
        WeightClass(name="Heavy", gender="Male", format="Gi", min_weight_kg=88.3, max_weight_kg=94.3, standard_id=gi_standard.id),
        WeightClass(name="Super Heavy", gender="Male", format="Gi", min_weight_kg=94.3, max_weight_kg=100.5, standard_id=gi_standard.id),
        WeightClass(name="Ultra Heavy", gender="Male", format="Gi", min_weight_kg=100.5, max_weight_kg=None, standard_id=gi_standard.id),

        # Female Gi
        WeightClass(name="Light Feather", gender="Female", format="Gi", max_weight_kg=53.5, standard_id=gi_standard.id),
        WeightClass(name="Feather", gender="Female", format="Gi", min_weight_kg=53.5, max_weight_kg=58.5, standard_id=gi_standard.id),
        WeightClass(name="Light", gender="Female", format="Gi", min_weight_kg=58.5, max_weight_kg=64.0, standard_id=gi_standard.id),
        WeightClass(name="Middle", gender="Female", format="Gi", min_weight_kg=64.0, max_weight_kg=69.0, standard_id=gi_standard.id),
        WeightClass(name="Medium Heavy", gender="Female", format="Gi", min_weight_kg=69.0, max_weight_kg=74.0, standard_id=gi_standard.id),
        WeightClass(name="Heavy", gender="Female", format="Gi", min_weight_kg=74.0, max_weight_kg=None, standard_id=gi_standard.id),

        # NoGi (same structure, format="NoGi")
        # You can duplicate the above with format="NoGi" if Grappling Industries offers both
    ]

    session.add_all(weight_classes)
    session.commit()
    session.close()
    print("[+] Grappling Industries weight classes seeded.")