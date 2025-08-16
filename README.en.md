<!-- Language Selection -->
[한국어](README.ko.md) | English

# Selenium Image Crawler for Google Images

This project provides a Python script that leverages Selenium to automate the process of crawling and downloading images from Google Images. It allows users to specify a search query, the number of images to download, and a target directory for saving the images.

## Features

*   **Automated Image Search:** Automatically searches Google Images for a given query.
*   **Dynamic Content Loading:** Scrolls down the page to load more images, handling lazy-loading content.
*   **Configurable Downloads:** Allows specifying the desired number of images to download.
*   **Customizable Output Directory:** Saves downloaded images to a user-defined directory.

## Prerequisites

Before running the script, ensure you have the following installed:

*   **Python 3.x:** The script is written in Python.
*   **pip:** Python package installer (usually comes with Python).
*   **Google Chrome or Chromium Browser:** Selenium requires a web browser to automate.
*   **ChromeDriver:** A WebDriver for Chrome. **It is crucial that the ChromeDriver version matches your Chrome browser version.**

## Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/your-username/selenium-image-crawling.git
    cd selenium-image-crawling
    ```
    (Note: Replace `your-username` with the actual GitHub username if this project is hosted on GitHub.)

2.  **Install Python dependencies:**
    ```bash
    pip install selenium
    ```

## ChromeDriver Setup

1.  **Check your Chrome browser version:**
    Open Chrome, go to `chrome://version/` and note your Chrome version number.

2.  **Download the compatible ChromeDriver:**
    Visit the [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) page. Download the ChromeDriver version that matches your Chrome browser version.

3.  **Place ChromeDriver in your PATH:**
    *   **Linux/macOS:** Move the downloaded `chromedriver` executable to a directory that is in your system's PATH (e.g., `/usr/local/bin`).
        ```bash
        sudo mv /path/to/your/downloaded/chromedriver /usr/local/bin/
        sudo chmod +x /usr/local/bin/chromedriver
        ```
    *   **Windows:** Place `chromedriver.exe` in a directory that is included in your system's PATH environment variable, or place it in the same directory as your `google.py` script.

## Usage

Run the script from your terminal.

```bash
python google.py <search_query> [num_images] [download_directory]
```

**Arguments:**

*   `<search_query>` (required): The keyword(s) to search for on Google Images. Enclose multi-word queries in quotes.
*   `[num_images]` (optional): The maximum number of images to download. If not specified, the script will attempt to download a default number (check `google.py` for the default value, typically around 100).
*   `[download_directory]` (optional): The path to the directory where images will be saved. If not specified, images will be saved in a directory named after the search query within the current working directory.

**Examples:**

1.  **Search for "cats" and download to a default directory:**
    ```bash
    python google.py cats
    ```

2.  **Search for "dogs" and download 50 images:**
    ```bash
    python google.py dogs 50
    ```

3.  **Search for "beautiful landscapes" and save to a specific folder:**
    ```bash
    python google.py "beautiful landscapes" 100 ./my_landscape_images
    ```

## Troubleshooting

*   **`selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.`**
    This error means ChromeDriver is not found. Ensure you have downloaded the correct version and placed it in your system's PATH, or in the same directory as `google.py`.

*   **`selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version XX`**
    This is a version mismatch error. Your ChromeDriver version does not match your Chrome browser version. Download the correct ChromeDriver version.

## Original Guides

*   **Blog Post:** [https://open-support.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C](https://open-support.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C)
*   **YouTube Video:** [https://www.youtube.com/watch?v=1b7pXC1-IbE&list=PLU9-uwewPMe2-vtJAgWB6SNhHcTjJDgEO&index=2](https://www.youtube.com/watch?v=1b7pXC1-IbE&list=PLU9-uwewPMe2-vtJAgWB6SNhHcTjJDgEO&index=2)

## License

This project is licensed under the [LICENSE](LICENSE) file.
