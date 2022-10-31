## Import required packages
from google_images_search import GoogleImagesSearch
import os
import requests
import urllib.request
import os
from serpapi import GoogleSearch
from simple_image_download import simple_image_download as simp 
import sys
import ast


## Functions to search for given # of images from three different sources

def Google_image_search(keyword, no_of_images):
    
    # you can provide API key and CX using arguments,
    # or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
    gis = GoogleImagesSearch(os.environ['GCS_DEVELOPER_KEY'], os.environ['GCS_CX'])

    # define search params:
    _search_params = {
        'q': keyword, ## Keywords
        'num': no_of_images ## Total no of images to search
        ## Can uncomment these parameters for more specific search
        #'safe': 'high',
        #'fileType': 'jpg|gif|png'
        # 'imgSize': 'HUGE',
        # 'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
    }
    
    # this will search for specified no of images for the keyword
    try:
        gis.search(search_params=_search_params)
    except:
        print('Some error with GoogleImagesSearch...')
    return gis

def serp_image_search(keyword):

    params = {
    "q": keyword,  ## query (one keyword at a time)
    "tbm": "isch",  ## image search engine
    "ijn": "0",  ##Page number to get (must be greater than or equal to 0)
    "api_key": os.getenv("SERPAPI_KEY")  ## Store your SERP API key as an environment variable
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    serp_results = results['images_results']

    return serp_results

def simple_image_search(keyword, no_of_images):

    response = simp.simple_image_download
    simple_results = response().urls(keyword, no_of_images)
    return simple_results

def main(keyword_list, path, no_of_images):
    # Define the path you want to store your images to
    #path = '/Users/rmakhija/Documents/image-search/images' ### Change the path to where you want your images to be downloaded

    #keyword_list = ['"data-mapping"']
    #no_of_images = 50

    for keyword in keyword_list:
        keyword = '"' + keyword + '"'
        print('Seaching images for keyword: ', keyword)

        # Check whether the specified path with the keyword folder exists or not
        isExist = os.path.exists(path + '/' + keyword)

        if not isExist:
            # Create a new directory because it does not exist 
            os.makedirs(path + '/' + keyword)
        gis_results = Google_image_search(keyword, no_of_images)
        serp_results = serp_image_search(keyword)
        simple_urls= simple_image_search(keyword, no_of_images)

        gis_urls = []
        serp_urls = []
        for result in gis_results.results():
            gis_urls.append(result.url)
        for image in serp_results:
            if 'original' in image.keys():
                serp_urls.append(image['original'])

        common_urls = []
        for url in simple_urls:
            if (url in serp_urls) and (url in gis_urls):
                common_urls.append(url)
        i = 1
        for image in gis_results.results():
            if image.url in common_urls:
                image.download(path + '/' + keyword)
                i += 1

        print('Total %i common images found for keyword %s after searching for %i images from each source. Images downloaded to the path: %s' %(i, keyword,  no_of_images, path))

if __name__ == "__main__":
    keyword_list = ast.literal_eval(sys.argv[1])
    path = sys.argv[2]
    no_of_images = int(sys.argv[3])

    main(keyword_list, path, no_of_images)