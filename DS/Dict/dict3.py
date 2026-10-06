data = {"Gujarat": ["gandhinagar" , "Surat" , "Ahmedabad"] , "Maharashtra":"Mumbai" , "Rajasthan":"Jaipur" , "Madhya Pradesh":"Bhopal" , "Karnataka":"Bengaluru" , "Tamil Nadu":"Chennai" , "Kerala":"Thiruvananthapuram" , "West Bengal":"Kolkata" , "Punjab":"Chandigarh" , "Haryana":"Chandigarh"}

data.update({"Goa":"Panaji" , "UP":"Lucknow" , "Bihar":"Patna"})

data["J & k"] = "Srinagar"


data.pop("Rajasthan")
# print(data)

data.popitem()
print(data)