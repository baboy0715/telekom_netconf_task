from ncclient import manager
import getpass
import re
def validate_ip(ip):
    pattern = r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$"
    if re.match(pattern, ip):
        return True
    return False
def main():
   while True:
        target_ip = input("Type IP Address: ")
        if validate_ip(target_ip):
            break
        else:
            print("Error: This is not a valid IPv4 address! Please try again.")
   user = input("Username: ")
   passw = getpass.getpass("Password: ")
   try:
        print(f"Connecting to {target_ip}...")
        with manager.connect(
            host=target_ip,
            port=830,
            username=user,
            password=passw,
            hostkey_verify=False
        ) as m:
            print("Connected succesfully!")
            print("Requesting 'running' configuration...")
            config = m.get_config(source='running')
            print("\n--- XML Config ---")
            print(config.data_xml)
               
   except Exception as e:
        print(f"\nError {e}")
        

if __name__ == "__main__":
    main()
        