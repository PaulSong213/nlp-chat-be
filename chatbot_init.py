from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from trainers import train_address, train_contact, train_how_appointment, what_to_bring_appointment, train_how_to_pay, how_long_wait_time, train_need_to_bring_old_medcert, train_can_request_doctor, train_obtain_medical_certificate_prescription, train_facility, train_parking, train_visiting_hours, train_is24hours, train_location_from_southmall
# TODO use the same chatbot settings in views.py


def chatbot_init():
    bot = ChatBot(
        'E. Zarate Assistant',
        read_only=True,
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'preprocessors.correct_zarate_term'
        ],
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, had no knowledge about that. Fee; free to contact E. Zarate Hospital facebook page for inquiries.',
                'maximum_similarity_threshold': 0.80
            }
        ]
    )

    # Train the bot
    corpus_trainer = ChatterBotCorpusTrainer(bot)

    corpus_trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations",
        "chatterbot.corpus.english.health",
    )

    list_trainer = ListTrainer(bot)
    train_address(list_trainer)
    train_contact(list_trainer)
    train_how_appointment(list_trainer)
    what_to_bring_appointment(list_trainer)
    train_how_to_pay(list_trainer)
    how_long_wait_time(list_trainer)
    train_need_to_bring_old_medcert(list_trainer)
    train_can_request_doctor(list_trainer)
    train_obtain_medical_certificate_prescription(list_trainer)
    train_facility(list_trainer)
    train_parking(list_trainer)
    train_visiting_hours(list_trainer)
    train_is24hours(list_trainer)
    train_location_from_southmall(list_trainer)
    return bot
