# **Data Analysis of GitHub Users in Barcelona**
### Data Scraping:
Leveraging the GitHub API, we collected data on users in Barcelona with over 100 followers using a Python script. The data includes user profiles and repository details.
### Insights Found: 
    The most followed users predominantly work on JavaScript projects, and many joined GitHub before 2015, showing long-standing community presence.
### Recommendation:
     Developers in Barcelona should collaborate more on repositories with permissive licenses like MIT to attract contributors and showcase skills.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Process

## Data Collection:
    Used GitHub API to scrape user details and their repositories in Barcelona with over 100 followers.Implemented pagination to handle large datasets and wrote results to structured CSV files.

## Data Cleaning:
    Cleaned company names, handled null values, and standardized boolean fields in CSV files for consistency.Filtered repositories and user details based on provided criteria (e.g., location, follower count).

## Analysis:
    Calculated statistics like most popular programming languages, average followers, and top repositories.Visualized trends and correlations using Python's pandas and matplotlib libraries.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Files in Repository
***users.csv:*** : Contains user details (e.g., login, name, followers, company, created_at).
***repositories.csv*** : Contains repository details (e.g., full_name, language, stars, license_name).
***script.py:*** : Python code to scrape and clean the data.
***README.md:*** : Documentation of the project.
