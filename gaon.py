#! python3
# -*- coding: <utf-8> -*-
# gaon.py - Scrape Gaon Music Chart front page

# TO-DO:
# Give user options to choose chart type (full 100) or overview (front page only)
# Save the result in a text file with specific file name
# Give option for number of result in individual chart type
# Print the result in a table-like format with each column header

import requests
import bs4


# Function to scrape chart title and contents.
def scrape_chart(chartType):
    chartTitle = soup.select('.main{} h3'.format(chartType))
    chartSongElement = soup.select('.main{} .subject'.format(chartType))
    chartSingerElement = soup.select('.main{} .singer'.format(chartType))
    return chartTitle, chartSongElement, chartSingerElement


# Function to print and write into file the overview chart in a readable format.
def print_chart_all(chartType):
    songTitle = []
    songSinger = []
    print('\nGAON {}'.format(scrape_chart(chartType)[0][0].get_text()))
    resultFile.write('GAON {}\n'.format(scrape_chart(chartType)[0][0].get_text()))
    for i in range(len(scrape_chart(chartType)[1])):
        for name in scrape_chart(chartType)[1]:
            songTitle.append(name.get_text())
        for name in scrape_chart(chartType)[2]:
            songSinger.append(name.get_text())
        # print(str(i+1) + '. ' + songTitle[i] + ' - ' + songSinger[i])
        print('{}. {} - {}'.format(i+1, songTitle[i], songSinger[i]))
        resultFile.write('{}. {} - {}\n'.format(i+1, songTitle[i], songSinger[i]))
    # print('\n')
    resultFile.write('\n')


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


urlAll = 'http://gaonchart.co.kr'
responseAll = requests.get(urlAll)
responseAll.raise_for_status()

soup = bs4.BeautifulSoup(responseAll.text, 'lxml')

# Asks user of chart type.
print('Select chart type:\n1. Overview\n2. Digital\n3. Download\n4. Streaming\n5. BGM\n6. Mobile\n7. Album\n8. Karaoke\n9. Total\n')
chartType = input('Input number: ')

if chartType == '1':
    scrapeResult = scrape_chart('digital')  # scrape the chart to get scrape result for text file title
    resultFile = open('gaon_chart_all_{}.txt'. format(scrapeResult[0][0].get_text().split()[2]), 'w', encoding='utf-8')
    print_chart_all('digital')
    print_chart_all('album')
    print_chart_all('social')
# else:
    # scrapeResult = scrape_chart(chartType)
    # resultFile = open('gaon_chart_{}_{}.txt'. format(chartType, scrapeResult[0][0].get_text().split()[2]), 'w', encoding='utf-8')
    # print_chart(chartType)


# Scrape for weekly digital chart.
if chartType == 'digital':
    print('\nSelect time span of chart:\n1. Weekly\n2. Monthly\n3. Yearly')
    timeSpan = input('Input numbers: ')
    if timeSpan == 'weekly':
        # Scrape weekly digital chart url
        urlDigitalWeekly = 'http://gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=week'
        responseDigitalWeekly = requests.get(urlDigitalWeekly)
        responseDigitalWeekly.raise_for_status()
        soupDigitalWeekly = bs4.BeautifulSoup(responseDigitalWeekly.text, 'lxml')

        # Scrape time span
        time = soupDigitalWeekly.select('option')[1].get_text()

        # Scrape chart content
        # subject = soupDigitalWeekly.select('.subject')
        # songTitle = soupDigitalWEekly.select_one('.subject p')
        dataScrape = soupDigitalWeekly.select('td p')
        songTitleScrape = dataScrape[::4]
        singerAlbumScrape = dataScrape[1::4]
        songProScrape = dataScrape[2::4]
        songDistScrape = dataScrape[3::4]

        # Print chart on display
        songTitle = []
        songSinger = []
        songAlbum = []
        songPro = []
        songDist = []

        #Asks user number of results to be displayed
        resultNumbers = input('Number of results: ')
        
        print('Gaon {} {} Chart ({})'.format(timeSpan, chartType, time))
        # resultFile.write('GAON {}\n'.format(scrape_chart(chartType)[0][0].get_text()))
        
        for name in songTitleScrape:
            songTitle.append(name.get_text())
        for name in singerAlbumScrape:
            songSinger.append(name.get_text().split('|')[0])
        for name in singerAlbumScrape:
            songAlbum.append(name.get_text().split('|')[1])
        for name in songProScrape:
            songPro.append(name.get_text().split('|')[0])
        for name in songDistScrape:
            songDist.append(name.get_text().split('|')[0])
            
        for i in range(int(resultNumbers)):
            # print(str(i+1) + '. ' + songTitle[i] + ' - ' + songSinger[i])
            print('{}. {} - {} - {} - {} - {}'.format(i+1, songTitle[i], songSinger[i], songAlbum[i], songPro[i], songDist[i]))
            # resultFile.write('{}. {} - {}\n'.format(i+1, songTitle[i], songSinger[i]))
        print('\n')

resultFile.close()
