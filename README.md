# Caesar Code
> This little sample was based on [Codenation](https://www.codenation.dev/)'s first challenge. You can find the full original description of it in another repositories like [this](https://github.com/Collumbus/CodeNation-Desafio-AceleraDev-Stone-2020) one.

## About ROT-N cipher
> According to [dCode](https://www.dcode.fr/rot-cipher):

Rot-N/Rot cipher is a simple character substitution based on a shift/rotation of N letters in an alphabet. E.g. one letter is replaced by another (always the same) that is located further (exactly N letters further) in the alphabet.

This is the basis of the famous **Caesar code** and its many variants modifying the shift. The most popular variant is the ROT13 which has the advantage of being reversible with our 26 letters alphabet (the encryption or decryption operations are identical because 13 is half of 26).

<details><summary><b>Notes</b></summary>

* Wrote in python 3.6.
* Requires [requests](https://requests.readthedocs.io/en/master/user/install/#install).
* Will be created a `answer.json` file.
* All letters are going to be converted to lowercase.
* Numbers and ponctuation remain the same.

   **Message:** `Tonight on 'Is There?' we examine the question, 'Is there a life after death?' And here to discuss it are three dead people.`
   
   **Coded:**   `wrqljkw rq 'lv wkhuh?' zh hadplqh wkh txhvwlrq, 'lv wkhuh d olih diwhu ghdwk?' dqg khuh wr glvfxvv lw duh wkuhh ghdg shrsoh.`
   
</details>

## Usage

### Using only ROT-N Coder/Decoder

<details><summary><b>Show detailed instructions</b></summary>
  <p align="center">
    <img width="460" height="300" src="https://media.giphy.com/media/fVhLa8rc2xGzLm76gb/giphy.gif">
  </p>
</details>

### Submitting Challenge's Answer
Set your token, and run `./main.py`.

<details><summary><b>Show detailed instructions</b></summary>
  
1. In the `main.py` file, past your token:
```python
token = 'MYTOKEN123' #PAST your token here
```
2. Run the `main.py` file:
```console
foo@bar:~$ python3 main.py
```
3. Receive your score:
```
OK: {score: 100}
```

</details>

   
