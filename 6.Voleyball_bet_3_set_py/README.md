# voley_bet_3_set
parsing/predict_model/autobet

## File names are working titles as the project was done for personal use, so there might be a lack of polish.

### 1. The program consists of 3 modules:

- **Parsing**: Parses live games from bookmaker websites.
- **Predictor**: Makes a prediction on which team to bet on based on a pre-trained model (the model is based on a test dataset of 8000 real games).
- **Autobet**: Places a bet on the outcome predicted by the predictor.

### The full process is executed in the following order:

1. Parser
2. Predictor
3. Autobet

All files are located in the `voley_set` folder. The training model is in the root of the project. In the `voley_set/test_model_result` folder, there are files that test the model's performance on real data.

### 2. To run the parser, execute the file `sound1508.py`.

### 3. To run the predictor, execute the file `to_bet.py`.

### 4. To run the autobet, execute the file `3_7`.

### 5. To check the predictor's performance, run the files in the `voley_set/test_model_result` folder in the order of their numerical prefixes. This step is optional and is provided to allow quick verification of the results.
