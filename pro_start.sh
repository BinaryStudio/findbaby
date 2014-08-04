rm -rf *.out
nohup python app.py pro >> app.out &
sleep 1
echo '---APP---'
cat app.out
