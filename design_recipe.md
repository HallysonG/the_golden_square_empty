1. Describe the Problem

users wants to know how long it would take to read the text assuming they can read 200 words per minute.

2. Design the Function Signature



The name of the function.
# function name: words_per_minute

- What parameters it takes, their names and data types.
# Arguments: one number
# data type: integer

- What it returns and the data type of that value.
# return data type = return string with the integer as minutes

- Any other side effects it might have.
# if we cannot divide it equally we might get back a float, so we would then have to find a way to turn that float into an integer.

3. Create Examples as Tests
words_per_minute(200): => "this will take 1 minute(s) to read"

4. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the function to return the right value for the given arguments.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.

