# image-search

## Python code to search and download common images for different keywords using 3 different sources/API's as mentioned:

Follow the steps below to setup accounts for the sources and get the credentials
1. Google-Images-Search API

- Visit https://console.developers.google.com and cretae a project. <br>
- Visit https://console.developers.google.com/apis/library/customsearch.googleapis.com and enable "Custom Search API" for your project.<br>
- Visit https://console.developers.google.com/apis/credentials and generate API key credentials for your project.<br>
- Visit https://cse.google.com/cse/all and in the web form where you create/edit your custom search engine enable "Image search" option and for "Sites to search" option select "Search the entire web but emphasize included sites".<br><br>

  After setting up your Google developers account and project you should have been provided with developers API key and project CX. Set thoe keys as environment variables: GCS_DEVELOPER_KEY, GCS_CX or add the to the python code in the google_image_search function.

2. SERP API

- Go to https://serpapi.com/dashboard and set upo your user account and credentials. You will have your SerpAPI key which you can use as an argument or store it as an environment variable.

3. simple-image-download by PyPI

  Refernce link: https://pypi.org/project/simple-image-download/


  After setting up accounts and credentials follow the steps below to run the code and download the images using the command line or the terminal:


1. Clone the repository using command line to the local working directory:
```
git clone https://github.com/Lucy-Family-Institute/image-search.git
```

2. Go to the working directory:
```
cd image-search
```

3. Checkout branch updated-image-serach using:
```
git checkout updated-image-search
```

4. Create a virtual environment and install the requirements:

```
pip install -r requirements.txt
```
5. Run the python script:
-Requires three arguments as shown in the example below:
  -list of keywords: '['data-mapping', 'data-pipeline']'
  -path: 'images' # Creates a folder named images in the working directory
  -no_of_images: 50 # Total images to search for(about 50 to download atleast 20-25 common images)

```
python image-search.py '['data-mapping', 'data-pipeline']' 'images' 50
```
