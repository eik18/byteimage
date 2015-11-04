# README.md
The purpose of this tool is to create an image of binary files at the byte level, then calculate entropy.  It is helpful in depiciting how a binary is constructed and measuring its level of compression/encryption.  

## How to use the tool
Executing the tool without option will yield a brief intro how to run the tools.  Executing a `--help` will give the following more detailed instructions.
> `$byteimage.py [-c|-g] [-e] <input_file> <output_file>`  <p>

##Example execution<br>
This example produces a color image and calculates entropy of the \bin\bash binary:<br>
Command: `$python byteimage.py -ce /bin/bash bashimage-color.png`<br>
Results: <br>
> `Generating Color Image...this may take a minute or so for large files`<br>
  `Calculating Entropy`<br>
  `Entropy Estimate: 2.11317354104`

Example Image:<br>
![Example Image](bashimage-color.png "Example Image")

##Interpreting Results
###How to read the picture
The picture is produced by converting each byte into an octal, then to its integer value based on ASCII.  Every pixel represents one byte, with the color progressing from red, to green, to blue as the value increases.  The purpose of the picture is to show the code stucture.<p>
###How to read the entropy value
Entropy in this context means how unique are the contents of file.  As file uniqueness goes up, the odds that it is encrypted or compressed also rises.  For example, the Bash execute above has an entropy of 2.11.  If you compress it as a zip, it's entropy, or presence of unique values, increases to 2.27, roughly equal to a file filled with pseudorandom numbers.  
