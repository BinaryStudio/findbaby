rm -rf *.out
nohup python app.py dev >> app.out &
sleep 1
echo '---APP---'
cat app.out

