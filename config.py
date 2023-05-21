"""
Configuration module for loading environment variables.

Modules:
- dotenv: Loads environment variables from a file.

"""

from dotenv import load_dotenv

state = 'local'

def load_config():
    """
    Loads configuration settings based on the state.

    - If the state is 'local', it loads environment variables from the '.env.local' file.
    - If the state is 'remote', it loads environment variables from the '.env.remote' file.
    - If the state is not recognized, an error message is returned.

    """
    if state == 'local':
        load_dotenv('.env.local')
    elif state == 'remote':
        load_dotenv('.env.remote')
    else:
        return f'{state} not recognized'

load_config()
