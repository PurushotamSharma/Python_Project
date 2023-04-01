list_of_cloud= ["aws","azure","oracle","gcp"]
list_of_env =["dev","test","prod"]

# print(list_of_cloud[0])

# print(list_of_env[1])

# list iteration 
for cloud in list_of_cloud:
    if cloud =="aws":
         print("Aws is the best cloud")
         
         
         
# dictionary
dict_of_cloud ={
    "aws":"Amazon web service",
    "azure":"Microsoft Azure",
    "gcp":"Google cloud platform"
    
}
print(dict_of_cloud["aws"])
print(dict_of_cloud.get("linode","Not found"))
dict_of_cloud.update({"linode":"linode of the cloiud"})
print(dict_of_cloud.get("linode","Not found"))
