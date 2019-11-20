import psycopg2
import requests
import yaml


def main():
    site = "https://www.bygeo.ru/materialy/naselenie-belarusi/238-spisok-gorodov-i-poselkov-respubliki-belarus-i-ix-c" \
           "hislennost-naseleniya-dannye-2003-goda.html"

    with open("password.yaml") as file:
        data = yaml.safe_load(file)
    try:
        if len(data) != 4: raise KeyError  # If file not corrected
        con = psycopg2.connect(
            host=data["host"],
            database=data["database"],
            user=data["user"],
            password=data["password"]
        )
    except KeyError:
        print("File password.yaml not corrected")
        exit(1)
    cur = con.cursor()

    response = requests.get(site)
    #print(response.status_code)
    print(response.content)

    #with open("CreateDatabaseMYSQL.sql", 'r') as file:
    #    cur.execute(file.read())

    #cur.execute("select * from SUBJECT")
    #for i in cur.fetchall():
    #    print(i)

    cur.close()
    con.close()


if __name__ == '__main__':
    main()
