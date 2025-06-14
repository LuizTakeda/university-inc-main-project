#include <Arduino.h>
#include <DHT.h>

#define DHTPIN 22
#define LED_PIN 19

#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

static void read_command();

void setup()
{
  Serial.begin(115200);

  pinMode(LED_PIN, OUTPUT);

  dht.begin();
}

void loop()
{
  read_command();
}

static void read_command()
{
  if (!Serial.available())
    return;

  String str = Serial.readStringUntil('\n');
  str.trim();

  if (str == "light:on")
  {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("OK");
    return;
  }

  if (str == "light:off")
  {
    digitalWrite(LED_PIN, LOW);
    Serial.println("OK");
    return;
  }

  if (str == "humidity:get")
  {
    float humidity = dht.readHumidity();

    if (isnan(humidity))
    {
      Serial.println("Error: Failed to read humidity.");
      return;
    }

    Serial.printf("%.2f%%\n", humidity);
    return;
  }

  if (str == "temperature:get")
  {
    float temperature = dht.readTemperature();

    if (isnan(temperature))
    {
      Serial.println("Error: Failed to read temperature.");
      return;
    }

    Serial.printf("%.2f°C\n", temperature);
    return;
  }

  Serial.printf("UNKNOWN");
}
