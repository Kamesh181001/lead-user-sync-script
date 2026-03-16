import csv
import sys
import uuid
from helpers import repo

BATCH_SIZE = 100


def _create_lead_data(lead_mobiles):
    lead_user_ids = repo.get_lead_user_ids(lead_mobiles)
    mobile_to_user_id_map = {user["mobile"]: user["id"]
                             for user in lead_user_ids}
    lead_data = []
    for mobile in lead_mobiles:
        if mobile_to_user_id_map.get(mobile) is not None:
            lead = {
                "name": "WILL NOT BE UPDATED",
                "mobile": mobile,
                "user_id": mobile_to_user_id_map.get(mobile)
            }
            lead_data.append(lead)
        else:
            print("User id does not exists for: ", mobile)
            print("User id does not exists for: ", mobile, file=sys.stderr)

    return lead_data


def _update_lead_user_ids(lead_mobiles):
    lead_data = _create_lead_data(lead_mobiles)
    response = repo.update_lead_user_id(lead_data)
    print("Batch response: ", response)
    print("\n\n")


def main():
    leads = repo.get_all_leads_mobile()
    lead_mobiles = []
    for lead in leads:
        lead_mobiles.append(lead["mobile"])
        if len(lead_mobiles) != BATCH_SIZE:
            continue
        _update_lead_user_ids(lead_mobiles)
        lead_mobiles = []

    if len(lead_mobiles) != 0:
        _update_lead_user_ids(lead_mobiles)


main()
