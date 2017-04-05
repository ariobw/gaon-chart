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


# Function definition

# Function to scrape overview chart title and contents.
def scrape_chart_all(chartType):
    chartTitle = soup.select('.main{} h3'.format(chartType))
    chartSongElement = soup.select('.main{} .subject'.format(chartType))
    chartSingerElement = soup.select('.main{} .singer'.format(chartType))
    return chartTitle, chartSongElement, chartSingerElement


# Function to scrape digital chart
def scrape_chart_digital(timeSpan):
    # Scrape digital chart url
    response = requests.get(url)
    try:
        response.raise_for_status()
    except HTTPError:
        print('An HTTP Error occurred.')
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    
    # Scrape chart current time
    if timeSpan == 'Yearly':
        time = soup.select('option')[-6].get_text().strip()
    else:
        time = soup.select('option')[1].get_text()

    # Scrape chart content
    # subject = soup.select('.subject')
    # songTitle = soup.select_one('.subject p')
    dataScrape = soup.select('td p')
    songTitleScrape = dataScrape[::4]
    singerAlbumScrape = dataScrape[1::4]
    songProScrape = dataScrape[2::4]
    songDistScrape = dataScrape[3::4]

    # Asks user number of results to be displayed
    resultNumbers = input('Number of results: ')

    # Print chart on display
    songTitle = []
    songSinger = []
    songAlbum = []
    songPro = []
    songDist = []

    print('Gaon {} {} Chart ({})'.format(timeSpan, chartType, time))
    # resultFile.write('GAON {}\n'.format(scrape_chart_all(chartType)[0][0].get_text()))

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


    # Function to scrape download chart
def scrape_chart_download(timeSpan):
    # Scrape download chart url
    response = requests.get(url)
    try:
        response.raise_for_status()
    except HTTPError:
        print('An HTTP Error occurred.')
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    
    # Scrape chart current time
    if timeSpan == 'Yearly':
        time = soup.select('option')[-6].get_text().strip()
    else:
        time = soup.select('option')[1].get_text()

    # Scrape chart content
    # subject = soup.select('.subject')
    # songTitle = soup.select_one('.subject p')
    dataScrape = soup.select('td p')
    songTitleScrape = dataScrape[::5]
    singerAlbumScrape = dataScrape[1::5]
    songCountScrape = dataScrape[2::5]
    songProScrape = dataScrape[3::5]
    songDistScrape = dataScrape[4::5]

    # Asks user number of results to be displayed
    resultNumbers = input('Number of results: ')

    # Print chart on display
    songTitle = []
    songSinger = []
    songAlbum = []
    songCount = []
    songPro = []
    songDist = []

    print('Gaon {} {} Chart ({})'.format(timeSpan, chartType, time))
    # resultFile.write('GAON {}\n'.format(scrape_chart_all(chartType)[0][0].get_text()))

    for name in songTitleScrape:
        songTitle.append(name.get_text())
    for name in singerAlbumScrape:
        songSinger.append(name.get_text().split('|')[0])
    for name in singerAlbumScrape:
        songAlbum.append(name.get_text().split('|')[1])
    for name in songCountScrape:
        songCount.append(name.get_text())
    for name in songProScrape:
        songPro.append(name.get_text().split('|')[0])
    for name in songDistScrape:
        songDist.append(name.get_text().split('|')[0])

    for i in range(int(resultNumbers)):
        # print(str(i+1) + '. ' + songTitle[i] + ' - ' + songSinger[i])
        print('{}. {} - {} - {} - {} - {} - {}'.format(i+1, songTitle[i], songSinger[i], songAlbum[i], songCount[i], songPro[i], songDist[i]))
        # resultFile.write('{}. {} - {}\n'.format(i+1, songTitle[i], songSinger[i]))
    print('\n')


# Function to print and write into file the overview chart in a readable format.
def print_chart_all(chartType):
    songTitle = []
    songSinger = []
    print('\nGAON {}'.format(scrape_chart_all(chartType)[0][0].get_text()))
    resultFile.write('GAON {}\n'.format(scrape_chart_all(chartType)[0][0].get_text()))
    for i in range(len(scrape_chart_all(chartType)[1])):
        for name in scrape_chart_all(chartType)[1]:
            songTitle.append(name.get_text())
        for name in scrape_chart_all(chartType)[2]:
            songSinger.append(name.get_text())
        print('{}. {} - {}'.format(i+1, songTitle[i], songSinger[i]))
        resultFile.write('{}. {} - {}\n'.format(i+1, songTitle[i], songSinger[i]))
    # print('\n')
    resultFile.write('\n')


# Main program

# Asks user of chart type.
print('Select chart type:\n1. Overview\n2. Digital\n3. Download\n4. Streaming\n5. BGM\n6. Mobile\n7. Album\n8. Karaoke\n9. Total\n')
chartType = input('Input number: ')

# Scrape for overview chart
if chartType == '1':
    # Scrape overview chart url
    urlAll = 'http://gaonchart.co.kr'
    responseAll = requests.get(urlAll)
    try:
        responseAll.raise_for_status()
    except:
        print('An HTTP Error occured.')
    soup = bs4.BeautifulSoup(responseAll.text, 'lxml')
    scrapeResult = scrape_chart_all('digital')  # scrape the chart first to get scrape result for text file title

    # Print overview chart
    resultFile = open('gaon_chart_all_{}.txt'. format(scrapeResult[0][0].get_text().split()[2]), 'w', encoding='utf-8')
    print_chart_all('digital')
    print_chart_all('album')
    print_chart_all('social')

# Scrape for digital chart
if chartType == '2':
    chartType = 'Digital'

    # Ask time span
    print('\nSelect time span of chart:\n1. Weekly\n2. Monthly\n3. Yearly')
    timeSpan = input('Input numbers: ')

    if timeSpan == '1':
        timeSpan = 'Weekly'
        url = 'http://gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=week'
        scrape_chart_digital(timeSpan)
    elif timeSpan == '2':
        timeSpan = 'Monthly'
        url = 'http://gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=month'
        scrape_chart_digital(timeSpan)
    elif timeSpan == '3':
        timeSpan = 'Yearly'
        # TODO: year display in yearly chart title, consider searching for 'selected' tag
        url = 'http://gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=year'
        scrape_chart_digital(timeSpan)

# Scrape for download chart
if chartType == '3':
    chartType = 'Download'
    
    # Ask time span
    print('\nSelect time span of chart:\n1. Weekly\n2. Monthly\n3. Yearly')
    timeSpan = input('Input numbers: ')
    
    if timeSpan == '1':
        timeSpan = 'Weekly'
        url = 'http://gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=S1020&termGbn=week'
        scrape_chart_download(timeSpan)
    elif timeSpan == '2':
        timeSpan = 'Monthly'
        url = 'http://gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=S1020&termGbn=month'
        scrape_chart_download(timeSpan)
    elif timeSpan == '3':
        timeSpan = 'Yearly'
        url = 'http://gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=S1020&termGbn=year'
        scrape_chart_download(timeSpan)
 
resultFile.close()
