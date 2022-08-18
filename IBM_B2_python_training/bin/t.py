
# # Accesing API with try/except
# # ----------------------
# import requests
#
# try:
#     weather_api = f'https://demoqa.com/utilities/weather/city/pune'
#     weather_api_response = requests.get(weather_api)
# except:
#     print("Api not accessible")
# else:
#     print(weather_api_response.status_code)
# # ----------------------

# try:
#     weather_api_response = requests.get(weather_api)
# except:
#     return "Currently not able to access/get the details"
# else:
#     if (weather_api_response.status_code == 200):
#         weather_api_response = weather_api_response.json()
