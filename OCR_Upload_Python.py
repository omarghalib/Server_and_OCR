import requests


def ocr_space_file(filename, overlay=False, api_key='fe802937b288957', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='fe802937b288957', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


def OCR_Req_name(file_path):
    print("OCR_Req_name")
    output = ocr_space_file(filename=file_path, language='ara')
    start = output.find('"ParsedText":"') + 14
    line_end = output.find('\\')
    line_start = output.find('\\') + 4
    end = output.find('","ErrorMessage":') - 4
    output_text_1 = output[start : line_end]
    output_text_2 = output[line_start : end]
    #print(output)
    return output_text_1,output_text_2

def OCR_Req_number(file_path):
    print("OCR_Req_number")
    output = ocr_space_file(filename=file_path, language='ara')
    start = output.find('"ParsedText":"') + 14
    end = output.find('","ErrorMessage":') - 4
    output_text = output[start : end]
    #print(output)
    return output_text

def OCR_Req_add(file_path):
    print("OCR_Req_add")
    output = ocr_space_file(filename=file_path, language='ara')
    start = output.find('"ParsedText":"') + 14
    line_end = output.find('\\')
    line_start = output.find('\\') + 4
    end = output.find('","ErrorMessage":') - 4
    output_text_1 = output[start : line_end]
    output_text_2 = output[line_start : end]
    #print(output)
    return output_text_1,output_text_2

def convert_nums(string):
    englishNumbersOnly = ""
    arabic = ['٩', '٨', '٧', '٦', '٥', '٤', '٣', '٢', '١','٠'];
    for i in range(len(string)):
        for x in range(10):
            if string[i] == arabic[9 - x]:
                englishNumbersOnly += str(x)
            
    return englishNumbersOnly