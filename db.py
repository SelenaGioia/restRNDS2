import pymysql

def all_users():
    sql = "" \
          "SELECT users.name, users.completeName, userstatuses.name, defaultstatuses.description, users.isDisturbing, users.actualNoiseLevel " \
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
        user["userID"] = str(t[0])
        user["userName"] = t[1]
        user["currentStatusID"] = t[2]
        user["currentStatus"]= t[3]
        user["disturbing"]= t[4]
        user["noiseLevel"]=t[5]
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

def statuses():
    sql = "" \
          "SELECT * " \
          "FROM defaultstatuses "
    conn = pymysql.connect(user="root", password="root", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    statuses = []
    for t in result:
        status = {}
        status["statusID"] = str(t[0])
        status["statusDescription"] = t[1]
        statuses.append(status)

    conn.close()
    return statuses

def put_user_status(username, status):
    sql1 = "UPDATE rnds.users set actualUserStatus=%s WHERE name = %s"

    conn = pymysql.connect(user="root", password="root", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql1, (status, username))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result


def get_user_setting2(status):
    sql = "" \
          "SELECT usersettings.name, isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, customisedDescription " \
          "FROM rnds.usersettings LEFT JOIN rnds.userstatuses ON usersettings.name = userstatuses.name " \
          "WHERE usersettings.name = %s"
    conn = pymysql.connect(user="root", password="root", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql, (status))

    result = cursor.fetchall()


    for t in result:
          status = {}
          status["StateID"] = t[0]
          status["isWindowsOpen"] = t[1]
          status["isDoorOpen"] = t[2]
          status["isLightsOn"] = t[3]
          status["noiseLevel"] = t[4]
          status["customisedDescription"] = t[5]

    conn.close()
    return status



def put_user_setting2(isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, description, name):
    sql1 = "UPDATE rnds.usersettings set isWindowsOpen=%s , isDoorOpen=%s, isLightsOn=%s, noiseLevel=%s WHERE name = %s"
    sql2 = "UPDATE rnds.userstatuses set customisedDescription = % s WHERE name = %s"

    conn = pymysql.connect(user="root", password="root", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql1, (isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, name))
    cursor.execute(sql2, (description, name))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == '__main__':
    #users= all_users()
    #print (users)
    #user_settings1 = get_user_setting('1_1')
    #print(user_settings1)
    #put_user_setting(1, 0, 0, 4, '1_1')
    #user_settings1 = get_user_setting('1_1')
    #print(user_settings1)
    #Availablestatuses= statuses()
    #print (Availablestatuses)
    #users = all_users()
    #print (users)
    #put_user_status('1','1_4')
    #users = all_users()
    #print (users)
    put_user_setting2(1, 0, 0, 3,'shopping at supermarket', '1_1')
    user_settings2 = get_user_setting2('1_1')
    print(user_settings2)