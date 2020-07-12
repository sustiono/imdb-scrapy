# IMDB Scrapy

Scrap best movies from https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc using Scrapy

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some packages needed.

```bash
git clone git@github.com:sustiono/imdb-scrapy.git
cd imdb-scrapy
pip3 install virtualenv
virtualenv .env
source .env/bin/activate
cd imdb
pip install -r requirements.txt
```

## Usage
Choose one of the commands below to get the results in the desired format

```bash
scrapy crawl best_movies -o best_movies.csv
scrapy crawl best_movies -o best_movies.json
scrapy crawl best_movies -o best_movies.xml
```
