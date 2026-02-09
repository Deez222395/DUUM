#!/usr/bin/env python3
"""
DUUM ASCII logo generator (DOOM-style look using pyfiglet).
No copyrighted assets — only free ASCII art font.
"""

import pyfiglet

def main():
    # Create a Figlet object with a bold, blocky font
    font = pyfiglet.Figlet(font='slant')
    
    # Fixed text "DUUM"
    ascii_art = font.renderText("DUUM")
    
    print(ascii_art)

if __name__ == "__main__":
    main()
