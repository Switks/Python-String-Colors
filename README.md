# Python String Colors

Python String Colors allow users to change colors of the string in the terminal. I've created this so I can just make my terminal look just a bit more pretty whenever I use python.(I wondered how to make this soo yeah)

## How to use
Just import the class from `String_Color.py`

`from String_Color import COLOR`

And it's all good to go!

### Example on how to implement is below

```py
from STRING_COLOR import COLOR

print("{COLOR.RGB(237, 145, 33)}CARROT!?")
```

```py
if stupid:
    print(f"{COLOR.RED}{COLOR.BOLD}I'm sad to announce but this is stupid{COLOR.RESET}")
else:
    print(f"{COLOR.GREEN}NO STUPID!!{COLOR.BRIGHT_HIGHLIGHT_YELLOW}(hopefully){COLOR.RESET}")
```

## Documentation

Whenver using ID Highlights(`HIGHLIGHTS_ID`) or ID Colors(`ID`) use the table below as the reference
> Note: Going below 0 or above 255 won't cause any issues(*in theory that is*)
![256 Color table](https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png)

---

All of the information was used from [ANSI Escape Sequences](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)

