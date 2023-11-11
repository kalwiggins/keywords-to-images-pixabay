# Python Image Fetching and Processing Script

This Python script automates the task of fetching images from Pixabay based on user-defined keywords, resizing, and cropping them to a specified size. It is designed to be user-friendly, allowing input directly through the command line.

## Features

- Fetch images from Pixabay using their API.
- Resize and crop images to user-specified dimensions.
- Save images locally in a designated folder.
- Handle rate limiting to comply with Pixabay's API usage policies.
- User input for search keywords, number of images, and image size.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- `PIL` (Pillow) library installed for image processing.
- `requests` library installed for making API requests.
- A Pixabay API key. You can obtain it by [signing up on Pixabay](https://pixabay.com/accounts/register/).

## Installation and Setup

1. Clone the repository or download the script to your local machine.
2. Install the required Python packages:
        pip3 install pillow requests
3. Create a `.env` file in the project directory and add your Pixabay API key:
        PIXABAY_API_KEY=your_api_key_here
4. Run the script using Python:
        python3 script_name.py

## Usage

After running the script, follow the on-screen prompts:

1. Enter the image descriptions separated by commas.
2. Enter the desired crop size (width x height).
3. Enter the number of images you want to fetch for each keyword.

The script will process the images and save them in the `images` directory within your project folder.

## Contributing

Contributions to this project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5. Push to the branch (`git push origin feature/AmazingFeature`).
6. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Kal Wiggins
Epic Design Labs
kal@epicdesignlabs.com
Project Link: [GitHub Project Link]
