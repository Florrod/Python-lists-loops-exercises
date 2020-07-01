my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:

# my_sample_list[1] = "Steven"
# my_sample_list.append("Pepe")
# my_sample_list.insert(0,"Ruth"+"Pedro")
# my_sample_list.remove("Annie")
# my_sample_list.remove("Esmeralda")

# for i in reversed(my_sample_list):
#     print(i)

my_sample_list[1] = "Steven"
my_sample_list[-1]="Pepe"
my_sample_list[0]= my_sample_list[2] + my_sample_list[4]

for i in range(len(my_sample_list)-1,-1,-1):
    print(my_sample_list[i])