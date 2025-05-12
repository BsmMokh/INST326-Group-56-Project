"""
Minecraft Resource Guide

A program that helps players find information about Minecraft resources,
including where to find them and what tools are needed to obtain them.
"""

from minecraft_resources import load_resources, find_resource_info

def display_banner():
    """Display a Minecraft Resource Guide Banner"""
    banner = """
     _  _  __  __ _  ____  ___  ____   __   ____  ____                            
( \/ )(  )(  ( \(  __)/ __)(  _ \ / _\ (  __)(_  _)                           
/ \/ \ )( /    / ) _)( (__  )   //    \ ) _)   )(                             
\_)(_/(__)\_)__)(____)\___)(__\_)\_/\_/(__)   (__)                            
 ____  ____  ____   __   _  _  ____   ___  ____     ___  _  _  __  ____  ____ 
(  _ \(  __)/ ___) /  \ / )( \(  _ \ / __)(  __)   / __)/ )( \(  )(    \(  __)
 )   / ) _) \___ \(  O )) \/ ( )   /( (__  ) _)   ( (_ \) \/ ( )(  ) D ( ) _) 
(__\_)(____)(____/ \__/ \____/(__\_) \___)(____)   \___/\____/(__)(____/(____)
    """
    print(banner)

def main():
    display_banner()
    print("Welcome to the Minecraft Resource Guide!")
    print("This program will tell you where to find resources and what tools you need.")
    print("Type 'exit' to quit the program.\n")
    
    # Load the resources from the CSV file
    try:
        resources = load_resources('minecraft_ores.csv')
    except FileNotFoundError:
        print("Error: Could not find the resource data file.")
        return
    except ValueError as e:
        print(f"Error: {str(e)}")
        return
    
    while True:
        # Get user input
        resource_name = input("\nEnter the name of the resource you want to find (e.g., 'Diamond Ore'): ")
        
        # Check if user wants to exit
        if resource_name.lower() == 'exit':
            print("\nThanks for using the Minecraft Resource Guide!")
            break
        
        # Get and display the resource information
        info = find_resource_info(resource_name, resources)
        print("\n" + info)
        
        # Show available resources if the requested one wasn't found
        if info == "Resource not found.":
            print("\nAvailable resources:")
            for resource in resources:
                print(f"- {resource.name}")

if __name__ == "__main__":
    main() 