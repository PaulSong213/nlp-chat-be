from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from trainers import train_address
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
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.80
            }
        ]
    )

    # Train the bot
    # corpus_trainer = ChatterBotCorpusTrainer(bot)

    # corpus_trainer.train(
    #     "chatterbot.corpus.english.greetings",
    #     "chatterbot.corpus.english.conversations",
    #     "chatterbot.corpus.english.health",
    # )

    list_trainer = ListTrainer(bot)
    train_address(list_trainer)
    return bot
