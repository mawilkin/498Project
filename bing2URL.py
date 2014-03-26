import urllib
import urllib2
import json
import sys

#run program by typing: python bing2URL.py query
#where query is whatever text you want as the query
#example: python bing2URL.py android


#NOTE: this api allows 5,000 calls per month
#To reduce our call usage we should run some queries
#and save the output to .txt files so that we can test our other api's
#on the saved files rather than re-run the query each time we fix a bug
#in another part of our analysis engine.
 
def main():
    #query = "sunshine"
    query = sys.argv[1]
    bing_search(query, 'Web')
    #bing_search(query, 'News')
 
def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= 'Bh66elf50GKt93aa4q6xhkqHnf1wsPphHQhjWMl68Po'
    query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=100&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request) 
    response_data = response.read()
    json_result = json.loads(response_data)
    result_list = json_result['d']['results']
    # for i in result_list:
        # for z in i:
            # if z == 'Url':
                # print i[z]
    lst = list()
    for x in range(len(result_list)):
        lst.append(result_list[x]['Url'])
    return lst
 
if __name__ == "__main__":
    main()