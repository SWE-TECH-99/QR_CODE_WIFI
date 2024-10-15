# Wi-Fi QR Code Generator

This project generates QR codes for Wi-Fi networks, allowing easy connection to specified networks by scanning the generated QR codes.

## Instructions to Run the Wi-Fi QR Code Generator

Follow these steps to set up and run the Wi-Fi QR code generator script:

### 1. Clone the Repository

First, clone the GitHub repository to your local machine:

```bash
git clone https://github.com/SWE-TECH-99/QR_CODE_WIFI.git
```

Navigate into the cloned repository directory:

```bash
cd QR_CODE_WIFI
```

### 2. Install the Required Python Libraries

Install the necessary Python packages by running the following command:

```bash
pip install -r requirements.txt
```

This will install libraries such as `qrcode`, `Pillow`, `python-dotenv`, and `wifi-qrcode-generator`.

### 3. Set Up the `.env` File

Create a `.env` file in the root directory of the project and add your Wi-Fi network names and password in the following format:

```
WIFI_NETWORKS=["Your_SSID_1", "Your_SSID_2", "Your_SSID_3"]
WIFI_PASSWORD=your_wifi_password
SAVE_DIRECTORY=C:\path\to\save\qr_codes
```

Make sure to replace `Your_SSID_1`, `Your_SSID_2`, `your_wifi_password`, and `C:\path\to\save\qr_codes` with your actual Wi-Fi network names, password, and the desired save location for the QR code images.

### 4. Run the Script

To generate the Wi-Fi QR codes, run the Python script:

```bash
python generate_qr.py
```

The script will generate QR codes for each Wi-Fi network specified in the `.env` file and save them in the directory you provided in the `SAVE_DIRECTORY` field.

### 5. Scan the QR Code

After running the script, go to the directory where the QR codes are saved and either display or print the images. You can now use any phone to scan the QR code to automatically connect to the respective Wi-Fi network.

### 6. Customizations

- **Adding More Networks**: To add more Wi-Fi networks, update the `WIFI_NETWORKS` array in the `.env` file with additional SSIDs.
- **Changing the Save Directory**: Modify the `SAVE_DIRECTORY` field in the `.env` file to change where the QR code images are saved.

That's it! Your QR codes will be generated and ready to use.

## Need Help?

If you need further assistance, please open an issue in the GitHub repository or contact the project maintainers.
