---
layout: print
---

# Steven Kukard's CV 

 [stevenkukard@gmail.com](mailto:stevenkukard@gmail.com) 

 **Note** 

 *This document is a print version of my online CV, which can be viewed at [cv.stevenknightkukard.com](https://cv.stevenknightkukard.com).* 

# Introduction


<!-- ## Introduction -->
<!-- This is the online home for my CV, specifically focused on Data Science.  -->

My professional and academic journey is a tapestry of diverse and rich experiences, from music to financial markets, culminating in data science. This unique blend of creativity and analytical skills has shaped my approach to problem-solving and innovation. This CV outlines a career characterised by versatility, technical expertise, and a continuous pursuit of learning and growth.

<img src="/assets/steven-portrait-cropped.jpg" alt="Image: Portrait" width="100"/>


<div style="page-break-after: always"></div>

# Experience


I have been fortunate to have worked in a range of industries and in roles focusing on every part of the data pipeline, from data engineering, to analysis, to reporting and visualisation.

I am, therefore, well positioned to understand the needs of business users and design complete solutions accordingly.

<img src="/assets/job_timeline.png" alt="Chart: Job Timeline">

### Data Solutions Specialist
**X-Consulting**  
*Aug 2021 - Present (2 years 2 months)*

### Data Analytics Developer
**FORTITUDINE VINCIMUS CAPITAL ADVISORS**  
*Jan 2020 - Present (3 years 9 months)*  
I produce portfolio analytics using R, R Shiny, Excel and Refinitiv Eikon.

### DataOps Engineer
**Wimmy**  
*Feb 2022 - Jan 2023 (1 year)*

### Data Solutions Specialist
**Wimmy**  
*Oct 2021 - Feb 2022 (5 months)*

### Copy-editor
**Freelance**  
*Sep 2017 - Dec 2020 (3 years 4 months)*  
I have copy-edited many technical documents as well as PhD theses in the fields of Statistics, Computer Science, Physics and Disability Studies.

### Business Intelligence Analyst
**Prodigy Finance**  
*Feb 2020 - May 2020 (4 months)*  
I produced business intelligence dashboards using Tableau.

### Copy-editor
**WriteArt**  
*Jul 2016 - Oct 2019 (3 years 4 months)*  
My work focused on academic papers and dissertations in the field of Economics.

### Music Director
**Peppa Pig Live in South Africa**  
*Sep 2017 - Dec 2018 (1 year 4 months)*  
I composed and produced the original songs for the show Peppa Pig Live in South Africa.

### Project Manager
**PropertyEngine**  
*Feb 2017 - Aug 2017 (7 months)* I managed the outsourced work.

### Frontend Web Developer
**PropertyEngine**  
*Jun 2016 - Jun 2017 (1 year 1 month)*  
I developed the UI for one of their web apps and constructed a style guide for another.

### Data Scientist
**NMRQL Research**  
*Apr 2016 - Aug 2016 (5 months)*  
Fitted machine learning algorithms to share price data.

### Quantitative Analyst
*Aug 2010 - Feb 2016 (5 years 7 months)*  
- Designed and tested trading strategies.  
- Designed and maintained a database of market and fund data.  
- Designed and produced monthly fact sheets.  
- Wrote fund reports.  
- Created and maintained the company website.


<div style="page-break-after: always"></div>

# Projects


Here are a few examples that I feel cover a range of use cases. I intend to include working examples in the future. 

---

## Data Engineering & Cloud Architecture
The sort of work I've done in the field of data engineering involves automating the extraction of data from various sources, transforming it into a format suitable for analysis, and loading it into a database.

### Pulling project data from Jira to update Clockify
I created an endpoint for the Jira webhook, using an Azure Function, which receives a JSON payload from Jira whenever a project is updated, parses it, then stores the data in CosmosDB. A second Azure Function, triggered by the database update, updates Clockify via the Clockify API.

### Ingesting broker reports from emails
Every morning a Google Cloud Function checks the email inbox, downloads the CSV, stores it in Cloud Storage, parses the data, and loads it into BigQuery. This data is used to generate a daily fund performance report.

### Preparing audio files for human transcription
Routinely scrape audio files from specific podcasts, remove long silences, chop them into bite-sized chunks, and upload them to the repository for the transcribers to access. This was done using a team of functions running on Google Cloud Run.

---

## Data Visualisation & User Interfaces
Although I have built a UI using Javascript, I mainly use Streamlit (Python) and R Shiny. 

### Fund performance report
This app connects to the automatically-updated database and allows the user to alter values in the database, and then to download an Excel report containing the calculated metrics.

<div style="page-break-after: always"></div>

# Skills


## Approach

On the back end I deploy **serverless processes** that communicate with each other via HTTP endpoints. Soon, I hope to begin integrating AI/LLM workers into this architecture. 

On the front end I mainly use Python and R **UI frameworks** (Streamlit, Dash, Shiny) running in containers on the cloud.

---
## Programming Languages
- **Python**
- **R**
- SQL
- Javascript
- HTML

---
## Cloud Platforms

### Google Cloud Platform
- BigQuery
- Cloud Storage
- Cloud Run
- Cloud Functions

### Microsoft Azure
- Functions
- CosmosDB
- SQL Database
- Machine Learning Studio
- Data Factory

<div style="page-break-after: always"></div>

# Education


My journey has taken me from music, to finance, to data science. I've kept a foot in the music world, taking on the occasional composition project.

<!-- After completing my undergraduate degree in music, I spent a year working as a freelance composer and music producer. I then moved into finance, working as a quantitative analyst for a hedge fund. I spent 5 years in finance, completing my CFA 1 and honours degree in statistics. I then moved into data science, working as a data scientist for a large South African retailer. I've been working as a data scientist for the past 3 years. -->

---


### University of Cape Town
**STA4016H, Statistics**  
*2014 - 2015*  
Half the credits of an honours degree.  
My honors project investigated the results of using stochastic optimization algorithms to find parameter sets for quantitative trading strategies.

### CFA Institute
**CFA 1**  
*2009 - 2010*

### University of Cape Town
**BMus, Composition**  
*2004 - 2007*  
Dean's Merit List 2004, 2005, 2006, 2007

## Licenses & Certifications

- **Introduction to Financial Markets**  
  *South African Institute of Financial Markets*

- **The Equity Market**  
  *South African Institute of Financial Markets*

- **Regulation and Ethics of the SA Financial Markets**  
  *South African Institute of Financial Markets*



---
[stevenkukard@gmail.com](mailto:stevenkukard@gmail.com)