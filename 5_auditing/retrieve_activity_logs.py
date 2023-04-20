import os
import strongdm
import datetime

# Define Access Keys
api_access_key = os.getenv('SDM_API_ACCESS_KEY')
api_secret_key = os.getenv('SDM_API_SECRET_KEY')
# Create SDM Client
client = strongdm.Client(api_access_key, api_secret_key)

# Use datetime library to specify date/time ranges when requesting activity logs
today = datetime.date.today()
# Start at 20 days ago 
start = today - datetime.timedelta(days=20)
# End time range at 5 days ago
end = today - datetime.timedelta(days=5)
# Specify after and before filters to get activities from a specific time range
activities= client.activities.list("after:? before:?", start, end)

for activity in activities:
    print(activity)

exit()