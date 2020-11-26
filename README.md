# JIZLD
 The JIZLD Hashing Application v1.0

JIZLED is a program for testing password hashes security against commonly used passwords to prevent brute force attacks

## Getting Started
To install via github, enter the following commands
```
git clone https://github.com/Outlandishh/JIZLD.git
python3 ./JIZLD/main.py
```

Opening the main.py file should immediately open the program to the homepage where you can select the options

### Adding Wordlists

To add your own wordlist, simply add the file to the /resources/ folder in the JIZLD installation folder. When the program needs input from a password file simply provide the filename of the desired wordlist in the resources folder.

### Prerequisites

What things you need to install the software and how to install them

```
Works on windows or linux
Minimum 4GB or RAM 8GB recommended

```

## Running the tests

To test a password you will need to create hash files in option 1 to use for the password hash testing 

### Testing breakdown

Option 1 'Hasher'

```
select option 1 from mainscreen
selecting option 1 will create a MD5 hash file
selecting option 2 will create a sha256 file
selecting option 3 will create a sha512 file
after selecting one of the 3 hash types you will need to decide the password file location (typing nothing will use the default location)
you will then need to select where the hash file will be located (typing nothing will use default location)
it will then ask if you want to salt
the program will then create and save the hash file
```

Option 2 'Password security check'

```
select option 2 from main screen
it will ask if you want to create a hash lookup (if you didn't create one before then you can create one now following same prompts as in option 1)
enter in the password that you would like to test
select the password hash algorithm to test 1 being MD5, 2 being sha256 and 3 being sha512
select the hash file location that is being used
the program will test the password and give the results
```

Option 3 'Hash comparison'

```
select option 3 from main screen
it will ask if you want to create a hash lookup (if you didn't create one before then you can create one now following same prompts as in option 1)
enter in the hash that you would like to test
select the password hash algorithm to test 1 being MD5, 2 being sha256 and 3 being sha512
select the hash file location that is being used
the program will test the password and give the results
```

Option 4 'Enable fancy mode'

```
Enables verbose mode which will produce detailed output for diagnostic purposes
```

Option 5 'Exit'

```
this option exits the program
```


## Built With

* [Python3](https://www.python.org/download/releases/3.0/) - The framework used


## Versioning

For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Daniel Holtham** - *Initial work* - [JIZLD](https://JIZLED.com/DH)
* **Luke Flemming** - *Initial work* - [JIZLD](https://JIZLED.com/LF)
* **Jeremy Landolfo** - *Initial work* - [JIZLD](https://JIZLED.com/JL)
* **Istvan Pal** - *Initial work* - [JIZLD](https://JIZLED.com/IP)
* **Zachary Gothard** - *Initial work* - [JIZLD](https://JIZLED.com/ZG)

people who participated in this project.

## License

This project is absolutely not meant for consumption by the public in any way, shape or form. 
JIZLD takes no responsibility for harmful or malicious use of this code.

## Acknowledgments

* Hat tip to Chisholm for learning resources
