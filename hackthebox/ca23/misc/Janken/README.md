# Janken - medium (maybe)
### As you approach an ancient tomb, you're met with a wise guru who guards its entrance. In order to proceed, he challenges you to a game of Janken, a variation of rock paper scissors with a unique twist. But there's a catch: you must win 100 rounds in a row to pass. Fail to do so, and you'll be denied entry.

For this challenge, we were provided with docker and the binary files.

The goal for this challenge was a win a pame of rock, paper and scissors a 100 times in a row.
<image>
not many rules, but we do have the binary file with us.
If we open it up in ghidra, we can decompile the program into a c code, and look around for any exploits we may exploit.

This challenge was particularly dreadful for me. The solution I came up with "worked", but just barely. I'll let some of my failed attempts help visulaize the hour long trauma.
<video>

## Not my Solution
I saw how it's actually meant to be solved in this <video_link>, and wanted to include it in here as I had gotten across this before, and quite funny too. It exploited a logic bug while checking if we won the game, by using a strstr() function to find if the winning choice (rock, paper or scissors, depending on the round), was present in our inputted string.
<image>
As the size of our input buffer is 32 bytes long, we could input `rockpaperscisscors`, and since the strstr() function would always find the winning choice in our input, we would always win xD


# My Solution
I, on the other hand, saw that the game() function was setting the rand seed with respect to the time, and worked on replicating it on Python.
<image>
The `ctypes` module actually allowed to run libc functions and get our output, ensuring that the random generator I got in Python used the same function as the given program.
<image>
After that, it was simply a case of sending the output the to program, and waiting for the flag. I tested out program locally on the binary they provided, and it worked wonderfully, but as soon as I connected it to the docker, it started to fail pseuro-randomly, sometimse after 5,10,30, even 60 iterations! My running assumption is that the time lag in getting the input, calculating the winning result, and sending it back resulted in errors.
I even created a test script on my machine and ran it even TEN thousand to make sure the solution I made was resiliant to change in seconds, as the local binary did finish 100 games very fast.

Any case, after almost an hour of trying, and 2 minutes after creating a support ticket, I got the flag!!
