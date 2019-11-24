import re
with open('employees.csv', newline='') as f:
    file = 'name,surname,age,email Karrah,Filon,32,kfilon0@google.comGris,Sarjent,35,gsarjent1@cdc.govWesley,Chaves,64,wchaves2@amazon.comKynthia,Limprecht,41,klimprecht3@miitbeian.gov.cnTorrin,Shovelbottom,37,tshovelbottom4@so-net.ne.jpDebora,Weippert,49,dweippert5@howstuffworks.comHendrick,Arnke,49,harnke6@youtu.beStormy,Willford,33,swillford7@elegantthemes.comKarlan,Gonzales,45,kgonzales8@blogspot.com Betti,Plenty,36,bplenty9@printfriendly.com'
x = re.findall('[A-Za-z]', file)
print(x)