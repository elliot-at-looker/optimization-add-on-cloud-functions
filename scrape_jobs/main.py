
# Import the beautifulsoup 
# and request libraries of python.
import requests
import bs4
  
# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
text= "software+engineer+nyc"
url = 'https://google.com/search?q=' + text
# https://www.google.com/search?q=software+engineer+nyc
# print(url)
# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url )
  
# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text,
                         "html.parser")
# print(soup)


# soup.find.all( h3 ) to grab 
# all major headings of our search result,
heading_object=soup.find_all( 'a' )
  
# Iterate through the object 
# and print it as a string.
for info in heading_object:
    print(info.getText())
    print("------")