import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Send prompt to MiniVault API")
    parser.add_argument("prompt", type=str, help="Prompt to send")
    args = parser.parse_args()

    response = requests.post("http://localhost:8000/generate", json={"prompt": args.prompt})

    print ("Response:\n")
    print (response.text)

if __name__ == "__main__":
    main()