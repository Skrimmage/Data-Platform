#! /bin/bash

# Credit: https://medium.com/@hillarywando/using-crontab-bash-scripts-to-do-automated-git-push-daily-27c6a8cedc49
# Date in format Day-Month-Year
date=$(date +"%Y-%m-%d %T")

# Commit message
message="Auto-push for $date"
cd /home/dpage/Projects/skrimmage/frontend/
git add .
git commit -m "${message}"
status="$(git status --branch --porcelain)"
echo $status >> ~/cron_git_push.log
if [ "$status" == "## main...origin/main" ]; then
  echo "{$date}: No Changes" >> ~/cron_git_push.log
else
  echo "{$date}: Changes being pushed. " >> ~/cron_git_push.log
  git push -u origin main
fi