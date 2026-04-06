#Web Crawler
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import json


class LinkParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for (key, value) in attrs:
                if key == "href":
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links.append(newUrl)

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url

        try:
            response = urlopen(url)
            content_type = response.getheader("Content-Type")

            if content_type and "text/html" in content_type:
                htmlBytes = response.read()
                htmlString = htmlBytes.decode("utf-8")
                self.feed(htmlString)
                response.close()
                return htmlString, self.links

        except:
            return "", []

        return "", []


def crawl(url, word):
    foundUrl = []
    visitedURL = []
    numberVisited = 0
    foundWord = False

    parser = LinkParser()
    data, links = parser.getLinks(url)
    links.append(url)

    for link in links:
        if link not in visitedURL:
            numberVisited += 1
            visitedURL.append(link)

            print(numberVisited, "Scanning URL:", link)

            data, li = parser.getLinks(link)

            if word.lower() in data.lower():
                foundWord = True
                foundUrl.append(link)
                print("Word found at:", link)
            else:
                print("Match not found")

    if not foundWord:
        print("The word", word, "was not found!")

    print("Finished, crawled", numberVisited, "pages")
    print(json.dumps(foundUrl, indent=2))


# Use a crawl-friendly site
crawl("https://www.instagram.com", "login")



For Viva -

# 📘 IR Practical Viva Questions (Web Crawling & Link Extraction)

---

## 🔹 1. What is Information Retrieval (IR)?
**Answer:**  
Information Retrieval is the process of collecting and retrieving relevant information from large data sources like the web.

---

## 🔹 2. What is web crawling?
**Answer:**  
Web crawling is the process of automatically browsing the internet to collect data from web pages.

---

## 🔹 3. What is a web crawler?
**Answer:**  
A web crawler is a program that systematically visits web pages and extracts information.

---

## 🔹 4. What is web scraping?
**Answer:**  
Web scraping is extracting specific data from websites.

---

## 🔹 5. Difference between web crawling and web scraping?
**Answer:**  
- Crawling → discovering URLs  
- Scraping → extracting data  

---

## 🔹 6. What is a hyperlink?
**Answer:**  
A hyperlink is a link that connects one webpage to another.

---

## 🔹 7. What is URL?
**Answer:**  
Uniform Resource Locator — the address of a webpage on the internet.

---

## 🔹 8. What is HTML?
**Answer:**  
HTML (HyperText Markup Language) is used to structure web pages.

---

## 🔹 9. What is an HTML parser?
**Answer:**  
A parser extracts and processes elements from HTML documents.

---

## 🔹 10. What is the role of a parser in crawling?
**Answer:**  
To extract links and useful data from HTML content.

---

## 🔹 11. What is link extraction?
**Answer:**  
Extracting URLs from web pages.

---

## 🔹 12. What is a base URL?
**Answer:**  
The main URL used to resolve relative links.

---

## 🔹 13. What are absolute and relative URLs?
**Answer:**  
- Absolute → full URL  
- Relative → partial path  

---

## 🔹 14. What is crawling depth?
**Answer:**  
The level up to which a crawler explores links.

---

## 🔹 15. What is visited URL tracking?
**Answer:**  
Keeping record of visited pages to avoid repetition.

---

## 🔹 16. Why avoid revisiting URLs?
**Answer:**  
To improve efficiency and avoid infinite loops.

---

## 🔹 17. What is data extraction in IR?
**Answer:**  
Retrieving useful information from web content.

---

## 🔹 18. What is keyword searching in crawling?
**Answer:**  
Finding specific words in web page content.

---

## 🔹 19. What is case normalization?
**Answer:**  
Converting text to lowercase or uppercase for consistency.

---

## 🔹 20. What is HTTP request?
**Answer:**  
A request sent to a server to fetch a webpage.

---

## 🔹 21. What is HTTP response?
**Answer:**  
The data returned by the server.

---

## 🔹 22. What is content-type?
**Answer:**  
It specifies the format of data returned (e.g., text/html).

---

## 🔹 23. What is error handling in crawling?
**Answer:**  
Managing failures like broken links or network errors.

---

## 🔹 24. What is scalability in web crawling?
**Answer:**  
Ability to crawl large numbers of web pages efficiently.

---

## 🔹 25. What is politeness policy in crawling?
**Answer:**  
Rules to avoid overloading websites (e.g., delays between requests).

---

## 🔹 26. What is robots.txt?
**Answer:**  
A file that tells crawlers which pages they can or cannot access.

---

## 🔹 27. What is indexing in IR?
**Answer:**  
Organizing data to enable fast search.

---

## 🔹 28. What is search engine?
**Answer:**  
A system that retrieves information from the web.

---

## 🔹 29. What is relevance in IR?
**Answer:**  
How well retrieved data matches the query.

---

## 🔹 30. What is data filtering?
**Answer:**  
Selecting only required information.

---

## 🔹 31. What is JSON format?
**Answer:**  
A lightweight format for storing and exchanging data.

---

## 🔹 32. Why is JSON used?
**Answer:**  
Because it is easy to read and widely supported.

---

## 🔹 33. What is automation in web crawling?
**Answer:**  
Automatically visiting and extracting data from web pages.

---

## 🔹 34. What is domain restriction?
**Answer:**  
Limiting crawling to a specific website.

---

## 🔹 35. What is duplicate content handling?
**Answer:**  
Avoiding repeated data during crawling.

---

## 🔹 36. What is real-world use of web crawling?
**Answer:**  
- Search engines  
- Price comparison sites  
- News aggregation  

---

## 🔹 37. What is data mining?
**Answer:**  
Extracting useful patterns from large datasets.

---

## 🔹 38. What is unstructured data?
**Answer:**  
Data without a fixed format (e.g., web pages).

---

## 🔹 39. What are limitations of web crawling?
**Answer:**  
- Dynamic content issues  
- Legal restrictions  
- Large data handling  

---

## 🔹 40. Why is web crawling important in IR?
**Answer:**  
Because it collects data that is later indexed and searched.

---

## 🔥 Tip for Viva:
If asked **“Explain web crawling in one line”**, say:  
👉 *“Web crawling is the automated process of visiting web pages and extracting links and data for information retrieval.”*

---
