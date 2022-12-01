import sqlite3

db = sqlite3.connect("app.db")

cr = db.cursor()


def commit_and_close():

    db.commit()

    db.close()

    print("Database Is Closed")


uid = 1

input_message = """
What Do You Want To Do ?
"s" => Show All Skills.
"a" => Add New Skill.
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quite The App
Choose Option:
"""

user_input = input(input_message).strip().lower()

commands_list = ["s", "a", "d", "u", "q"]


def show_skill():

    cr.execute(f"select * from skills where user_id = '{uid}'")

    results = cr.fetchall()

    print(f"You Have {len(results)} Skills")

    if len(results) > 0:

        print("Showing Skills With Progress: ")

    for row in results:

        print(f"Skill => {row[0]}", end=" ")

        print(f"Progress => {row[1]}")

    print("Your Data Is Showed")

    commit_and_close()


def add_skill():

    sk = input("Enter Your Skill Name: ").strip().capitalize()

    cr.execute(
        f"select name from skills where name = '{sk}' and user_id = '{uid}'")

    result_add_skill = cr.fetchone()

    if result_add_skill == None:

        prog = input("Enter Your Skill Progress: ").strip()

        cr.execute(
            f"insert into skills(name, progress, user_id) values('{sk}','{prog}',{uid})")

        print("Your Data Is Added")

        commit_and_close()

    else:

        print("Sorry, Skill Is Found in Db And You Can Not Add It")

        found_skill = input(
            "Want You Skill Update? Choose y or n: ").strip().lower()

        if found_skill == 'y':

            update_skill()

        else:

            commit_and_close()


def delete_skill():

    sk = input("Enter Your Skill Name: ").strip().capitalize()

    cr.execute(
        f"delete from skills where name ='{sk}' and user_id ='{uid}'")

    print("Your Data Is Deleted")

    commit_and_close()


def update_skill():

    sk = input("Enter Your Skill Name: ").strip().capitalize()

    prog = input("Enter Your New Skill Progress: ").strip()

    cr.execute(
        f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")

    print("Your Data Is Updated")

    commit_and_close()


if user_input in commands_list:

    print(f"Commands {user_input} Is Found")

    if user_input == "s":

        show_skill()

    elif user_input == "a":

        add_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        update_skill()

    else:

        print("App Is Closed.")

else:

    print(f"Sorry The Command \"{user_input}\" Is Not Found")
