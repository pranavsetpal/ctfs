# Navigating the Unknown - very easy
### Your advanced sensory systems make it easy for you to navigate familiar environments, but you must rely on intuition to navigate in unknown territories. Through practice and training, you must learn to read subtle cues and become comfortable in unpredictable situations. Can you use your software to find your way through the blocks?

I must say, this CTF felt more intended use simply learn how to communicate with blockchain, and me never having tried it, had very little knowledge in the tools used for communication. Fortunately, the staff members provided a very useful README for those new to blockchain, outlining what each was, what we must do, and even recommended a few tools that can be used. After a few difficulties with the web3py module, we went forward with using foundry-rs program.

We had access to 2 docker containers, one for the TCP port via which we could get our instance information, and our flag. It was a simple netcat connection. Another was the RPC URL, the url on which the blockchain was hosted on. Via the netcat docker, we could access the our instance information
<image>

The first thing we did after was to go through the source files and see what our ultimate goal was, which was to set TARGET.updated() to true, and for that we had to call the updateSensors(uint256) function present in Unknown.sol, which the TARGET contract's object was made on, and update the version to 10.
Note: The actual terminology may be wrong. Being used to programming languages, I interpreteted the contract like a Class, and as such think of TARGET as a object of class Unknown.

Foundry-rs provided us with a `cast` bash command, via which we could connect to the blockchain and the contract, and interact with the functions present.
The syntax followed a structure like so:
`cast send <contract_address> <function_name(input_type)> <input> --rpc-url <URL on which Blockchain was hosted> --private-key <Authentication key to validate our request>`
<image>

We could confirm that we solved by using their `cast call` command to run the isSolved function in the Setup contract:
`cast call <contract_address> <function_name()> --rpc-url <URL on which Blockchain was hosted> --private-key <Authentication key>`
<image>

On confirming we netcatted into the TCP connection and could successfully retrieve the flag :)
<image>
