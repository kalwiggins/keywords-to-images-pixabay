import requests
from PIL import Image
from io import BytesIO
import os
import time
import warnings
from dotenv import load_dotenv

# Suppress all warnings (including SSL warnings)
warnings.simplefilter('ignore')

# Load environment variables from .env file
load_dotenv()
PIXABAY_API_KEY = os.getenv('PIXABAY_API_KEY')

def resize_and_crop_image(url, target_size, save_path):
    """Resize and crop an image from a given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        # Resize image maintaining aspect ratio
        image_ratio = image.width / image.height
        new_width = target_size[0]
        new_height = int(new_width / image_ratio)
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        # Crop the image
        top = (new_height - target_size[1]) / 2
        bottom = top + target_size[1]
        image = image.crop((0, top, new_width, bottom))
        # Save the image
        if not os.path.exists('images'):
            os.makedirs('images')
        image.save(save_path, 'PNG')
        return save_path
    return None

def generate_filename(base_path, description, pixabay_id, ext='.png'):
    """Generate a filename for an image."""
    safe_description = description.replace(' ', '_').replace('"', '').replace("'", '')
    return f"{base_path}/{safe_description}-pixabay-{pixabay_id}{ext}"

def fetch_images_from_pixabay(description, per_keyword=20):
    """Fetch images from Pixabay API for a given description."""
    url = "https://pixabay.com/api/"
    params = {
        "key": PIXABAY_API_KEY,
        "q": description,
        "image_type": "photo",
        "per_page": min(per_keyword, 20)
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return [(img['webformatURL'], img['id']) for img in response.json().get('hits', [])]
    else:
        print(f"Failed to fetch images for '{description}'. HTTP Status: {response.status_code}")
        return []

def process_images(descriptions, size=(1200, 628), per_keyword=1, rate_limit=100):
    """Process images fetched from Pixabay for given descriptions."""
    results = {}
    fetched_image_ids = set()
    for description in descriptions:
        images = fetch_images_from_pixabay(description, per_keyword)
        image_paths = []
        for image_url, pixabay_id in images:
            if pixabay_id not in fetched_image_ids:
                save_path = generate_filename('images', description, pixabay_id)
                resized_path = resize_and_crop_image(image_url, size, save_path)
                if resized_path:
                    image_paths.append(resized_path)
                    fetched_image_ids.add(pixabay_id)
        results[description] = image_paths
        time.sleep(60 / rate_limit)  # Enforce rate limit
    return results

if __name__ == "__main__":
    # User input for image descriptions
    user_input = input("Enter image descriptions, separated by commas: ")
    descriptions = [desc.strip() for desc in user_input.split(',')]
    
    # User input for crop size
    crop_size_input = input("Enter crop size as 'width x height' (default 1200x628): ")
    crop_size = tuple(map(int, crop_size_input.split('x'))) if 'x' in crop_size_input else (1200, 628)
    
    # User input for number of images per keyword
    num_images_input = input("Enter number of images per keyword (default 1, max 20): ").strip()
    num_images = min(int(num_images_input), 20) if num_images_input.isdigit() else 1

    # Fetch, process, and display images
    images = process_images(descriptions, size=crop_size, per_keyword=num_images)
    print(images)
