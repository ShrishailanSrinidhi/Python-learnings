import ipaddress

ipadd = input("Enter IP address: ")

def IPvalidator(ipadd):
    try:
        ip = ipaddress.ip_address(ipadd)
        print(f'IP address {ipadd} is valid')
    except ValueError:
        print(f'IP address {ipadd} is invalid')

IPvalidator(ipadd)