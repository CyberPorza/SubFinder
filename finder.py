import requests
import sys

def finder():
    green = "\033[1;32m"
    red = "\033[1;31m"
    reset = "\033[0m"
    blue = "\033[1;34m"

    banner = r"""
    ______________________________________________________________
    
     ______      __             ____                      
    / ____/_  __/ /_  ___  ____/ __ \____  _____________ _
   / /   / / / / __ \/ _ \/ __/ /_/ / __ \/ ___/_  / __ `/
  / /___/ /_/ / /_/ /  __/ / / ____/ /_/ / /    / /_/ /_/ 
  \____/\__, /_.___/\___/_/ /_/    \____/_/    /___/\__,_/  
       /____/                                              
                        v1.1 - Powered by CyberPorza 🛡️
    ______________________________________________________________
    """
    
    print(green + banner + reset)

    if len(sys.argv) < 2:
        print(red + " [!] Usage: python3 finder.py <target_domain>" + reset)
        print(blue + " Example: python3 finder.py google.com" + reset)
        sys.exit()

    domain = sys.argv[1]
    
    
    subdomains = [
        "www", "mail", "ftp", "localhost", "dev", "test", 
        "admin", "blog", "cpanel", "api", "shop", "staging"
    ]
    
    print(f"{blue} [*] Scanning subdomains for: {domain} ...{reset}")
    print("-" * 62)

    found_count = 0
    try:
        for sub in subdomains:
            url = f"http://{sub}.{domain}"
            try:
                response = requests.get(url, timeout=1)
                if response.status_code < 400:
                    print(f"{green} [+] Found: {url} (Status: {response.status_code}){reset}")
                    found_count += 1
            except requests.ConnectionError:
                pass
            
    except KeyboardInterrupt:
        print(red + "\n [!] Scan interrupted by CyberPorza." + reset)
        sys.exit()

    print("-" * 62)
    print(f"{blue} [*] Scan complete. Found {found_count} subdomains.{reset}")
    print("=" * 62)

if __name__ == "__main__":
    finder()
