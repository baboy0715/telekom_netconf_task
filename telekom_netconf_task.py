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
        target_ip = input("Enter an IP Address: ")
        if validate_ip(target_ip):
            break
        else:
            print("This is not a valid IPv4 address!")
            
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
            print("Connected succesfully")
            
            while True:
                print("\nAvailable operations:")
                print("1 - Get Running Configuration")
                print("2 - Get Device State")
                choice = input("Select operation (1 or 2): ")
                if choice == "1":
                    print("Requesting running configuration...")
                    result = m.get_config(source='running')
                    break
                elif choice == "2":
                    print("Requesting device state...")
                    result = m.get()
                    break
                else:
                    print("Please enter 1 or 2!")

            print("\n--- XML Result ---")
            print(result.data_xml)
               
   except Exception as e:
        print(f"\nError {e}")

if __name__ == "__main__":
    main()
        