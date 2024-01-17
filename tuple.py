address=(51,"17th street","NE","Redmond","WA",92014)#packing
print(address)
print(address[3])
#unpacking
housenumber,street,direction,city,state,zipcode=address
print(direction)
print(address[1:4])#slicing
address[2]="SE"