# 8wood_crawler
Crawl data product from 8wood.co.id using Scrapy

## Prerequisites

Python 3 and Pip

### Follow the guides below to install Python 3 and pip

1. Linux – [guide](http://docs.python-guide.org/en/latest/starting/install3/linux/).

2. Mac – [guide](http://docs.python-guide.org/en/latest/starting/install3/osx/).

3. Windows – [guide](https://www.scrapehero.com/how-to-install-python3-in-windows-10/).

## How to use

These commands below will help you to use this program properly.

### Install Scrapy

Run `pip3 install scrapy` on your terminal.

### Modify Product Category

The product category is stored on `categories.csv` file. You can find it in `<this project directory>/EightWoodCrawler/resources/categories.csv`.

### Crawling Result

The result of crawling is store  in `<this project directory>/EightWoodCrawler/tmp/filename.extention` for the file result and `<this project directory>/EightWoodCrawler/tmp/images/full` for the downloaded images.

### Using the application

You can  try and debug your code without running the full spider:

```console
scrapy shell <web-page-url>
```

Running the full spider without store the result:

```console
scrapy crawl eightwoodSpider
```

Running the full spider and store the result:

```console
scrapy crawl eightwoodSpider <filename.extention>
```
For example, you can save the file as `<eightwood.xml>`
