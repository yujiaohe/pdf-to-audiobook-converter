# PDF to Audiobook Converter

This is a web application that allows you to convert a PDF file into an audiobook in your desired language. Simply upload a PDF file, select the language for the audiobook, and the application will generate an MP3 file that you can download and listen to.

## Features

- Upload a PDF file for conversion.
- Choose the language for the audiobook.
- Automatically extract the text from the PDF.
- Convert the text to speech using the selected language.
- Generate an MP3 file of the audiobook.
- Download the audiobook file.

## Installation

1. Clone this repository to your local machine.

2. Navigate to the project directory

3. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the `main.py` file to start the application:

2. Open your web browser and navigate to `http://localhost:5000` to access the application.

3. Choose a PDF file using the file upload form.

4. Select the language for the audiobook from the available options.

5. Click the "Submit" button to start the conversion process.

6. Wait for the conversion to complete. Once done, the audiobook file will be automatically downloaded.

7. Enjoy listening to your audiobook!

Note: Make sure you have an active internet connection during the conversion process as the `gtts` library requires an internet connection to fetch the required language files.

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.