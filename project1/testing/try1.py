#Converted queryset to list
# a = WebBeta1.objects.all().values()


a = [{'id': 3, 'service_name': 'Streams', 'ip1': '10.30.48.178', 'ip2': '10.30.48.183', 'ip3': '10.30.48.185', 'ip4': '', 'ip5': ''}, {'id': 4, 'service_name': 'Admin5', 'ip1': '10.30.48.153', 'ip2': '10.30.48.154', 'ip3': '10.30.48.192', 'ip4': '', 'ip5': ''}]
# print(a)
# print(type(a[0]))

# new_list = list((a[0]).values())
# print(new_list)
print(len(a))
j = 0
b = []

for i in a:
    while j < len(a):
        c =  list((a[j]).values())
        j = j + 1
        b.append(c)
    
    
print("----",b)
    
