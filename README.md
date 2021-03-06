# Audio-Watermarking-using-MATLAB

In this project, we are encrypting an image using a 4-digit integer key and encoding it into an audio file using LSB (Least Significant Bit) encoding method. We convert the encrypted image into its binary equivalent and replace the LSB bit in the binary form of the audio file. This results in a watermarked audio file without any size changes and minimal audio quality loss thus generally undetectable. The random key is generated and sent to the intended recipients' email id and the watermark image can be only retrieved using this key from the watermarked audio file. An UI has been developed using Python for the application with encryption and decryption functions implementedin MATLAB.

## Methodology
LSB encoding provides an easy way to mask information into any binary data. We convert the given audio file into a 16-bit binary array and replace the LSB bit with the encrypted image binary information.
For encryption, we generate a 4-digit Integer Key (PIN) and multiply the double image data with the Key integer and convert it into binary. This data is then written on the audio track after 2 x Key length. The image dimensions are then acquired and the dimensions are also then encrypted and written into the audio file. To optimize the code the binary length of the encrypted audios individual element is used to iterate over the encryption loop and the length is also embedded into audio for faster encryption and decryption. Once the encoded audio with encrypted watermark is written back to the folder in .wav format an email is sent to the desired recipient using SMTP protocol. 

![Proposed Encryption Diagram](https://raw.githubusercontent.com/HKpro2090/Audio-Watermarking-using-MATLAB/main/Encryption%20Detailed.png?raw=true)

The decryption program gets the input key from the user and starts reading from the audio from 2 x Key length of the binary converted encoded audio. First, the image dimensions and audio elements binary length are read from the audio file and decrypted using the key. Then the image data is decrypted to obtain the original image. A Graphical User Interface created using Python and Tkinter library is provided to the user to choose the source files and enter recipient email id, encoded audio filename, decryption key, and decrypted watermark image filename.

![Proposed Decryption Diagram](https://raw.githubusercontent.com/HKpro2090/Audio-Watermarking-using-MATLAB/main/Decryption%20Detailed.png?raw=true)

## References
- https://www.mathworks.com/matlabcentral/fileexchange/55123-watermarking-an-image-into-an-audio-file-using-least-significant-bit-lsb-method
- https://www.geeksforgeeks.org/python-gui-tkinter
- https://www.instructables.com/id/Call-MATLAB-Script-and-Function-From-Python/
- MATLAB help library

