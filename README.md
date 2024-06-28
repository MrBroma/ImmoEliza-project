# ImmoEliza-project
   - Description

   This is a project to obtain real estate data information in Belgium from the real estate website Immoweb. We intend to collect information from at least 10.000 properties.

   - Installation

    To run the code requires to install python and clone the repository

   - Usage
    
    This code allows to obtain a csv file with multiple details from houses available in the Belgiam real estate market

   - (Visuals)

   - (Contributors)
   Loic
   Ridvan
   Georgina

   - (Timeline)

    Monday 24, 2024: overview of web scraping and data collection
    Tuesday 25, 20024: scraping the website with cloudscraper and creating a loop for getting all webpages with the information using BeautifulSoup
    Wednesday 26, 2024: getting the information listed with json, selectolax, chompjs
    Thursday 27, 2024: organizing both, the list of properties information and the list of web pages.
    Fridya 28, 2024: Getting the code into a programming object to get a csv file with pandas

   - (Personal situation)

    When we first started this project, we didn't know much about how to scrape websites. But now, we have some great tools that help us do it more efficiently!

3. Small presentation :
   - How you did it ?
   
   We did a first search of each task to complete and then share what we where finding for each task

   - Who did what ?

   Loic:
   Started with the list of webpage collection and then found a way to list all the information with json. Then, he found that with selectolax and chompjs it was easier to collect the website information and prepared a line of commands to do one by one. He merged the two loops for getting list of websites and information into a programming object to finally obtain a csv file with pandas.

   Ridvan:
   Checked how to get the info by scraping using BeutifulSoup and the info of each part of the website
   He also found a different way to overcome the website scraping protection that only using cloudscraper
   He checked the whole programming.

   Georgina: 
   Found cloudscraper to overcome the website scraping protection, then make a comand to get each piece of information requiered by BeautifulSoup, but changed to selectolax and chompjs because it was a more simple way to collect information. Tested the code to get the csv file with pandas. Make changes in the loop to get the list of webpages.

   - What went wrong ?
   We have some issues getting the information in the format it was required, we generated codes that did not get the right information or not all the information we wanted and we were running a bit out of time.

   - How you solved it ?

