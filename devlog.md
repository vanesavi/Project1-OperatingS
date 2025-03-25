Initial Commit ~~~

Mar. 3 4:45pm
Starting the project. It’s three parts: logger, encryption, and a driver that runs everything and connects them together. I’ll use Python for easier management and development. For now just getting familiar with how it all fits together, and its requirements. Will try to map out the structure next.

Mar. 10 7:50pm
started working on the driver today... mostly just got the logging part working, calling the logging.py from inside the driver using subprocess, passed it a quick INIT_COMMENT and QUIT just to see if it logs right — and yeah it did. didn't wire up anything else yet but feels like a good first test to make sure files connect properly.

Mar. 14 10:30am
added the main menu today with all the command options (password, encrypt, decrypt, history, quit).
for the password part — decided not to log or store them in a file since that’s kinda sketchy security-wise... just keeping them in memory using a set. also made it so the user only sees the password history menu if there’s already at least one password in the set... otherwise it just goes straight to entering a new one. tested just typing through the menu to make sure things don’t crash lol.

Mar. 16 3:40pm
wired up the encryption stuff using the functions from before... tried testing it by just hardcoding a password and an input and printing the result. 
made this helper where u can either type a new string or reuse something from the log (reads ENCRYPT/DECRYPT lines)... just testing if i can read the log properly and it worked. password stuff still kept in memory only — nothing gets written to the log for security. logs now show both the input and the result for encryption/decryption.

Mar. 18 9:10pm
tried to encrypt something and realized i didn’t set a password yet ... so i added a check — now it won’t let u encrypt or decrypt unless there’s a password already set. throws a little error msg and skips... feels more real. 
also added back the logic so the password history menu only shows if there's actually history — otherwise it skips it and just asks for a new one. logs still never show the password, just actions like [SET_PASSWORD] and [ENCRYPT] etc.

Mar. 20 4:00pm
made a proper history view — just reads from the log and prints out all the encrypts and decrypts. 
added validation so inputs have to be only letters — stuff like “Hello123” gives a warning and makes u retype. ran the driver a few times to test different combos — stuff feels more stable now.

Mar. 21 2:00pm
added more checks today — mainly around input validation again.
was able to trigger some weird behavior by spamming random symbols lol so now if input isn’t strictly letters it gives an error right away. 
also added a pause (input prompt) after results print so the screen doesn’t jump back to the menu too fast.

Mar. 22 6:30pm
cleaned up a few things... was repeating the Y/N "use history?" prompt so i just turned it into a function. 
tested a few full runs: set password, encrypted, decrypted, checked history — logs look solid. right now i just use subprocess every time i write to the log, not persistent but it works.

Mar. 23 11:30am
did another full test run — this time trying a mix of valid and invalid encrypt/decrypt inputs, using both new strings and history. 
noticed that reselecting from history makes testing way faster. thought about maybe color coding the output but left it as is for now. everything looks solid.

Mar. 24 12:20pm
thinking more about how logging and encryption were supposed to be persistent programs taking stdin — mine don’t really do that right now.
for logging i just run it each time with subprocess and send one message with QUIT at the end... technically works and keeps it simple, but not 100% like the spec. tried to sketch out what it’d look like to have a real pipe open but not sure if i wanna go down that rabbit hole right now.

Mar. 24 3:45pm
realized encryption is supposed to be a whole separate program too but i kinda have it all inside the driver rn. 
not sure i’m gonna change that this late unless i really have to... everything works, it's just not split into 3 running processes. also tested encrypting a few things without history — works fine. and tested again by reusing values from log history — also works, pulls the last words from ENCRYPT/DECRYPT lines.

Mar. 24 6:00pm
honestly feels pretty complete now. added small things like better menus, error msgs if password not set, history reselect, input checking... 
all that made testing smoother. ran the full thing again a couple times — tried weird inputs, checked the log file after, results look good. might stop here unless something breaks last minute.

Mar. 24 9:00pm
last pass through the code before submitting. made sure all the log entries are clean — they follow the format exactly with timestamps and action tags. 
all the edge cases like trying to encrypt with no password, or entering bad inputs, are covered. ran a couple more tests with different log file names just to be sure it’s not hardcoded anywhere.

