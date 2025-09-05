"""saitama"""

push_goal = int(input())
situp_goal = int(input())
squat_goal = int(input())
run_goal = int(input())

push_day = int(input())
situp_day = int(input())
run_day = int(input())
squat_day = int(input())

if not push_goal % push_day:
    days_push = push_goal // push_day
else:
    days_push = push_goal // push_day + 1

if not situp_goal % situp_day:
    days_situp = situp_goal // situp_day
else:
    days_situp = situp_goal // situp_day + 1

if not squat_goal % squat_day:
    days_squat = squat_goal // squat_day
else:
    days_squat = squat_goal // squat_day + 1

if not run_goal % run_day:
    days_run = run_goal // run_day
else:
    days_run = run_goal // run_day + 1


most_days = days_push
if days_situp > most_days:
    most_days = days_situp
if days_squat > most_days:
    most_days = days_squat
if days_run > most_days:
    most_days = days_run

print(most_days)
