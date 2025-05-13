import os

def main():
    name = os.getenv('USER_NAME', 'Unknown')
    age = os.getenv('USER_AGE', '0')
    
    print(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    main()
