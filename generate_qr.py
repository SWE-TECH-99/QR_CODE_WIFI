import os
import wifi_qrcode_generator.generator
from dotenv import load_dotenv
import json
from PIL import Image
import logging

# Set up logging for better feedback
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Retrieve Wi-Fi networks, password, and save directory from environment variables
try:
    wifi_networks = json.loads(os.getenv("WIFI_NETWORKS"))
    wifi_password = os.getenv("WIFI_PASSWORD")
    save_directory = os.getenv("SAVE_DIRECTORY")
    
    if not wifi_networks or not wifi_password or not save_directory:
        raise ValueError("Wi-Fi networks, password, or save directory not found in .env file.")
except Exception as e:
    logging.error(f"Error loading environment variables: {e}")
    exit(1)

# Ensure the directory exists, create if necessary
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
    logging.info(f"Directory {save_directory} created.")

def generate_wifi_qr_code(ssid, password, directory):
    """
    Generate a QR code for the given Wi-Fi network and save it to the specified directory.
    """
    try:
        # Generate QR code with correct authentication type
        qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
            ssid=ssid, 
            hidden=False, 
            authentication_type='WPA',  # Ensure your network uses WPA or WPA2
            password=password
        )
        
        # Convert to PIL Image and save the QR code as an image file
        img = qr_code.make_image(fill="black", back_color="white")
        img_path = os.path.join(directory, f'{ssid}_wifi_qrcode.png')

        # Check if file already exists
        if os.path.exists(img_path):
            logging.warning(f"File {img_path} already exists.")
            overwrite = input(f"Do you want to overwrite {img_path}? (y/n): ").lower()
            if overwrite != 'y':
                logging.info(f"Skipping {ssid}")
                return

        # Save the image
        img.save(img_path)
        logging.info(f"QR code generated for {ssid} and saved to {img_path}")
        
    except Exception as e:
        logging.error(f"Failed to generate QR code for {ssid}: {e}")

# Generate QR codes for all Wi-Fi networks
for ssid in wifi_networks:
    generate_wifi_qr_code(ssid, wifi_password, save_directory)

logging.info("QR code generation process completed.")
