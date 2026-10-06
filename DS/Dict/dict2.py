data = {"Gujarat": ["gandhinagar" , "Surat" , "Ahmedabad"] , "Maharashtra":"Mumbai" , "Rajasthan":"Jaipur" , "Madhya Pradesh":"Bhopal" , "Karnataka":"Bengaluru" , "Tamil Nadu":"Chennai" , "Kerala":"Thiruvananthapuram" , "West Bengal":"Kolkata" , "Punjab":"Chandigarh" , "Haryana":"Chandigarh"}

print(data)
print(data["Gujarat"])
print(data.keys())
print(data.values())

print(data["Gujarat"][2])


data["Maharashtra"] = ["Mumbai" , "Pune" , "Nagpur"]  # to add data in dictionary we can use this method
print(data)