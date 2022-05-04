
def find_password(dict, site):
    if site in dict:
        return dict[site]


dict = {}
site_num, num = map(int, input().split())
for i in range(site_num):
    site, password = map(str, input().split())
    dict[site] = password

for j in range(num):
    site = input()
    print(find_password(dict, site))
