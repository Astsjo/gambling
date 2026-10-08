import sys

def press_any_key(prompt="Tryck på valfri tangent för att fortsätta..."):
    print(prompt, end="", flush=True)
    
    if sys.platform == "win32":
        import msvcrt
        msvcrt.getch()
    else:
        # macOS and Linux
        import tty
        import termios
        
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
    print()