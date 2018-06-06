import pymysql

def all_users():
    sql = "" \
          "SELECT users.name, users.completeName, userstatuses.name, defaultstatuses.description " \
          "FROM rnds.users " \
          "left JOIN rnds.userstatuses on  users.actualUserStatus = userstatuses.name " \
          "left JOIN rnds.defaultstatuses on userstatuses.Defaultstatus = defaultstatuses.name "
    conn = pymysql.connect(user="root", password="root", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    users = []
    for t in result:
        user = {}
        user["users.name"] = str(t[0])
        user["completeName"] = t[1]
        user["userstatuses.name"] = t[2]
        user["description"]= t[3]
        users.append(user)

    conn.close()
    return users


def get_user_setting(status):
    sql = "" \
          "SELECT isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel " \
          "FROM rnds.usersettings WHERE name = %s"
    conn = pymysql.connect(user="root", password="root", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql, (status))

    result = cursor.fetchall()
    conn.close()
    return result


def put_user_setting(isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, name):
    sql1 = "UPDATE rnds.usersettings set isWindowsOpen=%s , isDoorOpen=%s, isLightsOn=%s, noiseLevel=%s WHERE name = %s"

    conn = pymysql.connect(user="root", password="root", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql1, (isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, name))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == '__main__':
    user_settings1 = get_user_setting('1_1')
    print(user_settings1)
    put_user_setting(1, 0, 0, 4, '1_1')
    user_settings1 = get_user_setting('1_1')
    print(user_settings1)
