from app.main import db
from app.main.model.opportunity import Opportunity

def get_all_opportunities():
    return Opportunity.query.all()

def save_new_opportunity(new_lead, oportunity):
    new_oportunity=Oportunity(new_lead, oportunity)
    save_changes(new_oportunity)

def change_all_opportunities_description(add_to_desc):
    all = get_all_opportunities()
    for opp in all:
        opp.description = opp.description+add_to_desc
    db.session.commit() 


def save_changes(data):
	db.session.add(data)
	db.session.commit()
