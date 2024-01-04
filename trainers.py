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
        'Where it is located?',
        'Where is the hospital located?',
        'What is the address of the hospital?',
        'What is your location?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_contact(list_trainer):
    """
    Trains the bot to respond to contact number queries
    """
    ANSWER = "You can contact E. Zarate Hospital through phone 0919 991 4938 or email ezaratehospital@yahoo.com"

    questions = [
        'What is the contact number of E. Zarate Hospital?',
        'What is the contact number of the hospital?',
        'Contact number?',
        'Contact number of the hospital?',
        'Contact number of E. Zarate Hospital?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_how_appointment(list_trainer):
    """
    Trains the bot to respond to appointment queries
    """
    ANSWER = "You can schedule an appointment by using the E. Zarate Hospital reservation system by visiting www.ezarate.tech/appointment or by texting 0919 991 4938"

    questions = [
        'How can I schedule an appointment?',
        'How can I schedule an appointment with the doctor?',
        'How can I schedule an appointment with the hospital?',
        'How can I schedule an appointment with E. Zarate Hospital?',
        'How can I schedule an appointment with E. Zarate Hospital?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def what_to_bring_appointment(list_trainer):
    """
    Trains the bot to respond to appointment queries
    """
    ANSWER = "You can bring the following: 1. Medical Records 2. Doctor's Referral 3. Valid ID"

    questions = [
        'What should I bring during my appointment?',
        'What should I bring during my appointment with the doctor?',
        'What should I bring during my appointment with the hospital?',
        'What should I bring during my appointment with E. Zarate Hospital?',
        'What should I bring during my appointment with E. Zarate Hospital?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_how_to_pay(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "E. Zarate Hospital accepts the following payment methods: 1. Cash 2. Credit Card 3. Debit Card 4. HMO"

    questions = [
        'How can I pay?',
        'How can I pay for my hospital bill?',
        'How can I pay for my bill?',
        'How can I pay for my bill?',
        'How can I pay for my bill?',
        'How to pay?',
        'Do you accept credit card?',
        'Do you accept debit card?',
        'Do you accept HMO?',
        'Do you accept GCash?'
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def how_long_wait_time(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "The wait time depends on the number of patients, you have existing record and whether you have reservation. You can schedule an appointment by using the E. Zarate Hospital reservation system by visiting www.ezarate.tech/appointment or by texting 0919 991 4938"

    questions = [
        'How long is the wait time?',
        'How long is the wait time for the doctor?',
        'How long is the wait time for the hospital?',
        'How long is the wait time for E. Zarate Hospital?',
        'How long is the wait time for E. Zarate Hospital?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_need_to_bring_old_medcert(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "You need to bring your old medical certificate for your follow up checkup"

    questions = [
        'Do I need to bring my old medical certificate?',
        'Do I need to bring my old medical certificate for my follow up checkup?',
        'Do I need to bring my old medical certificate for my follow up checkup?',
        'Do I need to bring my old medical certificate for my follow up checkup?',
        'Do I need to bring my old medical certificate for my follow up checkup?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_can_request_doctor(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "You can request for a specific doctor by using the E. Zarate Hospital reservation system by visiting www.ezarate.tech/appointment or by texting 0919 991 4938"

    questions = [
        'Can I request for a specific doctor?',
        'Am I allowed to request for a specific doctor?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_obtain_medical_certificate_prescription(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "You can obtain your precription medical certificate by visiting the hospital at 16 J. Aguilar Avenue, Talon Uno, Las Piñas City. You can also get a verfiable digital copy of your medical certificate by checking your email. Your data will be stored in a secure data wallet for your convenience."

    questions = [
        'How can I obtain my medical certificate and prescription?',
        'How can I obtain my medical certificate and prescription after my checkup?',
        'How can I obtain a prescription or medical certificate after my consultation?'
        'how to get my medical certificate?',
        'how to get my prescription?',
        'how to get my medical certificate and prescription?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_facility(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "E. Zarate Hospital has the following facilities: 1. Emergency Room 2. Operating Room 3. Pharmacy 4. Laboratory 5. X-Ray"

    questions = [
        'What are the facilities of E. Zarate Hospital?',
        'What are the facilities of the hospital?',
        'What are the facilities of E. Zarate Hospital?',
        'What are the facilities of E. Zarate Hospital?',
        'What are the facilities of E. Zarate Hospital?',
        'Is there a pharmacy or laboratory within the hospital for convenience?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_parking(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "E. Zarate Hospital has a parking lot for patients and visitors"

    questions = [
        'Is there a parking lot?',
        'Is there a parking lot for patients?',
        'Is there a parking lot for visitors?',
        'Is there a parking lot for patients and visitors?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_visiting_hours(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "Visiting hours are from 8:00 AM to 8:00 PM"

    questions = [
        'What are the visiting hours?',
        'What are the visiting hours of the hospital?',
        'What are the visiting hours of E. Zarate Hospital?',
        'What are the visiting hours of E. Zarate Hospital?',
        'What are the visiting hours of E. Zarate Hospital?',
        'When is the visiting hours?',
        'When is the visiting hours of the hospital?',
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_is24hours(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "The hospital is open 24 hours"

    questions = [
        "Is the hospital open 24 hours?",
        "Is the hospital always open?",
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])


def train_location_from_southmall(list_trainer):
    """
    Trains the bot to respond to payment queries
    """
    ANSWER = "You can commute using jeepneys heading to Zapote then drop off on Casimiro Jollibee. From Casimiro you can walk through CAA road to go to E. Zarate Hospital."

    questions = [
        "How do I get to the hospital from SM Southmall?",
        "From SM Southmall, how do I get to the hospital?",
        "I am from SM Southmall, how do I get to the hospital?",
    ]

    for question in questions:
        list_trainer.train([
            question,
            ANSWER,
        ])
