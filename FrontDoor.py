from datetime import *
import datetime
import pytz
import requests
import json


def FrontDoor(pair):
    def date_time():
        import time
        current_date_time = time.localtime()
        year = str(current_date_time[0])
        month = str(current_date_time[1])
        day = str(current_date_time[2])
        time = str(f'{current_date_time[3]}:{current_date_time[4]}:{current_date_time[5]}')
        weekday_number = (current_date_time[6])
        weekday_words = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'
        }
        weekday = weekday_words.get(weekday_number, weekday_number)
        current_date_time = [year, month, day, time, weekday]
        return current_date_time

    def notion_export(weekday, pair_checkbox_passin, tz_name):
        token = 'secret_E2oQTwLQmCGonuLhWgYopiLomySC3cCqYlgELp3Mid6'
        database_id = 'b18d956b99ba4887a2dff6debcfc9777'
        headers = {
            'Authorization': "Bearer " + token,
            'Content-Type': "application/json",
            'Notion-Version': "2021-08-16"
        }
        create_url = 'https://api.notion.com/v1/pages'

        def first_last_check(database_id, headers, tz_name):
            read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
            res = requests.request("POST", read_url, headers=headers)
            data = res.json()
            # Converts UTC datetime to Local datetime so the dates will be accurate!
            local_tz = pytz.timezone(tz_name)

            def utc_to_local(utc_dt):
                local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
                return local_tz.normalize(local_dt)

            page_id = data["results"][0]["id"]
            last_date_notion = data["results"][0]["created_time"]
            last_date_recorded_utc = datetime.datetime.strptime(last_date_notion, "%Y-%m-%dT%H:%M:%S.000Z")
            last_date_recorded_local = utc_to_local(last_date_recorded_utc).date()
            current_utc_datetime = datetime.datetime.utcnow()
            current_utc_date = utc_to_local(current_utc_datetime).date()

            def update_last_line(pageID, headers):
                update_url = f"https://api.notion.com/v1/pages/{pageID}"
                update_page_data = {
                    "properties": {
                        "Not Customer": {
                            "checkbox": True
                        }
                    }
                }

                data_update = json.dumps(update_page_data)

                response = requests.request("PATCH", update_url, headers=headers, data=data_update)
                print(response.status_code)

            if current_utc_date == last_date_recorded_local:
                return False
            else:
                update_last_line(page_id, headers)
                return True

        new_page_data = {
            "parent": {"database_id": database_id},
            "properties": {
                "WeekDay": {
                    "select": {
                        "name": f"{weekday}",
                    }
                },
                "Not Customer": {
                    "checkbox": first_last_check(database_id, headers, tz_name)
                },
                "Pair": {
                    "checkbox": pair_checkbox_passin
                },
            }
        }
        new_page_json = json.dumps(new_page_data)
        res = requests.request("POST", create_url, headers=headers, data=new_page_json)

    # ____DOOR OPEN PROG____
    current_date_time = date_time()
    if pair == 0:
        pair_checkbox = False
    else:
        pair_checkbox = True
    tz_name = 'Canada/Mountain'  # TODO Rewrite this line so that it pulls local tz
    notion_export(current_date_time[4], pair_checkbox, tz_name)
    print(current_date_time)


# pair = True     #  TODO get rid of these before POST
# FrontDoor(pair)
