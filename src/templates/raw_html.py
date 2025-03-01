PASSWORD_RESET_EMAIL_CONTENT = '''
<!DOCTYPE html>
<html>
<head>
    <title>Password Reset Request</title>
</head>
<body>
    <p>Hi <b>{recipient}</b>,</p>
    
    <p>You are receiving this email because you requested a password reset. Please click on the Button 
    below to create a new password:</p>
    
    <p><a href="{reset_link}">Reset Password</a></p>
    
    <p>If you did not request a password reset, please disregard this email. Your password will remain unchanged. Please note, the link will expire in one day. If your link expires, you can request a new one.</p>
    
    <p>Best regards,</p>
    
    <p>The Zita Team</p>
</body>
</html>
'''
