import boto3
from settings.constants import COGNITO,CLIENT
from settings.env import get_env_vars
from typing import Dict, Optional
from settings.aws_service import cognito
client = cognito

env_vars: Dict[str, Optional[str]] = get_env_vars()
user_pool_id = env_vars.get(COGNITO,'us-east-1_546RUb4gO')
client_id = env_vars.get(CLIENT,'ovkvo2lg5g4j89rash1nmm5q5')


def initiate_forgot_password(event):
    obj = {}
    if event.get('queryparams'):
        queryparams = event.get('queryparams')
        if queryparams:
            email = queryparams.get('email').lower()
            response = client.list_users(
                UserPoolId=user_pool_id,
                Filter=f'email = "{email}"'
            )
            email_exist = response.get('Users')
            if email_exist:
                try:
                    # user = Get_Username(email)
                    if email:
                        username = email
                        if username:
                            response = client.forgot_password(
                            ClientId=client_id,
                            Username=username
                            )
                            obj['statusCode'] = 200
                            obj['success']= True
                            obj['message']= 'Password reset code sent to email.'
                        else:
                            obj['statusCode'] = 400
                            obj['message'] = 'user does not exist'
                    else:
                        obj['statusCode'] = 400
                        obj['message'] = 'Please enter the email address registered with Zita.'

                except client.exceptions.UserNotFoundException:
                    obj['statusCode'] = 404
                    obj['success']= False
                    obj['message']= 'User not found.'

                except client.exceptions.LimitExceededException:
                        obj['statusCode'] = 429
                        obj['success'] = False
                        obj['message'] = 'You have exceeded the maximum number of OTP requests. Please try again later.'        

                except Exception as e:
                    obj['message']= 'An internal server error occurred.'
            else:
                obj['message'] = 'Please enter the email address registered with Zita.'
                obj['statusCode'] = 400
                obj['success'] = False
        else:
            obj['message'] = 'Provide the valid email to proceed for reset password'
    else:
        obj['message'] = 'Provide the valid email to proceed for reset password'
    return obj


def verify_code_and_reset_password(event):
    obj = {}
    if event.get('queryparams'):
        queryparams = event.get('queryparams')
        if queryparams:
            email = queryparams.get('email').lower()
            confirmation_code=queryparams.get('confirmation_code')
            new_password=queryparams.get('new_password')
            user = Get_Username(email)
            username = user['username']
            if not new_password:
                obj['success']= False
                obj['message']= 'Please provide new password'
            else:
                try:
                    response = client.confirm_forgot_password(
                        ClientId=client_id,
                        Username=username,
                        ConfirmationCode=confirmation_code,
                        Password=new_password
                    )
                    obj['statusCode'] = 200
                    obj['success']= True
                    obj['message']= 'Password reset successfully.'

                except client.exceptions.CodeMismatchException:
                    obj['statusCode'] = 400
                    obj['success']= False
                    obj['message']= 'Verification code is invalid.'

                except client.exceptions.ExpiredCodeException:
                    obj['statusCode'] = 400
                    obj['success']= False
                    obj['message']= 'Confirmation code expired.'

                except Exception as e:
                    obj['success']= False
                    obj['message']= 'An internal server error occurred.'
        else:
            obj['message'] = 'Please provide the proper Username, Confirmation Code, New Password'
    else:
        obj['message'] = 'Please provide the proper Username, Confirmation Code, New Password'
    
    return obj

def Get_Username(email):
    obj = {}
    if email:
        response = client.list_users(
            UserPoolId=user_pool_id,
            Filter=f'email = "{email}"',
            Limit=1
        )    
        if response['Users']:
            username = response['Users'][0]['Username']
            print(username,'user')
            obj['username'] = username
    return obj

# email = "saransaran6967@gmail.com"
# username = Get_Username(email)
# print(username['username'],'user')

