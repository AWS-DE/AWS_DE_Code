import json
import logging 


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    
    result = None 

    action = event.get("action")
    number = event.get("number",0)

    if action == 'increment' :
        result = number + 1 
        logger.info("calculated increment value is {result}")
    elif action == 'decrement' :
        result = number - 1 
        logger.info("calculated decrement value is {result}")
    else :
        logger.error(f'{action} is not a valid action')
    
    
    return {
        'result': result
    }
