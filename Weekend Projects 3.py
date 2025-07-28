import requests

# Welcome message
print("\n=== SIMPLE JOB SEARCH ===")
print("Find jobs in 3 countries!\n")

# 1. Country selection
print("Choose a country:")
print("1. United States")
print("2. Canada")
print("3. UAE")

country_choice = input("Enter 1, 2, or 3: ")

if country_choice == "1":
    country_code = "us"
elif country_choice == "2":
    country_code = "ca"
elif country_choice == "3":
    country_code = "ae"
else:
    print("Invalid choice. Using USA as default.")
    country_code = "us"

# Job title input
job_title = input("\nWhat job do you want? (e.g. 'python' or 'designer'): ")

#API setup
api_key = "Tu veux copié le Api Key de Qui"
url = "https://jsearch.p.rapidapi.com/search"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}
params = {
    "query": f"{job_title} in {country_code}",
    "page": "1"
}

 #Get jobs from API
print("\nSearching for jobs...")
try:
    response = requests.get(url, headers=headers, params=params)
    jobs = response.json().get("data", [])[:5]  # Get first 5 jobs only
except:
    jobs = []
    print("Error connecting to API. Check your internet or API key.")

# 5. Display results
print("\n=== RESULTS ===")
if not jobs:
    print("No jobs found. Try a different search.")
else:
    for i, job in enumerate(jobs, 1):
        print(f"\nJob {i}:")
        print(f"Title: {job.get('job_title', 'Unknown')}")
        print(f"Company: {job.get('employer_name', 'Unknown')}")
        print(f"Location: {job.get('job_city', 'Unknown')}")
        print(f"Type: {job.get('job_employment_type', 'Unknown')}")
        if job.get('job_apply_link'):
            print(f"Apply here: {job['job_apply_link']}")

print("\nSearch complete! Good luck with your job hunt!")
