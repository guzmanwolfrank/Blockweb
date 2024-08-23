import platform
import subprocess

def block_website(site):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if platform.system() == "Windows" else "/etc/hosts"
    
    redirect = "127.0.0.1"
    
    with open(hosts_path, 'r+') as file:
        content = file.read()
        if site not in content:
            file.write(f"{redirect} {site}\n")
            file.write(f"{redirect} www.{site}\n")
            print(f"{site} has been blocked.")
        else:
            print(f"{site} is already blocked.")

def flush_dns():
    if platform.system() == "Windows":
        subprocess.run(["ipconfig", "/flushdns"], check=True)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"], check=True)
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "systemd-resolve", "--flush-caches"], check=True)
    print("DNS cache flushed.")

if __name__ == "__main__":
    site_to_block = "EXAMPLE.COM"
    block_website(site_to_block)
    flush_dns()
    print("Please restart your browser for changes to take effect.")
    
    