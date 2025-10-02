from db.session import SessionLocal
from db.models import Fighter, Division, EloRating

def delete_fighter():
    pass

def create_fighter(
        firstname: str, 
        lastname: str, 
        weight: float, 
        gender: str, 
        ped_status: bool, 
        phone_number: int
        ) -> None:
    
    with SessionLocal as s:
        new_fighter = Fighter(
            first_name=firstname,
            last_name=lastname,
            gender=gender,
            weight=weight,
            on_peds=ped_status,
            phone_number=phone_number,
        )

        s.add(new_fighter)
        s.commit()
        s.refresh(new_fighter)  # optional: populates new_fighter.id

        print("[+] Created fighter:", new_fighter.last_name, new_fighter.last_name)
        return 
        
# Setters

def update_first_name(id: int, new_name: str) -> None:
    with SessionLocal() as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter: 
            fighter.first_name = new_name
        else: 
            print("[!] Failed to update fighter (Couldn't find fighter)")

def update_last_name(id: int, new_lastname: str) -> None:
    with SessionLocal() as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter:
            fighter.last_name = new_lastname
        else:
            print("[!] Failed to update fighter (Couldn't find fighter)")



def update_email(id: int, new_email: str) -> None :
    with SessionLocal() as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter:
            fighter.email = new_email
        else:
            print("[!] Failed to update fighter (Couldn't find fighter)")


def update_phone_number(id: int, new_phonenumber: int) -> None :
    with SessionLocal as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter:
            fighter.phone_number = new_phonenumber
        else:
            print("[!] Failed to update fighter (Couldn't find fighter)")

def update_birthday(id: int, date: str) -> None:
    with SessionLocal as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter: 
            fighter.birthday = date
        else:
            print("[!] Failed to update fighter (Couldn't find fighter)")
    


def update_gender(id: int, new_gender: str) -> None:
    with SessionLocal as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter: 
            fighter.gender = new_gender
        else:
            print("[!] Failed to update fighter (Couldn't find fighter)")

def update_weight(weight: float) -> None:
    with SessionLocal as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter: 
            fighter.weight = weight
        else:
            print("[!] Failed to update fighter (Couldn't find fighter)")


def update_on_peds(status: bool) -> None:
    with SessionLocal as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter: 
            fighter.is_on_peds = status
        else:
            print("[!] Failed to update fighter (Couldn't find fighter)")
    
def update_elo(id: int, elo_gain: int) -> None:
    """
    id:         fighter id
    elo_gain:   elo to add to fighter
    """
    with SessionLocal as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        if fighter: 
            fighter.elo += elo_gain
        else:
            print("[!] Failed to update fighter (Couldn't find fighter)")

# Getters

def get_id_by_phone_number(phone_number: int) -> int | None:
    with SessionLocal as s:
        fighter = s.query(Fighter).filter_by(phone_number=phone_number).first()
        s.close()
        return fighter.id if fighter else None

def is_on_peds(id: int) -> bool:
    with SessionLocal as s:
        fighter = s.query(Fighter).filter_by(id=id).first()
        return fighter.is_on_peds if fighter else False




