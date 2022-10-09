import os
import requests

def slice_address(full_address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    query = {"address": full_address, "key": os.environ["GOOGLE_API"]}
    response = requests.get(url, params=query)
    response = return_response(response.json())
    return response

def return_response(response):
    if response["status"] == "ZERO_RESULTS":
        return None
    else:
        index_selected = 0
        for index in range(0, len(response["results"])-1):
            if len(response["results"][index]["address_components"]) > len(response["results"][index_selected]["address_components"]):
                index_selected = index
        return address_components(response["results"][index_selected])

def address_components(google_address_components):
    address_components = {}
    for google_address_component in google_address_components["address_components"]:
        field = None
        if "street_number" in google_address_component["types"]:
            field = "house_number"
        if "route" in google_address_component["types"]:
            field = "street"
        if "sublocality_level_1" in google_address_component["types"]:
            field = "district"
        if "administrative_area_level_4" in google_address_component["types"]:
            field = "quarter"
        if "administrative_area_level_2" in google_address_component["types"]:
            field = "city"
        if "administrative_area_level_1" in google_address_component["types"]:
            field = "state"
        if "postal_code" in google_address_component["types"]:
            field = "zip_code"
        if "country" in google_address_component["types"]:
            field = "country"

        if field:
            address_components[field] = google_address_component["short_name"]
    
    address_components["latitude"] = google_address_components["geometry"]["location"]["lat"]
    address_components["longitude"] = google_address_components["geometry"]["location"]["lng"]
    
    address_components["full_address"] = google_address_components["formatted_address"]

    return address_components
    