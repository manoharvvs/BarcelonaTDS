#Data Analysis of GitHub Users in Barcelona
Key Highlights
Data Scraping: Leveraging the GitHub API, we collected data on users in Barcelona with over 100 followers using a Python script. The data includes user profiles and repository details.
Insights Found: The most followed users predominantly work on JavaScript projects, and many joined GitHub before 2015, showing long-standing community presence.
Recommendation: Developers in Barcelona should collaborate more on repositories with permissive licenses like MIT to attract contributors and showcase skills.
Process
Data Collection:

Used GitHub API to scrape user details and their repositories in Barcelona with over 100 followers.
Implemented pagination to handle large datasets and wrote results to structured CSV files.
Data Cleaning:

Cleaned company names, handled null values, and standardized boolean fields in CSV files for consistency.
Filtered repositories and user details based on provided criteria (e.g., location, follower count).
Analysis:

Calculated statistics like most popular programming languages, average followers, and top repositories.
Visualized trends and correlations using Python's pandas and matplotlib libraries.
Results
Top Users by Followers:
midudev, ai, raysan5, vfarcic, spite.

Earliest Registered Users:
xyz_user1, xyz_user2, xyz_user3, xyz_user4, xyz_user5.

Popular Licenses:
MIT, Apache-2.0, GPL-3.0.

Dominant Companies:
IBM, GOOGLE, MICROSOFT.

Top Languages:
JavaScript, Python, Ruby.

Files in Repository
users.csv: Contains user details (e.g., login, name, followers, company, created_at).
repositories.csv: Contains repository details (e.g., full_name, language, stars, license_name).
script.py: Python code to scrape and clean the data.
README.md: Documentation of the project.
Instructions to Reproduce
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/yourrepo.git
Install dependencies (if any).
Run the script:
bash
Copy code
python script.py
Check users.csv and repositories.csv for the results.
