#!/usr/bin/env python3
"""
Lab 1 Creative Terminal Showcase
Student: Shreyas M H
Experiment: Setting Up, Basic Commands, and Pushing to Remote
"""

import sys
import time

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{CYAN}{BOLD}
  ____ ___ _____   _        _    ____     _ 
 / ___|_ _|_   _| | |      / \\  | __ )   / |
| |  _ | |  | |   | |     / _ \\ |  _ \\   | |
| |_| || |  | |   | |___ / ___ \\| |_) |  | |
 \\____|___| |_|   |_____/_/   \\_\\____/   |_|
{RESET}{YELLOW}>> Experiment 1: Git Setup, Staging, Committing & Remote Push <<{RESET}
"""

def print_animated(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_architecture():
    print(f"\n{BOLD}{MAGENTA}[*] Git 3-Stage Architecture in Action:{RESET}")
    print(f"{CYAN}┌──────────────────────┐      git add       ┌──────────────────────┐      git commit      ┌──────────────────────┐")
    print(f"│  Working Directory   │  ───────────────>  │     Staging Area     │  ─────────────────>  │   Local Repository   │")
    print(f"│   (my_file.txt)      │                    │     (Index Area)     │                      │      (main branch)   │")
    print(f"└──────────────────────┘                    └──────────────────────┘                      └──────────────────────┘")
    print(f"                                                                                                     │")
    print(f"                                                                            git push -u origin main  │")
    print(f"                                                                                                     ▼")
    print(f"                                                                                          ┌──────────────────────┐")
    print(f"                                                                                          │   Remote (GitHub)    │")
    print(f"                                                                                          │ shreyasMH26/lab1     │")
    print(f"                                                                                          └──────────────────────┘{RESET}\n")

def run_quiz():
    print(f"{BOLD}{GREEN}--- Mini Git Knowledge Check (For Lab Evaluation) ---{RESET}")
    questions = [
        ("What command moves changes from Working Directory to Staging Area?", "git add"),
        ("What flag is used with git commit to write an inline message?", "-m"),
        ("What command uploads local commits to a remote server like GitHub?", "git push")
    ]
    score = 0
    for q, ans in questions:
        print(f"\n{BOLD}Q: {q}{RESET}")
        user_ans = input(f"{YELLOW}Your Answer: {RESET}").strip()
        if ans.lower() in user_ans.lower():
            print(f"{GREEN}✓ Correct!{RESET}")
            score += 1
        else:
            print(f"\033[91m✗ Expected: {ans}{RESET}")
    print(f"\n{BOLD}{CYAN}Final Score: {score}/{len(questions)}{RESET}\n")

def main():
    print(BANNER)
    print_animated(f"{GREEN}✓ Student: Shreyas M H (@shreyasMH26){RESET}")
    print_animated(f"{GREEN}✓ Lab Activity: Experiment 1 Completed Successfully!{RESET}")
    show_architecture()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--quiz":
        run_quiz()
    else:
        print(f"{BOLD}Tip:{RESET} Run {YELLOW}python3 terminal_banner.py --quiz{RESET} to test the interactive knowledge check!\n")

if __name__ == "__main__":
    main()
