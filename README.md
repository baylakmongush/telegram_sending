# telegram_sending

### 1. Register my.telegram.org

<img width="1122" alt="Снимок экрана 2023-01-04 в 20 56 16" src="https://user-images.githubusercontent.com/56039676/210623619-69eb0de0-99e5-4f87-980f-d099253bef51.png">

### 2. Create app and get api_id and api_hash
<img width="1122" alt="Снимок экрана 2023-01-04 в 20 57 09" src="https://user-images.githubusercontent.com/56039676/210625381-b9200ba2-2327-4162-b745-0c45f37aa27a.png">

### 3. Set environment and install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 4. Run script with arguments
```bash
python3 main.py -i <api_id> -a <api_hash> -p <phone_number> -m <message> -u <username> -c <username_target> -f <sending_file>
```
-i -- api_id from my.telegram.org </br>
-a -- api_hash from my.telegram.org </br>
-p -- phone number in international format </br>
-m -- message for sending </br>
-u -- your username </br>
-c -- username target for sending message </br>
-f -- sending file (optional) </br>