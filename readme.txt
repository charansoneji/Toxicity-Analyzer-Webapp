README - TOXICITY ANALYSER BOT

-----------------------------------------------------

PART - I TELEGRAM BOT

1. In order to first make the model from the dataset, we need to run the get_model.py file on Google Colab as shown in the video.
   This is because huge amount of processing power is required.
2. After getting the model, download the model into the project directory.
3. Run the nlp_bot.py file which would then start our telegram bot.
4. The bot can now be accessed on Telegram with @ToxicAnalysisBot
5. Whenever a user messages a text, he receives a detailed toxicity analysis of the string.

-------------------------------------------------------

PART - II WEB APPLICATION

1. This part uses the premade model which we made in Part I.
2. Just go to the WebApp folder, the app.py file is the one which we need in order to start our localhost.
3. Open this project in an IDE and run app.py file.
4. The application will be hosted at 127.0.0.1:5000
5. Open the application, input some data.
6. If the data is within the safe limits, a safe signal is shown. Else unsafe signal is displayed.

------------------------------------------------------

END OF README