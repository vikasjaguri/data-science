#7. Create a function that grabs the email website domain from a string in the form : **user@domain.com.
#so for example, passinf "user@domain.com" would return: domain.com.
def get_domain(email):
    user, domain = email.split('@')
    return domain

email_address = "user@domain.com"
result = get_domain(email_address)
print(result)
