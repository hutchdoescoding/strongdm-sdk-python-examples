import os
import strongdm

def get_remote_identity_group_id(client):
    groups = client.remote_identity_groups.list('name:"Default"')
    groups = list(groups)
    return groups[0].id

def list_users(client):
    users = client.accounts.list('')
    for account in users:
        print(account)

def main():
    # Define Access Keys
    api_access_key = os.getenv('SDM_API_ACCESS_KEY')
    api_secret_key = os.getenv('SDM_API_SECRET_KEY')
    # Create SDM Client
    client = strongdm.Client(api_access_key, api_secret_key)
    # Get Remote Identity Default Group ID
    #  This is a required argument when creating 
    #  a user's remote identity. 
    ri_group_id = get_remote_identity_group_id(client)

    # To create a remote identity, you must supply: 
    #  The account_id for the user that you will 
    #   create the remote identity for
    #  The username that will be set as the remote identity
    #  The remote_identity_group_id, which will be the same
    #   for everyone in the current implementation. 

    remote_identity_to_create = strongdm.RemoteIdentity(
        account_id="a-777777777777",
        remote_identity_group_id=ri_group_id,
        username='username_populated_with_sdk'
    )
    create_response = client.remote_identities.create(remote_identity_to_create)
    print(create_response)
    list_of_remoteidentities = client.remote_identities.list('')
    for r in list_of_remoteidentities: 
        print(r)
    exit()

if __name__ == "__main__":
    main()