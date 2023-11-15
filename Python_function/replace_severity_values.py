import subprocess
package_name = 'memphis-py-beta'
try:
    subprocess.check_call(['pip', 'install', package_name])
    print(f'Successfully installed {package_name}')
except subprocess.CalledProcessError as e:
    print(f'Error installing {package_name}: {e}')
    
from memphis.functions import create_function
import json

def handler(event, context): # The name of this function should match the handler field in the memphis.yaml file
    return create_function(event, user_func = replace_severity_values)

def replace_severity_values(msg_payload, msg_headers):
    try:
        # Convert bytes to a JSON object
        payload =  str(msg_payload, 'utf-8')
        message_json = json.loads(payload)
        
        # Define a mapping of severity values
        severity_mapping = {
            1: 'low',
            2: 'medium',
            3: 'high',
            4: 'critical',
            'warning': 'low',
            'minor': 'medium',
            'major': 'high',
            'critical': 'critical'
        }

        # Replace severity values in the JSON data
        if 'severity' in message_json:
            old_severity = message_json['severity']
            new_severity = severity_mapping.get(old_severity, old_severity)
            message_json['severity'] = new_severity

        # Convert the modified JSON object back to a JSON-formatted string
        output_json = json.dumps(message_json, indent=2)

        return bytes(json.dumps(output_json), encoding='utf-8'), msg_headers


    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None, None





    
