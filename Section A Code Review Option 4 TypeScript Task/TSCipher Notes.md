
Line 5


Incorrect variable declarations -> "<T>" is not needed, just calling the first variable a string is fine, the shift variable is declared as a string, which is incorrect, it is a number
    const caesar_cipher = (string: string, shift: number) =>
*A little note is it is easier to read code if the closing "}" is below the line of code


line 15 

Intelligent use of the mod function when the shift value is larger than the alphabet, most people overlook this problem when doing this exercise which causes issues or make a much more unneccesarily complicated solution, good work.


line 52

"console.log" not print is how to generate an output using typescript
    console.log(caesar_cipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39));