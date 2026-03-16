from .hasura_client import run_query


def update_lead_user_id(lead_data):
    query = '''
        mutation create_leads($leads:[leads_leads_insert_input!]!){
            insert_leads_leads(objects: $leads,on_conflict:{constraint:leads_mobile_key,update_columns:[user_id]}){
                affected_rows
            }
        }
    '''
    variables = {"leads": lead_data}
    response = run_query(query, variables)

    return response


def get_all_leads_mobile():
    query = '''
    query get_all_leads_mobile{
        leads_leads{
            id
            mobile
        }
    }
    '''

    response = run_query(query, {})

    return response["leads_leads"]


def get_lead_user_ids(lead_mobiles):
    query = '''
    query get_lead_user_ids($lead_mobiles:[bigint!]!){
        users_users(where:{mobile:{_in:$lead_mobiles}}){
            id
            mobile
        }
    }
    '''

    variables = {
        "lead_mobiles": lead_mobiles
    }

    response = run_query(query, variables)

    return response["users_users"]
