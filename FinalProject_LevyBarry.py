# Barry Levy
# April 21, 2026
# The Dodo Logic Gauntlet (polished: forgiving input, shows correct answers,
# score/inventory updates, and a Play Again loop + “Thanks for playing” exit)

import time

def trigger_chicken():
    print("\n[IMAGE: SCARY CHICKEN JUMP SCARE]")
    print("THAT IS NOT THE RIGHT ANSWER, YOU DODO BIRD!")
    print("PENALTY: A bowl of Frosted Corn Flakes with lukewarm tap water and sea salt.")

def normalize_answer(s: str) -> str:
    """Uppercase + trim + collapse repeated spaces."""
    s = s.strip().upper()
    s = " ".join(s.split())
    return s

def ask_question(round_num, prompt, options, correct_answers, correct_display):
    """
    options: list of tuples like [("A","Elton John"), ("B","Queen"), ...]
    correct_answers: set of acceptable answers (already uppercase/normalized)
    correct_display: string to show the user when they miss (e.g., "B) Queen")
    """
    print(f"\n--- ROUND {round_num} ---")
    print(prompt)
    for letter, text in options:
        print(f"{letter}) {text}")

    answer = normalize_answer(input("Your answer (A/B/C/D or full text): "))
    ok = answer in correct_answers

    if ok:
        print("\n*** DONGGGGG! ***")
        print("CORRECT! A stadium crowd cheers for you!")
    else:
        trigger_chicken()
        print(f"Correct answer: {correct_display}")

    return ok, answer

def print_status(score, total_rounds, inventory):
    print("\n--- STATUS UPDATE ---")
    print(f"Score so far: {score}/{total_rounds}")
    print(f"Inventory: head={inventory['head']}, shoulders={inventory['shoulders']}, stomach={inventory['stomach']}")

def dodo_gauntlet():
    inventory = {"head": "None", "shoulders": "None", "stomach": "Empty"}
    score = 0
    total_rounds = 3

    print("\n=== WELCOME TO THE DODO LOGIC GAUNTLET ===")
    print("Survival is unlikely. Pizza is limited. The chicken is hungry.")
    time.sleep(1)

    # ROUND 1
    ok, _ = ask_question(
        1,
        "Identify the artist: 'I want to ride my bicycle, I want to ride my bike!'",
        [("A", "Elton John"), ("B", "Queen"), ("C", "The Rolling Stones"), ("D", "David Bowie")],
        correct_answers={"B", "QUEEN"},
        correct_display="B) Queen",
    )

    if ok:
        score += 1
        inventory["head"] = "Golden Crown"
        inventory["stomach"] = "NYC Pizza Slice"
    else:
        inventory["head"] = "Dunce Cap"
        inventory["stomach"] = "Salty Cereal"

    print_status(score, total_rounds, inventory)
    time.sleep(1)

    # ROUND 2
    ok, _ = ask_question(
        2,
        "Barnaby the Dodo hosts a 'Midnight Tea Party.' He operates on Inverse Logic.\nWhen should the guests arrive?",
        [("A", "12:00 PM (High Noon)"), ("B", "6:00 AM (Sunrise)"), ("C", "3:00 PM (Nap Time)"), ("D", "Never")],
        correct_answers={"A", "12:00 PM", "12PM", "NOON", "HIGH NOON", "12:00"},
        correct_display="A) 12:00 PM (High Noon)",
    )

    if ok:
        score += 1
        inventory["shoulders"] = "Golden Cape"
    else:
        inventory["head"] = "Damp Cardboard Box"
        inventory["shoulders"] = "Mismatched Wet Socks"

    print_status(score, total_rounds, inventory)
    time.sleep(1)

    # ROUND 3
    ok, _ = ask_question(
        3,
        "To bypass Dodo-Auth, you must provide 'Absurd Simplicity'.\nWhat is your Secondary Identification Factor?",
        [
            ("A", "Type '123456'"),
            ("B", "Stare at webcam for 47 seconds"),
            ("C", "Whisper pizza toppings into USB port"),
            ("D", "Throw the PC into a fountain"),
        ],
        correct_answers={
            "C",
            "WHISPER PIZZA TOPPINGS INTO USB PORT",
            "WHISPER PIZZA TOPPINGS INTO THE USB PORT",
            "WHISPER PIZZA TOPPINGS",
        },
        correct_display="C) Whisper pizza toppings into USB port",
    )

    if ok:
        score += 1
        inventory["stomach"] = "Pizza and Deep-Fried Oreos"
    else:
        inventory["stomach"] = "Plastic Computer Keys"

    # FINAL RESULT
    print("\n=== THE GAUNTLET IS OVER ===")
    print(f"Final Score: {score}/{total_rounds}")

    print("Final Inventory Check:")
    for item, value in inventory.items():
        print(f"- {item.capitalize()}: {value}")

    if score == 3:
        print("\nPERFECT VICTORY! You are the Grand Dodo Emperor!")
    elif score == 2:
        print("\nSOLID SURVIVAL! You are a Respected Dodo Knight.")
    elif score == 1:
        print("\nBARELY ALIVE! You are a Shaken Dodo Squire.")
    else:
        print("\nTOTAL WIPEOUT! The Chicken reigns supreme.")

def main():
    while True:
        dodo_gauntlet()
        again = normalize_answer(input("\nPlay again? (Y/N): "))

        if again in ("Y", "YES"):
            print("\nRebooting the Gauntlet...")
            time.sleep(1)
            continue

        print("\nThanks for playing! Game over. The chicken watches you leave.")
        break

if __name__ == "__main__":
    main()