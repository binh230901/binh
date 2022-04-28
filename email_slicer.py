def email_process(email):
    #binh230901@gmail.com
    email_username = email[: email.index('@')]
    email_domain = email[email.index('@') + 1 :]
    return [email_username, email_domain]
    
def print_return(email_username, email_domain):
    print(f'your email user name is: {email_username}', f'domain user name is: {email_domain}', sep= '\n')


def main():
    email = input('type your email: ')
    email_username, email_domain = email_process(email)
    print_return(email_username, email_domain)

if __name__ == '__main__':
    main()

