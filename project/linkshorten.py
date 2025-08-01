import pyshorteners
import requests
import qrcode
from tkinter import Tk, Label
from PIL import ImageTk

def optionalqrcode(link): # This is an optional function to generate a QR code for the shortened or real link which is tricky to test using pytest

    # Create a Tkinter root window to show up when user want a QR code

    user = input("\nDo you want to generate a QR code for this link? ('Y' for Yes or any key for No)\n").lower().strip()

    if user == "y":
        root = Tk()
        root.title("QR Code")

        # Generate the QR code
        qr = qrcode.QRCode(
            version=10,  # Controls the size of the QR Code (1 to 40)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=5,  # Size of each box in the QR code grid
            border=4,  # Border size (minimum is 4)
        )
        qr.add_data(link)
        qr.make(fit=True)

        # Create an image of the QR Code
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert the QR code to a format compatible with Tkinter
        img = ImageTk.PhotoImage(img)  # No error here because the Tk root is already initialized

        # Display the QR code in the Tkinter window
        label = Label(root, image=img)
        label.pack()

        root.attributes("-topmost", 1) # to make the QR code appear above all other tabs

        # Run the Tkinter event loop
        root.mainloop()

    else:
        pass

def link_shortener(link):
    try:
        shortener = pyshorteners.Shortener()  # class object
        short_link = shortener.tinyurl.short(link)  # shorting the link
        # Display
        return (f"{short_link}")
        
    except Exception as e:
        return ("Something went wrong!")
        
def link_opener(link):
    try:
        # Add headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        response = requests.get(link, headers=headers, allow_redirects=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        real_link = response.url  # Get the final URL after redirects
        return f'{real_link}'
       
        
    except requests.exceptions.RequestException as e:
        return (f"\nSomething went wrong! Error: {e}")

def main():
    # Added a loop to reprompt user when they entered a different option than the ones given
    while True:
        num = input("\nEnter your choice below:\n"
                    "1. Type 1 for shortening link\n"
                    "2. Type 2 for extracting real link from a shorten link\n"
                    "Your input: ").strip() # Rearrange some typo

        # Rearranged the structure from the original code for more convenience

        if num != '1' and num != '2':
            print("Please select a choice between '1' and '2' only!\n")  # added a reprompt if user enter anything else other than 1 and 2
            continue

        else:
            link = input("Enter the link: ").strip()

            if num == '1':
                short_link = link_shortener(link)
                print(f"\n[+] Shortened Link:+ {short_link}")
                optionalqrcode(short_link)

            else:
                real_link = link_opener(link)
                print(f"\n[+] Real Link: {real_link}")
                optionalqrcode(real_link)

            break

if __name__ == '__main__':
    main()





