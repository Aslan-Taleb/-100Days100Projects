from library import *


def main():
    #if we want to add someone..
    #update_csv("Amine", "mohamedamin.hamzaoui@edu.isetcom.tn", "2001", "04", "05")
    i = 0
    month_of_day, day_of_day = get_date()
    name_of, mail_of = check_birthday(month_of_day, day_of_day)
    if name_of != 0:
        for the_name in name_of:
            file = pick_letter(the_name)
            send(file, mail_of[i])
            i += 1
main()
