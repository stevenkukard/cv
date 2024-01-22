---
layout: page
title: Projects
permalink: /projects/
---

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