#include <Arduino.h>

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  if (Serial.available())
  {
    String str = Serial.readStringUntil('\n');

    if (str == "ligar:luz")
    {
      Serial.println("OK");
    }

    if (str == "desligar:luz")
    {
      Serial.println("OK");
      // Serial.println("desligar luz");
    }

    if (str == "abrir:porta")
    {
      Serial.println("OK");
      // Serial.println("abrir porta");
    }

    if (str == "fechar:porta")
    {
      Serial.println("OK");

      //      Serial.println("fechar porta");
    }
  }
}