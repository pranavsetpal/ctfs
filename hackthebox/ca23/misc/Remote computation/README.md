# Remote computation - easy (maybe)
### The alien species use remote machines for all their computation needs. Pandora managed to hack into one, but broke its functionality in the process. Incoming computation requests need to be calculated and answered rapidly, in order to not alarm the aliens and ultimately pivot to other parts of their network. Not all requests are valid though, and appropriate error messages need to be sent depending on the type of error. Can you buy us some time by correctly responding to the next 500 requests?

In this challenge, we were given docker and had to solve some easy math, but 500 times :|
<image>

We were even given a rules, where we had to account for invalid operands, division by zero, and our answers also had to be within -1337 and 1337, and had to given error messages specific to each of them.
<image>

Here's how my `solved.py` went about for each iteration,
- I took out the mathematical expression and I converted it into a list, such that it was number and then a operand, alternating. Due to the nature of expression, the first and the last value were both numbers.
 - As such, to make sure there wasn't any syntax error, I looped through all the operands, starting from the 2nd element(index 1) till then end skipping one(the number) each time.
 - If the operand wasn't a `+`,`-`,`*`,`/` then I gavea a `SYNTAX_ERR`. In the same loop, if I ever encountered a divide, I made sure the dividend wasn't 0 and gave a `DIV0_ERR` otherwise.
 - If the loop finished successfully, and the expression was valid, I joined it back into string and ran through python's eval() function to automatically calculate the result. I just had to check that the number didn't exceed (+/-)1337, sending a `MEM_ERR` if it did.
 - And that's that! I covered all the rules as outlined by the program, and sent the result.
<image>
 
 Once the loop completed, I got my flag :D
 There is something to looking at computers solve math quick I must say
<video>
