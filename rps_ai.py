import random

past_moves = {
    "r": {
        "ro": 1,
        "pa": 1,
        "sc": 1
    },
    "p": {
        "ro": 1,
        "pa": 1,
        "sc": 1
    },
    "s": {
        "ro": 1,
        "pa": 1,
        "sc": 1
    }
}

moves_list = ["r", "p", "s"]
next_move = None

ai_res = "Lose"

wl_database = []

count = 0

def print_stats():
    print("Here are the AI stats:\nWins: " +
    str(wl_database.count("Win")) + "\nLosses: " + 
    str(wl_database.count("Lose")) + "\nTies: " + 
    str(wl_database.count("Tie")) + "\nTotal Rounds: " +
    str(len(wl_database))
    )

while True:
    # MOVE DATABASE SETUP
    for i in range(len(moves_list) - 1, 0, -1):
        if moves_list[i - 1] == "p":
            past_moves[moves_list[i]]["pa"] += 1
        elif moves_list[i - 1] == "s":
            past_moves[moves_list[i]]["sc"] += 1
        elif moves_list[i - 1] == "r":
            past_moves[moves_list[i]]["ro"] += 1

    ran = round(random.uniform(0, 1), 2)

    if ran <= past_moves[moves_list[len(moves_list) - 1]]["ro"]/sum(past_moves[moves_list[len(moves_list) - 1]].values()):
        next_move = "paper"
    elif ran <= past_moves[moves_list[len(moves_list) - 1]]["ro"]/sum(past_moves[moves_list[len(moves_list) - 1]].values()) + past_moves[moves_list[len(moves_list) - 1]]["pa"]/sum(past_moves[moves_list[len(moves_list) - 1]].values()) and ran > past_moves[moves_list[len(moves_list) - 1]]["ro"]/sum(past_moves[moves_list[len(moves_list) - 1]].values()):
        next_move = "scissor"
    else:
        next_move = "rock"


    # LOGIC AND MAIN
    if count == 0:
        print("To enter rock paper or scissor, simply abbreviate it (e.g. Rock becomes r etc). After every 10 rounds, it will show you your stats. To see your stats at any time, simply enter in a 't'. To quit, press 'q'.")

    mq = input("Enter: ")

    match mq:
        case "r":
            if next_move == "rock":
                ai_res = "Tie"
            elif next_move == "scissor":
                ai_res = "Lose"
            elif next_move == "paper":
                ai_res = "Win"
        case "p":
            if next_move == "paper":
                ai_res = "Tie"
            elif next_move == "rock":
                ai_res = "Lose"
            elif next_move == "scissor":
                ai_res = "Win"
        case "s":
            if next_move == "scissor":
                ai_res = "Tie"
            elif next_move == "paper":
                ai_res = "Lose"
            elif next_move == "rock":
                ai_res = "Win"
        case "t":
            print_stats()
        case "q":
            print_stats()
            break
    
    # To make sure the data base and everything doesn't get messed up when t or q is pressed
    if mq == "r" or mq == "p" or mq == "s":
        print(next_move)
        moves_list.append(mq)

        print("AI " + ai_res.lower() + "s.")
        wl_database.append(ai_res)

        count += 1
    
    if count % 10 == 0:
        print_stats()

    print(" ")

print("\nHope you had fun :)\n")
