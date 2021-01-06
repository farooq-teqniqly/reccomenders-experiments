from collections import Counter
from data import users_interests


def get_popular_interests():
    return Counter(
        interest for user_interests in users_interests for interest in user_interests
    ).most_common()


def most_popular_new_interests(user_interests, max_results=5):
    suggestions = [
        (interest, frequency)
        for interest, frequency in get_popular_interests()
        if interest not in user_interests
    ]

    return suggestions[:max_results]


def main():
    print(most_popular_new_interests(users_interests[0]))
    print(most_popular_new_interests(users_interests[3]))


if __name__ == "__main__":
    main()
