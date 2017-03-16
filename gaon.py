#! python3
# -*- coding: <utf-8> -*-
# gaon.py - Scrape Gaon Music Chart front page

# TO-DO:
# Give user options to choose chart type (full 100) or all (front page only)
# Save the result in a text file with specific file name
# Give option for number of result in individual chart type
# Print the result in a table-like format with each column header

import requests
import bs4


url = 'http://gaonchart.co.kr'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')


# Function to scrape chart title and contents.
def scrape_chart(chartType):
    chartTitle = soup.select('.main{} h3'.format(chartType))
    chartSongElement = soup.select('.main{} .subject'.format(chartType))
    chartSingerElement = soup.select('.main{} .singer'.format(chartType))
    return chartTitle, chartSongElement, chartSingerElement


# Function to print the chart in readable format.
def print_chart(chartType):
    songTitle = []
    songSinger = []
    print('GAON {}'.format(scrape_chart(chartType)[0][0].get_text()))
    resultFile.write('GAON {}\n'.format(scrape_chart(chartType)[0][0].get_text()))
    for i in range(len(scrape_chart(chartType)[1])):
        for name in scrape_chart(chartType)[1]:
            songTitle.append(name.get_text())
        for name in scrape_chart(chartType)[2]:
            songSinger.append(name.get_text())
        # print(str(i+1) + '. ' + songTitle[i] + ' - ' + songSinger[i])
        print('{}. {} - {}'.format(i+1, songTitle[i], songSinger[i]))
        resultFile.write('{}. {} - {}\n'.format(i+1, songTitle[i], songSinger[i]))
    print('\n')


# Asks user of chart type.
print('Please input Gaon chart type:\n[e.g. all/digital/album/social]')
chartType = input()

# Scrape the chart to get scrape result for text file title.
scrapeResult = scrape_chart(chartType)

if chartType == 'all':
    scrapeResult = scrape_chart('digital')
    print_chart('digital')
    print_chart('album')
    print_chart('social')
else:
    #Create text file to save the chart.
    resultFile = open('gaon_chart_{}_{}.txt'. format(chartType, scrapeResult[0][0].get_text().split()[2]), 'w', encoding='utf-8')
    print_chart(chartType)


resultFile.close()
