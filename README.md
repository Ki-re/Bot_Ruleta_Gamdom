<div align="center">
  <img src="logo.png" alt="logo" width="200" height="auto" />
  <h1>Bot Ruleta Gamdom</h1>
  
  <p>
    A bot that simulates betting on the Gamdom roulette using data from the website
  </p>
  
<h4>
    <a href="https://github.com/Ki-re/Bot_Ruleta_Gamdom/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/Ki-re/Bot_Ruleta_Gamdom/issues/">Request Feature</a>
  <span> · </span>
    <a href="https://github.com/Ki-re/Bot_Ruleta_Gamdom/pulls">Contribute</a>
  </h4>
</div>

<br />

<!-- About the Project -->

## About the Project

A simple bot that simulates betting on the Gamdom roulette based on predefined strategies and conditions. The bot uses data from the website but does not interact with it directly.

<!-- Requirements -->

## Requirements

In order to run this script you will need: 

```bash
 pip install selenium
```

Download the chromedriver version that matches your chrome version: 

```bash
https://chromedriver.chromium.org/downloads
```

<!-- Get Started -->

## Get Started

Clone the project

```bash
   git clone https://github.com/Ki-re/Bot_Ruleta_Gamdom.git
```

Set-up the config.py file with your betting strategy and Gamdom account details

```python name=config.py
   presupuesto_inicial = 10
   color_apuesta = 'red'
   # color_apuesta = 'black'
   apuesta_inicial = 0.2
```

Run the script
```bash
   python3 main.py
```

<!-- License -->

## License

Distributed under the no License. See LICENSE.txt for more information.
