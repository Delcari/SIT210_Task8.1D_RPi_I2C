// This #include statement was automatically added by the Particle IDE.
#include <I2CSlaveRK.h>

// Set up this Photon as an I2C device device, address 0x10, with 1 uint32 registers
I2CSlave device(Wire, 0x10, 1);

unsigned long lastCounterUpdate = 0;

void setup() {
    randomSeed(millis());
	device.begin();
}

void loop() {
	// Once per second sends data
	if (millis() - lastCounterUpdate >= 1000) {
		lastCounterUpdate = millis();

        //sends random number between 0-99
		device.setRegister(0, random(100));
	}
}