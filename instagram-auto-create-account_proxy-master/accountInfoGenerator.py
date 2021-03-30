import string
import random


# Generating name functions 
# You can create different surnames to increase the variety of usernames.
def generatingName():
    firstName = [
        "Adelaide", "Douglas",
        "Lucia", "Davis",
        "Brianna", "Brooks",
        "Penelope", "Payne",
        "Edgar", "Fowler",
        "Steven", "Harper",
        "Melanie", "Perry",
        "Savana", "Murray",
        "Hailey", "Higgins",
        "Carina", "Brown",
        "Anna", "Parker",
        "George", "Thomas",
        "Edward", "Warren",
        "Violet", "Miller",
        "Oscar", "Mason",
        "Emma", "Walker",
        "Alexia", "Farrell",
        "Nicholas", "Wells",
        "Elian", "Phillips",
        "Lenny", "Baker",
        "Briony", "Ross",
        "Vanessa", "Johnson",
        "Miley", "Farrell",
        "Tiana", "Parker",
        "Harold", "Evans",
        "Gianna", "Hawkins",
        "Joyce", "Clark",
        "Edward", "Elliott",
        "Heather", "Holmes",
        "Arnold", "Harris",
        "Tony", "Robinson",
        "Olivia", "Morris",
        "Roman", "Jones",
        "Tiana", "Perry",
        "Edith", "Sullivan",
        "Audrey", "Brown",
        "Jenna", "Warren",
        "Lucia", "Campbell",
        "Elise", "Casey",
        "Melissa", "Payne",
        "Jessica", "Armstrong",
        "Fenton", "Robinson",
        "Julian", "Moore",
        "April", "Johnson",
        "Daniel", "Adams",
        "Robert", "Casey",
        "Nicole", "Murray",
        "William", "Clark",
        "Ashton", "Farrell",
        "Sarah", "Stewart",
        "Roman", "Alexander",
        "Richard", "Moore",
        "Reid", "Gibson",
        "George", "Jones",
        "Kelvin", "Sullivan",
        "Abigail", "Chapman",
        "Michael", "Harrison",
        "Charlie", "Cameron",
        "Carina", "Bennett",
        "Thomas", "Campbell",
        "Emma", "Cunningham",
        "Adele", "Ryan",
        "Kellan", "Holmes",
        "Nicholas", "Grant",
        "Brad", "Murray",
        "Nicholas", "Ross",
        "Martin", "Johnson",
        "Miley", "Higgins",
        "Tiana", "Allen",
        "Abigail", "Henderson",
        "Arnold", "Harper",
        "Savana", "Morgan",
        "Jessica", "Clark",
        "Antony", "Wright",
        "Connie", "Barnes",
        "Tiana", "Higgins",
        "Roland", "Brooks",
        "Edward", "Campbell",
        "Lydia", "Payne",
        "Antony", "Carroll",
        "Myra", "Carroll",
        "Dexter", "Carroll",
        "Maya", "Myers",
        "Alan", "Mason",
        "Carlos", "Baker",
        "Jessica", "Mason",
        "Frederick", "Lloyd",
        "Michelle", "Montgomery",
        "Kevin", "Phillips",
        "Spike", "Watson",
        "Catherine", "Holmes",
        "Leonardo", "Henderson",
        "Roland", "Payne",
        "Jenna", "Anderson",
        "Agata", "Gibson",
        "Emily", "Kelley",
        "Carlos", "Murray",
        "Harold", "Ferguson",
        "Savana", "Hill",
        "Albert", "Crawford"

    ]

    surName = ["Carl", "Ross",
               "Michael", "Rogers",
               "Ada", "Harrison",
               "Gianna", "West",
               "Roland", "Jones",
               "Brianna", "Hall",
               "Kirsten", "Campbell",
               "Emma", "Brown",
               "Sofia", "Cole",
               "Clark", "Miller",
               "Bruce", "Andrews",
               "Nicole", "Williams",
               "Rosie", "Hall",
               "Alexia", "Campbell",
               "Marcus", "Anderson",
               "Jenna", "Ferguson",
               "Myra", "Evans",
               "Albert", "Hamilton",
               "Carina", "Riley",
               "Carl", "Cameron",
               "Alen", "Wells",
               "Brad", "Hawkins",
               "Stuart", "Ryan",
               "Vincent", "Higgins",
               "Rebecca", "Thomas",
               "Adelaide", "Harper",
               "Ada", "Morgan",
               "James", "Henderson",
               "Lydia", "Stewart",
               "Dale", "Hall",
               "Jessica", "Gibson",
               "Ned", "Cooper",
               "Chester", "Holmes",
               "Antony", "Harrison",
               "Kimberly", "Craig",
               "Rosie", "Bennett",
               "Martin", "Stevens",
               "Carl", "Baker",
               "Chloe", "Wilson",
               "Garry", "Brooks",
               "Deanna", "Henderson",
               "Kelsey", "Jones",
               "Vincent", "Ross",
               "Tess", "Bailey",
               "Blake", "Bennett",
               "Amber", "Carter",
               "Charlie", "Phillips",
               "Jared", "Mitchell",
               "Adam", "Ferguson",
               "Vincent", "Grant",
               "James", "Farrell",
               "Fenton", "Foster",
               "Lily", "Evans",
               "Jared", "Tucker",
               "Nicole", "Brooks",
               "Melissa", "Crawford",
               "Edwin", "Perry",
               "Aida", "Robinson",
               "Kellan", "Phillips",
               "Sawyer", "Owens",
               "Natalie", "Armstrong",
               "Cadie", "Sullivan",
               "Aiden", "Alexander",
               "Harold", "Nelson",
               "Abraham", "Lloyd",
               "Naomi", "Spencer",
               "Reid", "Chapman",
               "Cadie", "Owens",
               "Sydney", "Stewart",
               "Vincent", "Nelson",
               "Vincent", "Martin",
               "Vanessa", "Wells",
               "Melanie", "Phillips",
               "Kelvin", "Andrews",
               "Michael", "Morrison",
               "Haris", "Henderson",
               "Sam", "Brown",
               "Roland", "Baker",
               "Dainton", "Cameron",
               "Edward", "Campbell",
               "Steven", "Grant",
               "Dexter", "Grant",
               "Aida", "Hawkins",
               "Derek", "Gray",
               "Kirsten", "Harris",
               "Julia", "Farrell",
               "Julian", "Watson",
               "Elian", "Andrews",
               "Tara", "West",
               "Albert", "Miller",
               "Dainton", "Owens",
               "Stuart", "Bailey",
               "Oscar", "Adams",
               "Stella", "Chapman",
               "Aida", "Grant",
               "Ashton", "Craig",
               "Gianna", "Cooper",
               "Reid", "Hunt",
               "Melanie", "Turner",
               "Joyce", "Henderson"
               ]
    return ''.join(random.choice(firstName) + ' ' + random.choice(surName))


# Generating a username
def username(size=8, chars=string.ascii_lowercase + random.choice(['.', '_'])):
    word_list = [

        "Carlos", "Holmes",
        "Ellia", "Lloyd",
        "Florrie", "Watson",
        "Aiden", "Richardson",
        "Florrie", "Montgomery",
        "Roman", "Barnes",
        "Adelaide", "Williams",
        "Victor", "Alexander",
        "Fenton", "Cole",
        "Violet", "Fowler",
        "Adrianna", "Ross",
        "Fenton", "Douglas",
        "Valeria", "Parker",
        "Andrew", "Anderson",
        "Stella", "Tucker",
        "Mary", "Warren",
        "Sienna", "Brown",
        "Ryan", "Barrett",
        "Richard", "Adams",
        "Alina", "Jones",
        "Andrew", "West",
        "Jessica", "Riley",
        "Sarah", "Dixon",
        "Mike", "Carroll",
        "Isabella", "Davis",
        "Justin", "Cooper",
        "Maya", "Perkins",
        "Amelia", "Kelly",
        "Naomi", "Ryan",
        "Olivia", "Carter",
        "Alexia", "Chapman",
        "Edward", "Wells",
        "Victor", "Higgins",
        "Eleanor", "Scott",
        "Michael", "Cooper",
        "Chelsea", "Harrison",
        "Henry", "Murray",
        "Julian", "Grant",
        "Alina", "Gray",
        "John", "Richards",
        "Justin", "Andrews",
        "Ned", "Henderson",
        "Sabrina", "Richards",
        "Sawyer", "Craig",
        "Valeria", "Taylor",
        "Alissa", "Bailey",
        "Chester", "Kelley",
        "Rubie", "Higgins",
        "Alexander", "Farrell",
        "Cadie", "Adams",
        "Heather", "Morgan",
        "Caroline", "Cooper",
        "Amelia", "Stevens",
        "Blake", "Ferguson",
        "Sofia", "Martin",
        "Tiana", "Fowler",
        "Paul", "Payne",
        "Briony", "Murray",
        "Olivia", "Harper",
        "Kevin", "Evans",
        "Alexia", "Cunningham",
        "Sawyer", "Barrett",
        "Ryan", "Hill",
        "Nicholas", "Barnes",
        "John", "Barnes",
        "Dale", "Hunt",
        "Thomas", "Payne",
        "Florrie", "Roberts",
        "Ned", "Alexander",
        "Edward", "Watson",
        "Amy", "Jones",
        "Roman", "Roberts",
        "Luke", "Crawford",
        "Jacob", "Scott",
        "George", "Wilson",
        "Amber", "Miller",
        "Elise", "Morrison",
        "David", "Grant",
        "Samantha", "Myers",
        "Dainton", "Richards",
        "Jordan", "Spencer",
        "Carina", "Elliott",
        "Julia", "Owens",
        "Richard", "Roberts",
        "Adelaide", "Allen",
        "Vivian", "Turner",
        "Evelyn", "Wilson",
        "Adrian", "Cole",
        "Melanie", "Ellis",
        "Catherine", "Perkins",
        "Kelvin", "Campbell",
        "Adam", "Montgomery",
        "Honey", "Edwards",
        "David", "Bennett",
        "Chloe", "Elliott",
        "Maddie", "Foster",
        "Chester", "Robinson",
        "Adelaide", "Lloyd",
        "Lana", "Barrett",
        "Stuart", "Kelley"

    ]
    word_list += chars

    result_username = 'x' * 100  # Init username as dummy words
    while len(result_username) < size or len(result_username) >= 30:  ### Limit of instagram username length is 30
        ### Case 0: Combination of words
        n_word = random.randint(1, 2)
        target_word_list = list(map(lambda x: x.lower(), random.choices(word_list, k=n_word)))

        ### Case 1: Flip each word (5%)
        for word_i, target_word in enumerate(target_word_list):
            if random.random() < 0.03:
                target_word = target_word[::-1]
            target_word_list[word_i] = target_word

        ### Case 2: replace character to 'x' or 'y' or number (3%)
        for word_i, target_word in enumerate(target_word_list):
            for ch_i in range(len(target_word)):
                if random.random() < 0.03:
                    target_char = random.choice(['x', 'y'] + list(map(str, range(10))))
                    target_word = target_word[:ch_i] + target_char + target_word[ch_i + 1:]
            target_word_list[word_i] = target_word

        ### Case 3: Repeat last character (7%, 1~4 times)
        for word_i, target_word in enumerate(target_word_list):
            # if random.random() < 0.07:
            #     target_word = (target_word[0]*random.randint(1,3)) + target_word 
            if random.random() < 0.07:
                target_word += (target_word[-1] * random.randint(1, 4))
            target_word_list[word_i] = target_word

        ### Case 4: Join the words with '.' or '_'
        joining_char = random.choice(['.', '_'])
        result_username = joining_char.join(target_word_list)

        ### Case 5: Add some number to end (30%, 1~999999)
        if random.random() < 0.3:
            if random.random() < 0.6:
                result_username += joining_char
            additional_number_list = []
            number_list = list(map(str, range(10)))
            additional_number_list.append(random.choice(number_list))
            number_list += [''] * 10
            additional_number_list += random.choices(number_list, k=5)
            result_username += ''.join(list(map(str, additional_number_list)))

    return result_username


# Generating a password
def generatePassword(passwd=None):
    if passwd is None:
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(12))
    else:
        return passwd


# Generating a Email
def generatingEmail():
    return ''.join(username() + '@mail.com')


if __name__ == '__main__':
    print(username(size=12, chars=string.ascii_lowercase + random.choice(['.', '_'])))
