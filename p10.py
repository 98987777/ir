import csv  # Used to read/write CSV files
import requests  # Used to send HTTP requests (fetch RSS feed)
import xml.etree.ElementTree as ET  # Used to parse XML data

# Load RSS feed
def load_rss(url, filename):
    resp = requests.get(url)  # Send GET request to fetch RSS feed from URL
    with open(filename, 'wb') as f:  # Open file in write-binary mode
        f.write(resp.content)  # Write fetched XML content into file
    print(f"RSS feed loaded and saved to '{filename}'.")  # Print confirmation

# Parse XML and extract items
def parse_xml(xmlfile):
    tree = ET.parse(xmlfile)  # Parse XML file into tree structure
    root = tree.getroot()  # Get root element of XML
    newsitems = []  # List to store extracted news data

    allowed_fields = {'guid', 'title', 'pubDate', 'description', 'link'}  
    # Set of required fields to extract

    for item in root.findall('.//item'):  # Find all <item> tags in XML
        news = {}  # Dictionary to store single news item

        for child in item:  # Loop through each child tag inside item
            tag = child.tag.split('}')[-1]   # Remove namespace (if present)

            # keep only required fields
            if tag in allowed_fields:  # Check if tag is needed
                news[tag] = child.text  # Store tag text in dictionary

            # handle media content if present
            if tag == 'content' and 'url' in child.attrib:  
                news['media'] = child.attrib['url']  
                # Extract media URL if available in attributes

        newsitems.append(news)  # Add news dictionary to list

    return newsitems  # Return list of news items

# Save to CSV
def save_to_csv(newsitems, filename):
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']  
    # Define CSV column headers

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:  
        # Open CSV file in write mode with UTF-8 encoding
        writer = csv.DictWriter(csvfile, fieldnames=fields)  
        # Create CSV writer object with field names
        writer.writeheader()  # Write header row in CSV
        writer.writerows(newsitems)  # Write all news data rows

    print(f"Data saved to '{filename}'.")  # Print confirmation

# Main function
def main():
    # Choose any one RSS link
    rss_url = 'http://feeds.bbci.co.uk/news/rss.xml'  
    # RSS feed URL (BBC News)
    # rss_url = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'
    # rss_url = 'https://feeds.feedburner.com/50WordStories'

    xml_filename = 'news.xml'  # File to store downloaded XML
    csv_filename = 'news.csv'  # File to store processed CSV

    load_rss(rss_url, xml_filename)  # Download and save RSS feed
    newsitems = parse_xml(xml_filename)  # Parse XML and extract data
    save_to_csv(newsitems, csv_filename)  # Save extracted data to CSV

if __name__ == "__main__":  # Check if script is run directly
    main()  # Call main function










For Viva -

# 📘 IR Practical Viva Questions (RSS Feed & XML Parsing)

---

## 🔹 1. What is Information Retrieval (IR)?

**Answer:**
Information Retrieval is the process of collecting and retrieving relevant information from large data sources like the web.

---

## 🔹 2. What is web data extraction?

**Answer:**
It is the process of automatically collecting data from websites or online sources.

---

## 🔹 3. What is an RSS feed?

**Answer:**
An RSS (Really Simple Syndication) feed is a format used to publish frequently updated content like news in XML format.

---

## 🔹 4. Why are RSS feeds used?

**Answer:**
To easily access and distribute updated content without visiting the website repeatedly.

---

## 🔹 5. What is XML?

**Answer:**
XML (Extensible Markup Language) is a structured format used to store and transport data.

---

## 🔹 6. Difference between XML and HTML?

**Answer:**

* XML → stores data
* HTML → displays data

---

## 🔹 7. What is parsing in IR?

**Answer:**
Parsing is the process of analyzing structured data (like XML) to extract useful information.

---

## 🔹 8. What is a parser?

**Answer:**
A parser is a tool or program that reads structured data and extracts meaningful content.

---

## 🔹 9. What is structured data?

**Answer:**
Data organized in a predefined format (like XML, JSON).

---

## 🔹 10. What are tags in XML?

**Answer:**
Tags define elements in XML and enclose data (e.g., `<title>`).

---

## 🔹 11. What is a root element?

**Answer:**
The top-level element that contains all other elements in XML.

---

## 🔹 12. What is an attribute in XML?

**Answer:**
Additional information inside a tag (e.g., `<tag attr="value">`).

---

## 🔹 13. What is web scraping?

**Answer:**
Extracting data from websites automatically using programs.

---

## 🔹 14. Difference between web scraping and RSS feeds?

**Answer:**

* RSS → structured and easy to parse
* Scraping → extracts data from HTML (more complex)

---

## 🔹 15. What is a URL?

**Answer:**
Uniform Resource Locator — the address of a resource on the internet.

---

## 🔹 16. What is HTTP request?

**Answer:**
A request sent from client to server to fetch data.

---

## 🔹 17. What is HTTP response?

**Answer:**
The data returned by the server after a request.

---

## 🔹 18. What is data preprocessing?

**Answer:**
Cleaning and organizing data before using it.

---

## 🔹 19. What is a dataset?

**Answer:**
A collection of structured data used for analysis.

---

## 🔹 20. What is CSV format?

**Answer:**
Comma-Separated Values — a simple file format for storing tabular data.

---

## 🔹 21. Why is CSV used in IR?

**Answer:**
Because it is lightweight, easy to store, and compatible with many tools.

---

## 🔹 22. What is data extraction pipeline?

**Answer:**
A sequence of steps to collect, process, and store data.

---

## 🔹 23. What is automation in data retrieval?

**Answer:**
Automatically fetching and processing data without manual effort.

---

## 🔹 24. What is real-time data retrieval?

**Answer:**
Fetching data as soon as it is updated.

---

## 🔹 25. What is metadata?

**Answer:**
Data that describes other data (e.g., publication date of news).

---

## 🔹 26. What are common fields in RSS feeds?

**Answer:**

* Title
* Description
* Link
* Publication date

---

## 🔹 27. What is data filtering?

**Answer:**
Selecting only required data from a dataset.

---

## 🔹 28. What is data storage?

**Answer:**
Saving extracted data for future use.

---

## 🔹 29. What is encoding in data?

**Answer:**
The format used to represent characters (e.g., UTF-8).

---

## 🔹 30. Why is encoding important?

**Answer:**
To correctly display special characters and avoid errors.

---

## 🔹 31. What is scalability in data extraction?

**Answer:**
Ability to handle large amounts of data efficiently.

---

## 🔹 32. What is data consistency?

**Answer:**
Ensuring data remains accurate and uniform.

---

## 🔹 33. What is error handling?

**Answer:**
Managing errors during data retrieval or processing.

---

## 🔹 34. What is namespace in XML?

**Answer:**
A way to avoid tag name conflicts in XML.

---

## 🔹 35. What is hierarchical structure in XML?

**Answer:**
Data organized in parent-child relationships.

---

## 🔹 36. What is API vs RSS?

**Answer:**

* API → more flexible, dynamic
* RSS → simple, read-only feed

---

## 🔹 37. What is data transformation?

**Answer:**
Converting data from one format to another (XML → CSV).

---

## 🔹 38. What is the role of IR in news aggregation?

**Answer:**
To collect, organize, and present relevant news efficiently.

---

## 🔹 39. What are advantages of RSS-based IR systems?

**Answer:**

* Easy access to updates
* Structured data
* Low complexity

---

## 🔹 40. What are limitations of RSS feeds?

**Answer:**

* Limited information
* Not all websites provide RSS
* No customization

---

## 🔥 Tip for Viva:

If asked **“Explain your practical”**, say:
👉 *“This practical demonstrates web-based information retrieval using RSS feeds, where structured XML data is extracted, parsed, filtered, and stored in CSV format for further analysis.”*

---
