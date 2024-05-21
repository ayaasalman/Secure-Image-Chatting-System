This project is for a Software Engineering course. It is a preview of a secure image chatting system using Elliptic Curve Cryptography (ECC).

For each image, an "Elliptic" object is created, with data members "a" and "b" corresponding to coefficents in the elliptic curve function. Data member "p" as the prime number defining the finite field. "xg" and "yg" being the coordinates of the point G.

Pixel grouping is done before the encryption to enchance the encryption of the images. Pixel de-grouping is done after the decryption to properly get the same original image after decryption. 

The image is compressed to a size of 146 x 96. And then the image is encrypted using a random point on the curve and the derived public key of the sender.

Entropy analysis and Histogram analysis are used to measure the security of the encryption process.

Decryption was done by reversing the encryption process.

An indivitual file is made for the "Elliptic" class and the encrypt and decrypt functions. 

To run the code, run 'Main.py'.
