import requests
import logging
import json

# Define authentication credentials
API_USERNAME = 'heron.arteaga.h@gmail.com'
API_TOKEN = 'pntb11edimm8vdpjrilpolj4hyu5iht7'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Make API call with the current credentials
response = requests.get('https://api.thousandeyes.com/v6/tests.json', auth=(API_USERNAME, API_TOKEN))

resp_body = response.json()

# API Response
if response.status_code == 200:
    for test in resp_body['test']:
        created_by = test['createdBy']
        test_id = test['testId']
        test_type = test['type']
        print("CreatedBy:", created_by)
        print("TestId:", test_id)
        print("Type:", test_type)

# Data from another ThousandEyes trial account
trial_email = 'mr.emilio.olguin@gmail.com'
trial_auth_token = 'cgzz63claa68qfrbv77gyj9cczejqvh0'
logging.info(f'Attempting to retrieve data from trial account: {trial_email}')

# API call with trial account credentials
trial_auth = (trial_email, trial_auth_token)
trial_response = requests.get('https://api.thousandeyes.com/v6/tests.json', auth=trial_auth)

if trial_response.status_code == 200:
    trial_data = trial_response.json()
    logging.info('List of tests from trial account:')
    for test in trial_data['test']:
        logging.info(f"Test ID: {test['testId']}, Test Name: {test['testName']}")
else:
    logging.error(f'Error calling API with trial account: {trial_response.status_code}')
