# nehebkaus trap
### In search of the ancient relic, you go looking for the Pharaoh's tomb inside the pyramids. A giant granite block falls and blocks your exit, and the walls start closing in! You are trapped. Can you make it out alive and continue your quest?

> A docker connection

As I connected to the docker, it immediately looked like a restricted shell. This was actually my first restricted shell, and enjoyed solving it :)
<image>

I tried using `whoami`, but I could not run it, the error message was particularly interesting though, rather than a normal bash `command not found`, I received a `name 'whoami' was not found`.
<image>

This gave me the hint that it may a python intepreter I was inside. I tried running 3+4 and it did run successfully, but nothing got printed weirdly. I then tried explicitly printing text and started exploring the 2nd interesting output I was receiving, "Input accepted". This time I used a blacklisted character. To confirm what all characters were blocked, I got all the printable charcters from the separate python shell and copyed it here. There were quite a few that backlisted too.
<image>

The moment I saw that spaces weren't allowed, I was reminded of a video by John Hammond, were he walkthrough-ed a Fiter Evasion, preventing him from using spaces. In that, he displayed a <pyminify> script, that converted python code into `chr(ascii)+chr(ascii)+chr(ascii)...`. This was exactly what I needed! I tried out the script he had made, but it didn't work quite how I wanted, and so I quickly spun up my own version.
<image>

On converting it into the 'obfuscated' version, I tried it out in the challenge provided, the input was accepted, but no output. I thought it may just be evaluating it into a string and nothing after, and so wrapped everything in a exec() function, and just as I suspected, it WORKED!
<image>

I edited the program a bit for it work easily for creating bash commands, and tried `whoami` again and got the output as expected.
<image>

Finally, I could use `ls` and `cat` to get the flag. It was quite fun!
<image>

I even had access to the jail.py file, and I got the script of the shell I was stuck in, it was exciting to see what my predictions of how I may have been locked and the the file itself, confirming that I was indeed in a eval() python function.
<image>
