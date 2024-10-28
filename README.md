# Lab 2 - Django Application For Sending Emails

## Pre-requisites
- Python 3.x installed. You can download it from the [official Python website](https://www.python.org/downloads/).

## Setting Up the Email Backend

It is assumed that you have a Gmail account. 

1. Go to your [Google Account](https://myaccount.google.com/apppasswords).

   ![image](https://github.com/user-attachments/assets/991a0c5d-0708-4191-b0af-51c251a30886)

3. Enter the **App name** and click **Create**.
4. A pop-up window will appear with the App password. Copy the 16-character code.
   
![image](https://github.com/user-attachments/assets/b22776a8-9403-438b-8ff4-5f8833e9b0dd)

6. Tap **Done**.
7. Go to the /myproject/settings.py file and replace the `EMAIL_HOST_PASSWORD` with the 16-character code.
8. Change the `EMAIL_HOST_USER` to your Gmail account.
9. Change the `DEFAULT_FROM_EMAIL` to your Gmail account.

## Cloning the Repository

```sh
git clone https://github.com/Aesonnn/WADT-Lab2.git
cd WADT-Lab2
```

## Installing Django

1. Create a virtual environment:

    ```sh
    python3 -m venv env
    ```

2. Install Django:

    ```sh
    pip install django
    ```

## Running the App

1. Navigate to the project directory:

    ```sh
    cd myproject
    ```

2. Run the development server:

    ```sh
    python manage.py runserver
    ```

3. Open your web browser and go to `http://127.0.0.1:8000/` to see your app in action.
