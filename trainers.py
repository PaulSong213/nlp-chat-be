def train_address(list_trainer):
    """
    Trains the bot to respond to location/address queries
    """
    ANSWER = "E. Zarate Hospital is located at 16 J. Aguilar Avenue, Talon Uno, Las Piñas City"

    questions = [
        'Where can I find the address of E. Zarate Hospital?',
        'Where is the hospital located?',
        'Where is the hospital?',
        'What is the address of Zarate Hospital?',
        'Location?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])
