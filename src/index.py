from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"""\
Luonnin jälkeen:
Mehuvarasto: {mehua}
Olutvarasto: {olutta}

Olut getterit:
saldo = {olutta.saldo}
tilavuus = {olutta.tilavuus}
paljonko_mahtuu = {olutta.paljonko_mahtuu()}

Mehu setterit:
Lisätään 50.7\
    {mehua.lisaa_varastoon(50.7)}
Mehuvarasto: {mehua}
Otetaan 3.14\
    {mehua.ota_varastosta(3.14)}
Mehuvarasto: {mehua}

Virhetilanteita:
Varasto(-100.0);
{Varasto(-100.0)}

Varasto(100.0, -50.7)
{Varasto(100.0, -50.7)}

Olutvarasto: {olutta}
olutta.lisaa_varastoon(1000.0)\
    {olutta.lisaa_varastoon(1000.0)}
Olutvarasto: {olutta}

Mehuvarasto: {mehua}
mehua.lisaa_varastoon(-666.0)\
    {mehua.lisaa_varastoon(-666.0)}
Mehuvarasto: {mehua}

Olutvarasto: {olutta}
olutta.ota_varastosta(1000.0)
saatiin {olutta.ota_varastosta(1000.0)}
Olutvarasto: {olutta}

Mehuvarasto: {mehua}
mehua.otaVarastosta(-32.9)
saatiin {mehua.ota_varastosta(-32.9)}
Mehuvarasto: {mehua}\
    """)


if __name__ == "__main__":
    main()
