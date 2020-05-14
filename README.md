# Audio generation using 555 timers and frequency doublers

### Working:
1. In this project, we have used six __LM555 timer ICs__ in astable configuration to generate six 6 unique frequencies from the musical scale. We
   have further doubled two of the frequencies to produce notes from the next octave.
2. We have used text files to store the control logic. This logic is produced by a python program based on the
   user-inputs. In real life, we can easily replace the text files with a clock(again using 555 timer) and an EEPROM.
3. A 3:8 decoder is used to produce 8 control signals using the three text files as input.
4. These 8 control signals further control 8 tristate buffers to select one frequency at a time.
5. We have used LTspiceXVII for our simulations. The output voltage is stored into a wav file for further playback.

#### Note:
There seems to be some problem with the XOR gate or comparator which causes the simulation to crash after a particular time period.

### Team members:
1. [Sai Manish Sasanapuri](https://github.com/Sai-Manish)
2. [Tanmay Joshi](https://github.com/tanmayJ527)
3. [Veerendra S Devaraddi](https://github.com/vsdevaraddi)
