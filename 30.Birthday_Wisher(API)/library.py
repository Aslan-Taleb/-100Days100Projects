import smtplib
import datetime as dt
import random
import csv
import shutil


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
def update_csv(name, email, year, month, day):
    # Create the new row as a list
    new_row = [name, email, year, month, day]
    # Read the CSV file into a list of rows
    with open('birthdays.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]

    # Check if the new row is already in the list of rows
    if new_row in rows:
        print(f'The row {new_row} is already in the file.')
    else:
        # Add the new row to the list of rows
        rows.append(new_row)

        # Write the updated list of rows back to the CSV file
        with open('birthdays.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in rows:
                writer.writerow(row)


# Read the CSV file into a list of rows
def open_csv():
    rows = []
    with open('birthdays.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    del rows[0]
    return rows


# 2. Check if today matches a birthday in the birthdays.csv


def check_birthday(month, day):
    name = []
    mail = []
    the_list = open_csv()
    for i in the_list:
        if int(i[3]) == month and int(i[4]) == day:
            name.append(i[0])
            mail.append(i[1])
    if len(name) != 0 and len(mail) != 0:
        print(f"it's {name} with the mail : {mail} Birthday ! ")
        return name, mail
    else:
        print("no one today :(")
        return 0, 0


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pick_letter(name):
    random_number = random.randint(1, 3)
    name_file = "letter_templates/letter_" + str(random_number) + ".txt"
    name_copy_file = "copy_for_" + name + ".txt"
    shutil.copy(name_file, name_copy_file)
    with open(name_copy_file, 'r+') as f:
        contents = f.read()
        updated_contents = contents.replace('[NAME]', name)
        f.seek(0)
        f.write(updated_contents)
        f.truncate()
    return name_copy_file


# 4. Send the letter generated in step 3 to that person's email address.
def send(file, to_who):
    my_email = "aslantalebselim@gmail.com"
    password = "tu_pense"
    # Connect to the SMTP server using a secure connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls()

    # Login
    connection.login(user=my_email, password=password)
    # test email
    # Open the file for reading
    with open(file, 'r') as f:
        message = f.read()
    f.close()
    connection.sendmail(from_addr=my_email, to_addrs=to_who, msg=f"Subject:It's your birthday ! \n\n{message}")
    connection.quit()
    print("i sent : " + message + "\n\n" + "to: " + to_who + "\n")


def get_date():
    now = dt.datetime.now()
    month = now.month
    day = now.day
    return month, day
