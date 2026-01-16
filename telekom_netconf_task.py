from statistics import harmonic_mean
from tkinter import EXCEPTION
from ncclient import manager
def main():
    target_ip =input("Type IP Address: ")
    user = input("Username: ")
    passw = input("Password: ")
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
        print("f\nError {e}")
        

if __name__ == "__main__":
    main()
        