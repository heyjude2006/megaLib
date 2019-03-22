# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), input('Password: '), input('TFA (Leave black if not enabled): '))

# Order LAG ports
port = megalib.port(auth.header, loc_id, '''megaLib LAG''', 10000, lag_count=2)

# Check for 'Great Success!'
if port.status_code == 200:
    print('Great Success!')
