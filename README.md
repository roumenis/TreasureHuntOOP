Tahová desková hra v Pythonu (OOP)
Projekt simuluje soutěžní deskovou hru, ve které hráč soupeří s několika počítačovými protivníky o dosažení cílového políčka na herním plánu s proměnlivou velikostí.

Hráči se střídají v tazích, hází kostkou, pohybují se po herním plánu, aktivují speciální políčka a mohou si navzájem ovlivňovat pozice prostřednictvím kolizí. Hra je plně ovladatelná z terminálu a je navržena tak, aby bylo snadné přidávat nové herní mechaniky.

Architektura a návrh:
Projekt je postaven na principech objektově orientovaného programování:
-Třídy Player a CPU zapouzdřují stav hráče (pozice, vynechaný tah, extra tah) a logiku pohybu.
-Třída Dice odděluje náhodnost od herní logiky a umožňuje snadné rozšíření (např. speciální kostky).
-Abstraktní třída SpecialTile a její potomci. Každý typ speciálního políčka (Hadí past, Magický portál, Bažina, Zlatá mince) implementuje vlastní chování pomocí polymorfismu.
-Herní smyčka řídí tahy hráčů, kolize mezi hráči, aktivaci speciálních políček a kontrolu vítězství.
-Logika je rozdělena do jasných odpovědností bez nadměrného použití if/else bloků.

Technologie: 
-Python 3
-OOP design
