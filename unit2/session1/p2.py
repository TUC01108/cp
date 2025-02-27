def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        info = festival_schedule[artist]
        return info
    else:
        return "Artist not found"



festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  

# we have key value of band and set time, day, location
# outside of that dictionary we have just band name and the schedule value