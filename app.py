import requests

response = requests.get("https://api.covidtracking.com/v1/us/20201201.json")
print(response.status_code)

print(response.json())

## Testing

## Infections (Confirmed)

## Change Over Time Infections Rate
## Is COVID infetions getting more aggressive and contagious over time? 

## Hospitalizations

## Change Over Time in Hospitalizations
## Are people with confirmed cases more likely to access onsite medical care?

## Deaths / Death Rate

## Recovered / Recovered Rate


