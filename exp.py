def expp(your_info):
    with open('info.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person_tel in info_list:
            if your_info in person_tel:
                print(person_tel)


    
    