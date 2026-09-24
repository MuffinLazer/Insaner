#include <DHT11.h>
// libary slop


DHT11 TempHumidPin(2);
// attachs this program to this pin 


void setup() {
  // starts communcation for text 
  Serial.begin(9600);
}

void loop() {
  int temperature = 0;
  int humidiy = 0;
  // ints for later

  int combined = TempHumidPin.readTemperatureHumidity(temperature, humidiy);

  if (combined == 0) {
    Serial.print("TEMPERATURE: ");
    Serial.print(temperature);
    Serial.print("C HUMIDITY: ");
    Serial.print(humidiy);
    Serial.println("%");
  }
}
