import discord
import textwrap

def get_embed_fisica_2_pc1():

    lista = [get_embed_fisica_2_pc1_1(), get_embed_fisica_2_pc1_2()]

    return lista

def get_embed_fisica_2_pc2():

    lista = [get_embed_fisica_2_pc2_1(), get_embed_fisica_2_pc2_2()]

    return lista

def get_embed_fisica_2_pc3():

    lista = [get_embed_fisica_2_pc3_1(), get_embed_fisica_2_pc3_2()]

    return lista

def get_embed_fisica_2_pc4():

    lista = [get_embed_fisica_2_pc4_1(), get_embed_fisica_2_pc4_2()]

    return lista

def get_embed_fisica_2_exparcial():

    lista = [get_embed_fisica_2_exparcial_1(), get_embed_fisica_2_exparcial_2(), get_embed_fisica_2_exparcial_3()]

    return lista

def get_embed_fisica_2_exfinal():

    lista = [get_embed_fisica_2_exfinal_1(), get_embed_fisica_2_exfinal_2(), get_embed_fisica_2_exfinal_3()]

    return lista

def get_embed_quimica_1_laboratorios_2021_II():
    embed = discord.Embed(
        title="Test de Laboratorios de Química - 2021-II",
        description=textwrap.dedent(f"""\
            - [1°TEST DE LABORATORIO 2021-2.pdf](https://drive.google.com/file/d/1MB8K7cfiY_ggvqlO6q3Xq-qi-aUNYdr7/view?usp=drive_link) 
            - [2°TEST DE LABORATORIO 2021-2.pdf](https://drive.google.com/file/d/1YWuy5lt9Q6-YvzHZ5b8hK4bqwMHmY3qP/view?usp=drive_link)
            - [3°TEST DE LABORATORIO 2021-2.pdf](https://drive.google.com/file/d/19ogYekGFiiEVl7qRTu_gjqZoXhGzRBek/view?usp=drive_link)
            - [4°TEST DE LABORATORIO 2021-2.pdf](https://drive.google.com/file/d/1MEoENWN5NBB70WBe-NLrSP3n6j1KGPfz/view?usp=drive_link)
            - [5°TEST DE LABORATORIO 2021-2.png](https://drive.google.com/file/d/1YcUPfwo-wU_hrsum1Tk7fBAY77CHrCo5/view?usp=drive_link)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_fisica_2_pc1_1():
    embed = discord.Embed(
        title="1ra PC - Física 2",
        description=textwrap.dedent(f"""\
            - [PC1 BFI05 M 2023-3.pdf](https://drive.google.com/file/d/1Kk0Xpa9Ev0PnHIL-NwC_IWqN6gd31Yso/view?usp=sharing)
            - [PC-1 23-3 (Prof Chirinos).pdf](https://drive.google.com/file/d/18g5Ao1sby25A84Iczl20vTkhefSXrF76/view?usp=sharing)
            - [PC1 BFI05 2023-2.pdf](https://drive.google.com/file/d/1_ZrKLonvkK7kd7IPbQsdjZD-vdFONUOC/view?usp=sharing)
            - [PC1 BFI05 2023-1.pdf](https://drive.google.com/file/d/16AJsVniMFXpvxNh2CPBpWjXzYiD9zVA3/view?usp=sharing)
            - [PC-1 2022-3.pdf](https://drive.google.com/file/d/1cbMMwQjXi4VIF36zU5CupYDnIeGY7Alw/view?usp=sharing)
            - [PC-1 2022-2.pdf](https://drive.google.com/file/d/1MjEKdua2dz83kuWVC4LXF_H0UWM0x45A/view?usp=sharing)
            - [PC-1 2022-1.pdf](https://drive.google.com/file/d/13LbtjazyoAtfym3msd3BZ_zOwkx1BuJ6/view?usp=sharing)
            - [PC-1 2021-2 (Prof. Roy Secc. Q).pdf](https://drive.google.com/file/d/1zBiRHqh51ktmajxZPOpcNJvYOcKbARs6/view?usp=sharing)
            - [PC-1 2021-2 (Prof. Roy Secc. N).pdf](https://drive.google.com/file/d/1Z0FrGdX857Aau64XbgFa-Ihh4ziAhMLg/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc1_2():
    embed = discord.Embed(
        title="1ra PC - Física 2",
        description=textwrap.dedent(f"""\
            - [PC-1 2021-2 (Prof. Durand y Llamoja Secc. M).pdf](https://drive.google.com/file/d/1j_pNPAuDEdsPvy-Aq-ZP787i0LTnw7wE/view?usp=sharing)
            - [PC-1 2021-1 (Prof. Alva).pdf](https://drive.google.com/file/d/1nZnBzXYJt_SK6IA3bjbh7cwvIfwTfMCW/view?usp=sharing)
            - [PC-1 2021-1 (Prof. Durand).pdf](https://drive.google.com/file/d/1-WXJfN0S05EG9_2ZhTx9a7rnjyIxFVOB/view?usp=sharing)
            - [PC-1 2020-2 (Prof. Pauyac).pdf](https://drive.google.com/file/d/1kPA0K6oGh-ZS-Vel_bdhVfer16bgpAL8/view?usp=sharing)                       
            - [PC-1 2020-2 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1hZDHR8vrZl9LnVIiOp9ukgc8zCDWbtOh/view?usp=sharing)
            - [PC-1 2020-2 (Prof. Farfan).pdf](https://drive.google.com/file/d/16orgSWNwkrhUZqFaxSrNpiqN-_1-wmK0/view?usp=sharing)
            - [PC-1 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/1H-qiGa4St9NbbprxzzIf9haq76oyKfNE/view?usp=sharing)
            - [E.Continua PC-1 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/1GapISy22QTl4W9sU5vWz6zPHvwZU3BWm/view?usp=sharing)
            - [PC-1 2020-1 (Prof. Azuero).pdf](https://drive.google.com/file/d/1cvd6GK_rVWtfCjyapOJ3iy0OlUOw59qE/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc2_1():
    embed = discord.Embed(
        title="2da PC - Física 2",
        description=textwrap.dedent(f"""\
            - [PC2 BFI05 M 2023-3.pdf](https://drive.google.com/file/d/1n1k6pQ-EnPxvXuFARWZV6boJVlso4Ayw/view?usp=sharing)
            - [PC2 BFI05 2023-2.pdf](https://drive.google.com/file/d/1NoKz-EuweiFsDF1w_tH0WkrpHKUillXb/view?usp=sharing)
            - [PC2 BFI05 2023-1.pdf](https://drive.google.com/file/d/1fzHwvZUZITcRpw37O2EL2jB0qAyMhkMv/view?usp=sharing)
            - [PC-2 2022-3.pdf](https://drive.google.com/file/d/1fzHwvZUZITcRpw37O2EL2jB0qAyMhkMv/view?usp=sharing)
            - [PC-2 2022-2.pdf](https://drive.google.com/file/d/1fzHwvZUZITcRpw37O2EL2jB0qAyMhkMv/view?usp=sharing)
            - [PC-2 2022-1.pdf](https://drive.google.com/file/d/1fzHwvZUZITcRpw37O2EL2jB0qAyMhkMv/view?usp=sharing)
            - [PC-2 2021-2 (Prof. Roy Secc. Q).pdf](https://drive.google.com/file/d/1v7pGYnFR5YETBoXGVD1put5wtM-5goRE/view?usp=sharing)
            - [PC-2 2021-2 (Prof. Roy Secc. N).pdf](https://drive.google.com/file/d/1CNX4yD8mqvBxGRwlajfZsfy4khTaqrVs/view?usp=sharing)
            - [PC-2 2021-2 (Prof. Durand y Llamoja Secc. M).pdf](https://drive.google.com/file/d/1rM4xi3Jl7om-wdUikVi4AgMswehqWSFD/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc2_2():
    embed = discord.Embed(
        title="2da PC - Física 2",
        description=textwrap.dedent(f"""\
            - [PC-2 2021-1 (Prof. Alva).pdf](https://drive.google.com/file/d/10mNS_obj5N4jdBSbgF_R0_rHdxzsAcwF/view?usp=sharing)
            - [PC-2 2021-1 (Prof. Durand).pdf](https://drive.google.com/file/d/1KYlvGI0M66FbozT4WhkeUjA_saO-ybgp/view?usp=sharing)
            - [PC-2 2020-2 (Prof. Pauyac).pdf](https://drive.google.com/file/d/1kPA0K6oGh-ZS-Vel_bdhVfer16bgpAL8/view?usp=sharing)
            - [PC-2 2020-2 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1hZDHR8vrZl9LnVIiOp9ukgc8zCDWbtOh/view?usp=sharing)
            - [PC-2 2020-2 (Prof. Farfan).pdf](https://drive.google.com/file/d/16orgSWNwkrhUZqFaxSrNpiqN-_1-wmK0/view?usp=sharing)
            - [PC-2 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/1H-qiGa4St9NbbprxzzIf9haq76oyKfNE/view?usp=sharing)
            - [E.Continua PC-2 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/1GapISy22QTl4W9sU5vWz6zPHvwZU3BWm/view?usp=sharing)
            - [PC-2 Quiz 2020-1.pdf](https://drive.google.com/file/d/1mUBgqOb3B2qlE9DroxvOCkbIolJt-1bw/view?usp=sharing)
            - [PC-2 2020-1 (Prof. Azuero).pdf](https://drive.google.com/file/d/1sLKy2r8KcJvArgNuWCmfYLXNfdJ9koQt/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc3_1():
    embed = discord.Embed(
        title="3ra PC - Fisica 2",
        description=textwrap.dedent(f"""\
            - [PC3 BFI05 M 2023-3.pdf](https://drive.google.com/file/d/1Rf-l6liNtnX6QgSjB14WwcpZejKXf1GO/view?usp=sharing) 
            - [PC3 BFI05 2023-2.pdf](https://drive.google.com/file/d/1FrFX6ieDstOKFUvlKkpLwBhwn6_LHWbP/view?usp=sharing)
            - [PC3 BFI05 2023-1.pdf](https://drive.google.com/file/d/1HhMJf749lKNEEXpG2lUbmQ8s6OiZl2jU/view?usp=sharing)
            - [PC-3 2022-3.pdf](https://drive.google.com/file/d/1tHs4YnyyJF_AzhctJbFHNQ5WsrQnrSgL/view?usp=sharing)
            - [PC-3 2022-2.pdf](https://drive.google.com/file/d/1ykZUMiZJ67dXg2G4Ras2-BEEahtEgFEm/view?usp=sharing)                       
            - [PC-3 2022-1.pdf](https://drive.google.com/file/d/1Lbq79XbtGkDydxf_7XMK5H1AcTtr-N0Q/view?usp=sharing)
            - [PC-3 2021-2 (Prof. Roy Secc. Q).pdf](https://drive.google.com/file/d/17w1g3Uh66SJcZrhXJKIC1mzTM_-F0U8A/view?usp=sharing)                      
            - [PC-3 2021-2 (Prof. Roy Secc. N).pdf](https://drive.google.com/file/d/1JJSq438bl7SXiiuvWSzRH5umKLaKpVta/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc3_2():
    embed = discord.Embed(
        title="3ra PC - Fisica 2",
        description=textwrap.dedent(f"""\
            - [PC-3 2021-2 (Prof. Durand y Llamoja Secc. M).pdf](https://drive.google.com/file/d/11r_PJImMe7UrJio2-PUJsjcsRUaEeUZL/view?usp=sharing)
            - [PC-3 2021-1 (Prof. Alva).pdf](https://drive.google.com/file/d/1jn-tbyr0l7eLWjPWPvd_ySdE9rmmayOA/view?usp=sharing)
            - [PC-3 2021-1 (Prof. Durand).pdf](https://drive.google.com/file/d/1W4SWBBn-xHREH7kt-bq3Fkdbpu7YlDY0/view?usp=sharing)
            - [PC-3 2020-2 (Prof. Pauyac).pdf](https://drive.google.com/file/d/1TbfN9Wa6gOqyVFxbQJDEGnP2tQMYlpl3/view?usp=sharing)
            - [PC-3 2020-2 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1wyVIh39zR8VPUZuEP6RUqrHaInJL6-Go/view?usp=sharing)
            - [PC-3 2020-2 (Prof. Farfan).pdf](https://drive.google.com/file/d/1xSDt-7wJw-3WitTaeWW90jTvGnggyPNj/view?usp=sharing)
            - [PC-3 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/1j7365TZ32ODrRSEjUp5QEC8eortWhhBE/view?usp=sharing)
            - [PC-3 2020-1 (Prof. Azuero).pdf](https://drive.google.com/file/d/1663gmcGLxqF79p4EUWT5nwSuBjUzUnXt/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_fisica_2_pc4_1():
    embed = discord.Embed(
        title="4ta PC - Física 2",
        description=textwrap.dedent(f"""\
            - [PC4 BFI05 M 2023-3.pdf](https://drive.google.com/file/d/1SUW1z3DEwpxEhRdB5Se8fF7RzbAVVGna/view?usp=sharing)
            - [PC4 BFI05 2023-2.pdf](https://drive.google.com/file/d/1sSIFals02rHOV5H5Mu9944AGfAl1IiY1/view?usp=sharing)
            - [PC4 BFI05 2023-1.pdf](https://drive.google.com/file/d/1TV2ryM2pjTRPsI6MKENa2PYzPSy-bvkh/view?usp=sharing)
            - [PC-4 2022-3.pdf](https://drive.google.com/file/d/1YnoR0ZNC5-Qx8rj1DZ8MNnhNcGv3nqZY/view?usp=sharing)
            - [PC-4 2022-2.pdf](https://drive.google.com/file/d/1_rJNoeQ2IOVcmPPLbrcjz87RSi2nlQ8y/view?usp=sharing)                       
            - [PC-4 2021-2 (Prof. Roy Secc. Q).pdf](https://drive.google.com/file/d/13gXj8lSWhdUgUAvpkl4zai-8qA4ZOokn/view?usp=sharing)
            - [PC-4 2021-2 (Prof. Roy Secc. N).pdf](https://drive.google.com/file/d/1bDFuQ4alZ20ONZYQ51XGTyI-PLY8oo0x/view?usp=sharing)
            - [PC-4 2021-2 (Prof. Durand y Llamoja Secc. M).pdf](https://drive.google.com/file/d/1VVGoIjIHD6UqLjY8TJFMe65ZRht5bbXE/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc4_2():
    embed = discord.Embed(
        title="4ta PC - Física 2",
        description=textwrap.dedent(f"""\
            - [PC-4 2021-1 (Prof. Alva).pdf](https://drive.google.com/file/d/1rZ_bI0WZBvfTt7oWm49giFZ4ACjR55yQ/view?usp=sharing)
            - [PC-4 2021-1 (Prof. Durand).pdf](https://drive.google.com/file/d/1sSVEW9h49hflo6GpMYFbtCqOsa1hfBK9/view?usp=sharing)
            - [PC-4 2020-2 (Prof. Pauyac).pdf](https://drive.google.com/file/d/1knRxB18liFx8jQdkwyofTJl7_02SUSra/view?usp=sharing)
            - [PC-4 2020-2 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1sE0b1EaiyJD8t4wh6iRDj1_46QlRshnw/view?usp=sharing)
            - [PC-4 2020-2 (Prof. Farfan).pdf](https://drive.google.com/file/d/1sk8AFin1RxI9AEfIxiiinyBi92uxQKLs/view?usp=sharing)
            - [PC-4 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/1xvBGx5UkFeHBL17v4DHY4xVEzTokX7HZ/view?usp=sharing)
            - [PC-4 Quiz 2020-1.pdf](https://drive.google.com/file/d/1sJFQfty0iFdINrGOjgHA6tyhzdYsZQ8P/view?usp=sharing)
            - [PC-4 2020-1 (Prof. Azuero).pdf](https://drive.google.com/file/d/1ygO8BkXUJB8YGNt5jhIpZHG5zvC7O84u/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc5():
    embed = discord.Embed(
        title="5ta PC - fisica_2",
        description=textwrap.dedent(f"""\
            - [PC-5 2021-2 (Prof. Durand y Llamoja Secc. M).pdf](https://drive.google.com/file/d/1L8bhDoPOLCGltirTEXn1mkpmEd9hTk0e/view?usp=sharing)                     
            - [PC-5 2022-1.pdf](https://drive.google.com/file/d/1UAkwBBeP4RQgwksvRjGZ93mSCnoRmkZ9/view?usp=sharing)
            - [PC-5 2022-2.pdf](https://drive.google.com/file/d/1QoUVKWE3KsDT_YwfY8R5sr9HG_VvPptC/view?usp=sharing)                       
            - [PC5 BFI05 2023-1.pdf](https://drive.google.com/file/d/1VAK5lV62ibOoJuFMIbRDimzJJimMtVVx/view?usp=sharing)
            - [PC5 BFI05 2023-2.pdf](https://drive.google.com/file/d/1uc8ljjzZpotDs8gPBN0to2SvNyE5SLt0/view?usp=sharing)
            - [PC5 BFI05 A 2023-2.pdf](https://drive.google.com/file/d/1KzgEZecSMqs4LhHPRPi4wY8AbdoblUfd/view?usp=sharing)
            - [PC5 BFI05 M 2023-3.pdf](https://drive.google.com/file/d/15T_112Z35dKtcf0HLNzYeBnc6uz9ncKp/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_exparcial_1():
    embed = discord.Embed(
        title="Ex. Parciales - fisica_2",
        description=textwrap.dedent(f"""\
            - [PARCIAL BFI05 M 2023-3.pdf](https://drive.google.com/file/d/1hWPYPYUSG5zoiCAEq0_BIn3My4Jt7bPz/view?usp=sharing)
            - [PARCIAL BFI05 2023-2.pdf](https://drive.google.com/file/d/1RVYS3WWxfJnZywREdsEfdEN-loMVWEJs/view?usp=sharing)
            - [PARCIAL BFI05 2023-1.pdf](https://drive.google.com/file/d/1Azipdpn513Ea0m3CJWziqEFhzCfGhntc/view?usp=sharing)
            - [PARCIAL 2022-3.pdf](https://drive.google.com/file/d/1E5eRcWxyjdAu9OhwHmnbitM9pRDzsIpT/view?usp=sharing)
            - [PARCIAL 2022-2.pdf](https://drive.google.com/file/d/1LThgej7cp7_VXcBddvPukSu5GfabvB4w/view?usp=sharing)                       
            - [PARCIAL 2022-1.pdf](https://drive.google.com/file/d/1ZVetWQZgMMLLZKyJMH-V9jWsa4HaXTZS/view?usp=sharing)
            - [PARCIAL 2021-2 (Prof. Roy Secc. Q).pdf](https://drive.google.com/file/d/1cwMVIwqR8E_yEj_ZqCvG_EEQE1_JzeEJ/view?usp=sharing)                      
            - [PARCIAL 2021-2 (Prof. Roy Secc. N).pdf](https://drive.google.com/file/d/1OyGB3aFhZDVkbY-JpQ_-heX_BHxeXSFX/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_exparcial_2():
    embed = discord.Embed(
        title="Ex. Parciales - fisica_2",
        description=textwrap.dedent(f"""\
            - [PARCIAL 2021-2 Pt.1 (Prof. Durand y Llamoja Secc. M).pdf]()
            - [PARCIAL 2021-1 (Prof. Alva).pdf](https://drive.google.com/file/d/1ExXqQ08k2NZwzGD3-SHXw7qmtiSW9F4W/view?usp=sharing)
            - [PARCIAL 2021-1 Pt.2 (Prof. Llamoja.pdf]()
            - [PARCIAL 2021-1 Pt.1 (Prof. Llamoja.pdf]()
            - [PARCIAL 2020-2 (Prof. Pauyac).pdf](https://drive.google.com/file/d/1bhci5MM-QyHwoQbWKaNBKli10HDVF9Tf/view?usp=sharing)
            - [PARCIAL 2020-1 Pt.2 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1yKqTXXapNxBAgYCUATNRELAxxPBrwfH5/view?usp=sharing)
            - [PARCIAL 2020-1 Pt.1 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1s5LOH2DOpP861X0HiXza1HvSccHDHxJQ/view?usp=sharing)
            - [PARCIAL 2020-2 (Prof. Farfan).pdf](https://drive.google.com/file/d/1UR3ZCS3ZnbBK00094w5-BTbjFoS5k3yb/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_fisica_2_exparcial_3():
    embed = discord.Embed(
        title="Ex. Parciales - fisica_2",
        description=textwrap.dedent(f"""\
            - [PARCIAL 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/1WzBhS9SUnxbbieSJtBUs3yz19WEYbnY4/view?usp=sharing)
            - [PARCIAL 2020-1 (Prof. Barrientos).pdf](https://drive.google.com/file/d/1GwRYpctpHg7UiAR6WVCmwY2_wHvjoOAq/view?usp=sharing)       
            - [PARCIAL 2020-1 Pt.2 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1IE78WzcIkpkLn23ZAhu213Z4Tlycug3t/view?usp=sharing)
            - [PARCIAL 2020-1 Pt.1 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1yAPJ9Ur69wljnQWP90wmLjwL2lSkUjD1/view?usp=sharing)
            - [PARCIAL 2020-1 (Prof. Durand).pdf](https://drive.google.com/file/d/1TVcPazXP1NOG2Wd3UmDukE_lOni6M3pY/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 3. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_fisica_2_exfinal_1():
    embed = discord.Embed(
        title="Ex. finales - fisica_2",
        description=textwrap.dedent(f"""\
            - [Ex.Final BFI05 M 2023-3.pdf](https://drive.google.com/file/d/1vkatDTCyTBzQqael6zTBBxP54119IXN8/view?usp=sharing)
            - [Ex.Final BFI05 A 2023-2.pdf](https://drive.google.com/file/d/14aTGiNLsei7JlIPArZZfQ99AI0dz2P5_/view?usp=sharing)
            - [Ex.Final BFI05 2023-2.pdf](https://drive.google.com/file/d/1UUBWrvWgc83UnFHy5h45Cbd69tWEDXzO/view?usp=sharing)
            - [Ex.Final BFI05 2023-1.pdf](https://drive.google.com/file/d/1TQcB653CCzpRt0-hFtZii4S_4XVq_C66/view?usp=sharing)
            - [Ex.Final 2022-3.pdf](https://drive.google.com/file/d/1Wg-p0cAV1zW5phx0Kf8QH6YbBrjGBP2X/view?usp=sharing)
            - [Ex.Final 2022-2.pdf](https://drive.google.com/file/d/1DgpwNu-PrChX9RgS9h03LJwBx_l2cjkU/view?usp=sharing)                       
            - [Ex.Final C 2022-1.pdf](https://drive.google.com/file/d/1K44KPYQt4iyze3q1SHzLFbNEECuBuxjm/view?usp=sharing)
            - [Ex.Final B 2022-1.pdf](https://drive.google.com/file/d/1lgS6pjj8vzWPCtYsIP-C1FjVPnk0tTgn/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_exfinal_2():
    embed = discord.Embed(
        title="Ex. finales - fisica_2",
        description=textwrap.dedent(f"""\
            - [Ex.Final A 2022-1.pdf](https://drive.google.com/file/d/1atTSORPWhbT4_KiK_CspD-wJNaj9mpRR/view?usp=sharing)
            - [Ex.Final 2021-2 (Prof. Roy Secc. Q).pdf](https://drive.google.com/file/d/1e1KV5oLWdTlgPuSI_FrbOq2aSPd1eduE/view?usp=sharing)                      
            - [Ex.Final 2021-2 (Prof. Roy Secc. N).pdf](https://drive.google.com/file/d/1A-vYzKpGtlrIZUK_zeoins-BRtkK3zwE/view?usp=sharing)
            - [Ex.Final 2021-2 (Prof. Durand y Llamoja Secc. M).pdf]()
            - [Ex.Final 2021-1 (Prof. Alva).pdf](https://drive.google.com/file/d/1nLXXPXnilRPqYc3hAyxBObYR_qXEcwn4/view?usp=sharing)
            - [Ex.Final 2021-1 (Prof. Llamoja).pdf]()
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_exfinal_3():
    embed = discord.Embed(
        title="Ex. finales - fisica_2",
        description=textwrap.dedent(f"""\
            - [FINAL 2020-2 Pt.2 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1XdGYS2--wN1zb6X5NR94J4VcppWmriCj/view?usp=sharing)
            - [FINAL 2020-2 Pt.1 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1_9c_coh3vpj6S5y-eQ3RYGTRk8i7C8oI/view?usp=sharing)
            - [FINAL 2020-2 (Prof. Farfan).pdf](https://drive.google.com/file/d/1-WsgtOaalQHxLCEpzYzzkh-WG-m5X1qj/view?usp=sharing)
            - [FINAL 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/1swTVfOnzFfzzd7ygCtyPgcfNo7gndJmi/view?usp=sharing)
            - [FINAL 2020-1 (Prof Barrientos).pdf](https://drive.google.com/file/d/1mSVBDlVAs98p4eHvSTqgrwonQppsQ74v/view?usp=sharing)
            - [FINAL 2020-1 (Prof Llamoja).pdf](https://drive.google.com/file/d/1qdLuHQZmXI3mUwVsppteoaltx31J2nn5/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 3. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - fisica_2",
        description=textwrap.dedent(f"""\
            - [SUSTI BFI05 2023-2.pdf](https://drive.google.com/file/d/1WNmhmrNWIN9sbzYbnP-Jsd9B2RBFEt8p/view?usp=sharing)
            - [SUSTI 2022-2.pdf](https://drive.google.com/file/d/1PSOyQG1bQ_NEQYdYNd0sqbDGAP4icOPg/view?usp=sharing)
            - [SUSTI 2022-1.pdf](https://drive.google.com/file/d/1huK2r7lAVISEkOKC3NM8GADllGF_xzbw/view?usp=sharing)
            - [SUSTI 2021-2 (Prof. Roy Secc. Q).pdf](https://drive.google.com/file/d/1gBzWH-pq1_KwQ7K0gA5OkiRRR-JrQxN_/view?usp=sharing)
            - [SUSTI 2020-2 (Prof. Caro).pdf](https://drive.google.com/file/d/102PJb1Pcu3URaorhJ6H9FQdZVXt4jXaa/view?usp=sharing)
            - [SUSTI 2020-2 (Prof. Farfan).pdf](https://drive.google.com/file/d/1AGRBfC94rZLhRqT1oljbHNCCTZ7U8-ix/view?usp=sharing)
            - [SUSTI 2020-2 Pt.1 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1lxvks7uASArcPC67rvCkppTV3TMeAjkq/view?usp=sharing)
            - [SUSTI 2020-2 Pt.2 (Prof. Llamoja).pdf](https://drive.google.com/file/d/1uP7emqgh5bBDXyT0o0nxKBR8H9YQ6nA5/view?usp=sharing)
            - [SUSTI 2020-2 (Prof. Pauyac).pdf](https://drive.google.com/file/d/1Tw8Tx-LCPC_nso0tISn_yvWH-fYlivTg/view?usp=sharing)                                           
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - fisica_2",
        description=textwrap.dedent(f"""\
            - [Prueba de Entrada BFI05 2023-2.pdf](https://drive.google.com/file/d/13HCHKxXxxOgY7QhXzotr7p8uz5x4BuIT/view?usp=sharing)
            - [Prueba de Entrada 2022-2.pdf](https://drive.google.com/file/d/1BRn5vYK0R3BIgqpb1_28Wa2rJNN7cZiU/view?usp=sharing)                       
            - [Prueba de Entrada 2022-1.pdf](https://drive.google.com/file/d/1AJFsv1Y7uGV45dA-1cwHCLHJtSrxz0RV/view?usp=sharing)
            - [Prueba de Entrada 2020-1.pdf](https://drive.google.com/file/d/1rR_y4ebr-FnnyseXRv1S0wFJhduTzZSy/view?usp=sharing)        
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc1():
    lista = []

    lista.append(get_embed_calculo_integral_pc1_0())
    lista.append(get_embed_calculo_integral_pc1_1())
    lista.append(get_embed_calculo_integral_pc1_2())
    lista.append(get_embed_calculo_integral_pc1_3())
    lista.append(get_embed_calculo_integral_pc1_4())

    return lista

def get_embed_calculo_integral_pc1_0():
    embed = discord.Embed(
        title="1ra PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-1 2023-3.pdf](https://drive.google.com/file/d/1orGkJ6SmVRdfZK3l2AjeIvd-7JLt9Vzx/view?usp=sharing)
            - [PC-1 2023-2.pdf](https://drive.google.com/file/d/14FXucz08MnRxm864S4CgqFL8O0ixQB4W/view?usp=sharing)
            - [PC-1 2023-1.pdf](https://drive.google.com/file/d/1lv93DzQsnuuuOPrGu6a6KFWOi3pj7LGd/view?usp=sharing)
            - [PC-1 2022-3.pdf](https://drive.google.com/file/d/1q5ICqAuZ05SEy1TQBG1QBcwxGHpaUH-l/view?usp=sharing)
            - [PC-1 2022-2.pdf](https://drive.google.com/file/d/1QONMndjz-0QnUOQgOSaAgQACb7TrW1F1/view?usp=sharing)
            - [PC-1 2022-1.pdf](https://drive.google.com/file/d/15a-oQ2mb4M-U-Or946pZCtZfQM2L3eMw/view?usp=sharing)
            - [PC-1 2021-2 O (Prof Erquizio).pdf](https://drive.google.com/file/d/1IizCrN3Jg7ih8y5yyvCWAt-ngyJl3GUD/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc1_1():
    embed = discord.Embed(
        title="1ra PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-1 2021-2 N (Prof Cornejo).pdf](https://drive.google.com/file/d/1ldbz4Z8u3vTFFP_PNVR2J_Pdfdapqs6w/view?usp=sharing)
            - [PC-1 2021-2 M (Prof Saal).pdf](https://drive.google.com/file/d/1giZDAWC81yYY2ZLpdquBSm4TByYBnN-y/view?usp=sharing)
            - [PC-1 2021-1 (Prof Saal).jpg](https://drive.google.com/file/d/1Qaik5eSuhBTVW2up1SPCGX4YmaCEFxMT/view?usp=sharing)
            - [PC-1 2021-1 (Prof Arevalo).pdf](https://drive.google.com/file/d/1BKjF3sgGBdPlfjveNvkkVaRHN5yj8C8o/view?usp=sharing)
            - [PC-1 2020-2 (Prof Saal).pdf](https://drive.google.com/file/d/12W8aQd_ES9Rl6mk46JKpq3EQcTVy6O-r/view?usp=sharing)
            - [PC-1 2020-2 (Prof Oria-Arevalo).pdf](https://drive.google.com/file/d/1t4ZTU4Pfb3dTexelbPsjV0S-NMfG7UfK/view?usp=sharing)
            - [PC-1 2020-2 (Prof Israel).pdf](https://drive.google.com/file/d/1aqH46wdSjdn7wXQFAUA40RcTqp9WTTJz/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc1_2():
    embed = discord.Embed(
        title="1ra PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-1 2020-2 (Prof Erquizio).pdf](https://drive.google.com/file/d/1fNrRjCqAe7fOGmnYdM71UT6nLvP4O3sw/view?usp=sharing)
            - [PC-1 2020-1 Sol.(Prof Oria).pdf](https://drive.google.com/file/d/1vt_Qsv2g40sF3fN3hJW5kk8uemVizFYB/view?usp=sharing)
            - [PC-1 2020-1 (Prof Saal).pdf](https://drive.google.com/file/d/1FJfyE4aWtEeGUAOaXTZYrMHa_BLHUsYN/view?usp=sharing)
            - [PC-1 2020-1 (Prof Oria).pdf](https://drive.google.com/file/d/1lmZrvVVB16XkiiGT7NnaxqImU1CWzBU_/view?usp=sharing)
            - [PC-1 2020-1 (Prof Erquizio).pdf](https://drive.google.com/file/d/11kMelkoKL-NKGgkr7OCz62EIattjkyNP/view?usp=sharing)
            - [PC-1 2019-2.jpg](https://drive.google.com/file/d/1IjX77iCTZzEvAEEH_U2_FGzc1NJugGcN/view?usp=sharing)
            - [PC-1 2018-3.pdf](https://drive.google.com/file/d/1k5TzTgtfKF5hfN9BUgJQRntxUw-n4b62/view?usp=sharing)
            - [PC-1 2018-2.pdf](https://drive.google.com/file/d/1e23FhN0r8TDDh-FdS3tMlcgBNvkluH5S/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 3. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_calculo_integral_pc1_3():
    embed = discord.Embed(
        title="1ra PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-1 2018-1.pdf](https://drive.google.com/file/d/199k-E_IIjwBpPmH_FKw9aWM_fN9RXdV8/view?usp=sharing)
            - [PC-1 2017-2.pdf](https://drive.google.com/file/d/1s5AfZD01w-ah7I4rPVCBb5RwMADVf0B9/view?usp=sharing)
            - [PC-1 2017-1.pdf](https://drive.google.com/file/d/1a5Di196nsMthDC2rdAGrqAe43Ll6C7lk/view?usp=sharing)
            - [PC-1 2016-2.pdf](https://drive.google.com/file/d/1qGbfnelpmhnltkj8FP5jDvq4stoFI-R-/view?usp=sharing)
            - [PC-1 2016-1.pdf](https://drive.google.com/file/d/12ZsWakmfkPJG-DbJp1tkhlvGhkSQkR3h/view?usp=sharing)
            - [PC-1 2015-2.pdf](https://drive.google.com/file/d/1Q9qibNTU47K4DA90cvp2UZsmaprNb_iE/view?usp=sharing)
            - [PC-1 2015-1.pdf](https://drive.google.com/file/d/1eISVXIJi8dGYa5y0v4k-hVnMqXZh4GaT/view?usp=sharing)
            - [PC-1 2014-3.pdf](https://drive.google.com/file/d/1JtT_r9b-dQFbS0V1O-SsuROpe3iKblFJ/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 4. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_calculo_integral_pc1_4():
    embed = discord.Embed(
        title="1ra PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-1 2014-2.pdf](https://drive.google.com/file/d/1USJuIG9F4olN1HTT3UJA3lG14kzBzMlf/view?usp=sharing)
            - [PC-1 2013-3.jpg](https://drive.google.com/file/d/1xHI9XieaGidKTO9ZVa1DOaKtngfaEpHn/view?usp=sharing)
            - [PC-1 2013-2.pdf](https://drive.google.com/file/d/1AJBxsHT3osrrn6AK3xbaY9A0CwXkheN5/view?usp=sharing)
            - [PC-1 2012-3.pdf](https://drive.google.com/file/d/1z--RtBKUfw4qB9jm-FZiP-W8HcEXWzbD/view?usp=sharing)
            - [PC-1 2012-2 Sol.pdf](https://drive.google.com/file/d/1kMN7o9RBr8iKHer5XbAF7Z9KKyDm0_mO/view?usp=sharing)
            - [PC-1 2012-1.pdf](https://drive.google.com/file/d/10jgm8J7bhtBHLGgs_P_6KMovxhF8FtMi/view?usp=sharing)
            - [PC-1 2007-3.pdf](https://drive.google.com/file/d/18-M1tbJwSsykIrlHW6HEJFY4SzW15V-r/view?usp=sharing)
            - [PC-1 2007-2.jpg](https://drive.google.com/file/d/1UWhmbTzCY71Rm2B2qT8Q-PVZ2Kz7WDtu/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 5. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc2():
    lista = []

    lista.append(get_embed_calculo_integral_pc2_1())
    lista.append(get_embed_calculo_integral_pc2_2())
    lista.append(get_embed_calculo_integral_pc2_3())
    lista.append(get_embed_calculo_integral_pc2_4())
    lista.append(get_embed_calculo_integral_pc2_5())

    return lista

def get_embed_calculo_integral_pc2_1():
    embed = discord.Embed(
        title="2da PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-2 2023-3.pdf](https://drive.google.com/file/d/11a-S8JpVFi2s3BoAWiEd1ecCtoSYr4dA/view?usp=sharing)
            - [PC-2 2023-2.pdf](https://drive.google.com/file/d/1vqJC2GHC3K-qScfptv-5DRRWaKrZNEz3/view?usp=sharing)
            - [PC-2 2023-1.pdf](https://drive.google.com/file/d/13c2_MlzNAg178DSWAT9ef34zuRzZTEEm/view?usp=sharing)
            - [PC-2 2022-3.pdf](https://drive.google.com/file/d/1fc9cQTjIYxGk8vSEXgaTya6Q42QAy2LY/view?usp=sharing)
            - [PC-2 2022-2.pdf](https://drive.google.com/file/d/1iL6SiNSZ2WHsJ-H2qyTqL0DyvKrRxqax/view?usp=sharing)
            - [PC-2 2022-1.pdf](https://drive.google.com/file/d/1pV2cRZ794i0j4u0Y6rqFpx6Gsdo4RFbq/view?usp=sharing)
            - [PC-2 2021-2 O (Prof Erquizio).pdf](https://drive.google.com/file/d/1M0-CkRETfB6wXSMEjmEO1UfT8kZD0loy/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc2_2():
    embed = discord.Embed(
        title="2da PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-2 2021-2 N (Prof Cornejo).pdf](https://drive.google.com/file/d/1FqSNOM_bNnYEUrIHNJxQlVXMwW2Xcur7/view?usp=sharing)
            - [PC-2 2021-2 (Prof Saal).pdf](https://drive.google.com/file/d/11nd9k2vgLafBh55qa7nx5g_Ym1FgUkQM/view?usp=sharing)
            - [PC-2 2021-1 (Prof Saal).jpg](https://drive.google.com/file/d/1bHKiGDkvTfqdouvU6VLieYxedWyjJFOy/view?usp=sharing)
            - [PC-2 2021-1 (Prof Arevalo).pdf](https://drive.google.com/file/d/1glMmweAJhxzcOw4vymXt4dG-CQCzvS5_/view?usp=sharing)
            - [PC-2 2020-2 (Prof Saal).pdf](https://drive.google.com/file/d/11V0n2diwqS84_yXSf2FnwfTEtOYS-8Ul/view?usp=sharing)
            - [PC-2 2020-2 (Prof Oria).pdf](https://drive.google.com/file/d/10PAKpSX53SC-ZwtyAF_EZ-2r3OXGA96z/view?usp=sharing)
            - [PC-2 2020-2 (Prof Israel).pdf](https://drive.google.com/file/d/19u85TWYvKysQwTMWkAllW2-TGFb4siQz/view?usp=sharing)
            - [PC-2 2020-2 (Prof Erquizio).pdf](https://drive.google.com/file/d/1KQ95H-OaklaZge7AhWgecvRoAmBRtgu3/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc2_3():
    embed = discord.Embed(
        title="2da PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-2 2020-2 (Prof Arevalo).pdf](https://drive.google.com/file/d/10tjf-KAgQ7g_yr6VRa4R6MiWeGJm05iH/view?usp=sharing)
            - [PC-2 2020-1 (Prof Saal).pdf](https://drive.google.com/file/d/1gpX_6KIZ7WKWl1N7miK34lmau-WuuAtJ/view?usp=sharing)
            - [PC-2 2020-1 (Prof Oria).pdf](https://drive.google.com/file/d/1sHi9jTxiZrjO3uahraOx7l2lWBdEClIZ/view?usp=sharing)
            - [PC-2 2020-1 (Prof Erquizio).pdf](https://drive.google.com/file/d/1V3iPvENjK1nFnff2oMkn3qlW_msoBrYh/view?usp=sharing)
            - [PC-2 2019-2.jpg](https://drive.google.com/file/d/1g235AjpCqNUanTXpGoW8GJqHzgDkgwaz/view?usp=sharing)
            - [PC-2 2019-1.pdf](https://drive.google.com/file/d/1VYshO5RfTSDckzdfenXCx-gannlGk5qs/view?usp=sharing)
            - [PC-2 2018-3.pdf](https://drive.google.com/file/d/1dYlpWkYDmksnUrC4WPFPqE0is1kHtHZS/view?usp=sharing)
            - [PC-2 2018-2.pdf](https://drive.google.com/file/d/1wB7opiYkrD7VkHtnAKrNy63J6XoBnBMY/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 3. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc2_4():
    embed = discord.Embed(
        title="2da PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-2 2017-2.pdf](https://drive.google.com/file/d/1L6Ej1D_o4sIGEK0paeyKXVXZCH49dXbW/view?usp=sharing)
            - [PC-2 2016-2.pdf](https://drive.google.com/file/d/1Me4AR7fVN-V69eZpRDpmUwspvl4gKOM2/view?usp=sharing)
            - [PC-2 2016-1.jpg](https://drive.google.com/file/d/102rYF4KV3ktfa6OSHsxAW2DKW0tWoZYZ/view?usp=sharing)
            - [PC-2 2015-2.pdf](https://drive.google.com/file/d/1a5GeI6m4LKfnmOdUxYVCCuM_55kHYHWR/view?usp=sharing)
            - [PC-2 2015-1.pdf](https://drive.google.com/file/d/1_9GQPli0P6VMd73VEdBfYGuV9BTrsBqN/view?usp=sharing)
            - [PC-2 2014-1.jpg](https://drive.google.com/file/d/1mkqHsAE1QTV2EDteaZO6qKFDCT3C2MLR/view?usp=sharing)
            - [PC-2 2013-3.jpg](https://drive.google.com/file/d/1FZ78QDEvQi1It_xueJx7D6CW-ps5_IbE/view?usp=sharing)
            - [PC-2 2013-1.pdf](https://drive.google.com/file/d/1VPxCrUApbepWAG7SjeJtzYqRq7a-9nrQ/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 4. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc2_5():
    embed = discord.Embed(
        title="2da PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-2 2012-3.pdf](https://drive.google.com/file/d/16guwYKXRePzdAdgC2kGCHd26SG7m6eWG/view?usp=sharing)
            - [PC-2 2012-2.pdf](https://drive.google.com/file/d/1LBVkKvoRQRrdcvLd-88xj76mcj2s8wnv/view?usp=sharing)
            - [PC-2 2009-3.pdf](https://drive.google.com/file/d/1UA_wRxM6SCUTICriB0sA7lNzQelI7_Yg/view?usp=sharing)
            - [PC-2 2008-2.pdf](https://drive.google.com/file/d/1kit5p9GQU3TlsKLzwQG2gNi4q8YK67im/view?usp=sharing)
            - [PC-2 2006-1.pdf](https://drive.google.com/file/d/1KDZ1LU05_IjpK2WE7CtEs3-o-GMiS3c4/view?usp=sharing)
            - [PC-2 2001-1.pdf](https://drive.google.com/file/d/1ZOlkQMuZLl9IOc77zVHAma3TAOYi-32r/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 5. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embed_calculo_integral_pc3():
    embed = discord.Embed(
        title="3ra PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-3 2022-1.pdf](https://drive.google.com/file/d/1jFf4cj3GymvAkqJFtt0nIMj37Ib5HiBi/view?usp=sharing)
            - [PC-3 2022-2.pdf](https://drive.google.com/file/d/17wsCacq_rNNwCy_8CmA8ZmCbKCk_U5GS/view?usp=sharing)
            - [PC-3 2022-3.pdf](https://drive.google.com/file/d/1bW0di2SR5llge63UaWlErwxzNhLND0Sz/view?usp=sharing)
            - [PC-3 2023-1.pdf](https://drive.google.com/file/d/1fqDRXrsWYNrbnnT_s9jZ8zuHYafHbQKJ/view?usp=sharing)
            - [PC-3 2023-2.pdf](https://drive.google.com/file/d/1Bwo1dg-JdGwAzvYB1HUFp8lWJ6AdNU3Z/view?usp=sharing)
            - [PC-3 2023-3.pdf](https://drive.google.com/file/d/1LkqkWQGUpnmZKhc5OmIyXWVxaQ7049If/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc4():
    embed = discord.Embed(
        title="4ta PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-4 2022-1.pdf](https://drive.google.com/file/d/13zim1zPNylgIWMwrDgiH7SbwPzJ6cZqF/view?usp=sharing)
            - [PC-4 2022-2.pdf](https://drive.google.com/file/d/1yqCpzLK2MAf9NPd0oq9lDY-xFqix_U7h/view?usp=sharing)
            - [PC-4 2023-1.pdf](https://drive.google.com/file/d/1rpBSnIheGpVx3EPeOsoqbG2AXA3o_nK3/view?usp=sharing)
            - [PC-4 2023-2.pdf](https://drive.google.com/file/d/15KYxgA8m0QvdY-AenvIMj3K7fRBBCp8P/view?usp=sharing)
            - [PC-4 2023-3.pdf](https://drive.google.com/file/d/17UYGWmB7vZ5bhU1ypfmnvlGbLLafV9pM/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc5():
    embed = discord.Embed(
        title="5ta PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PC-5 2022-1.pdf](https://drive.google.com/file/d/18nhmu5sD6U-3OjhC3quGrRdvwFXypQaY/view?usp=sharing)
            - [PC-5 2022-2.pdf](https://drive.google.com/file/d/13oIKnH-nVigmAAKUtxlV5wkH2S8H_kgr/view?usp=sharing)
            - [PC-5 2023-1.pdf](https://drive.google.com/file/d/1fJkycvTxU7pR3LZgRRSC2H9_PAHnaLre/view?usp=sharing)
            - [PC-5 2023-2.pdf](https://drive.google.com/file/d/1unpOJ8zqAu3f59xJp4YaoufANTk9AL57/view?usp=sharing)
            - [PC-5 2023-3.pdf](https://drive.google.com/file/d/1yqHQr1V8DMg3eZtwMHPuq-6GTxn3pdaF/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - calculo_integral",
        description=textwrap.dedent(f"""\
            - [Parcial 2022-1.pdf](https://drive.google.com/file/d/17gRQrAYjigjZnn9oCG5qyqByIJThlh08/view?usp=sharing)
            - [Parcial 2022-2.pdf](https://drive.google.com/file/d/1_vy_23vI5A8zWmMnmyLA09xuuIXyBbTK/view?usp=sharing)
            - [Parcial 2022-3.pdf](https://drive.google.com/file/d/111akGnIBcR64ZnCkDvGJerYkirENkOFI/view?usp=sharing)
            - [Parcial 2023-1.pdf](https://drive.google.com/file/d/1U4iSVJH9oLMbH3F0TrlD9Z3gjoi-vo6v/view?usp=sharing)
            - [Parcial 2023-2.pdf](https://drive.google.com/file/d/1Xgk3YECgZO0W5CTcmSxkf6vr07aiPuRS/view?usp=sharing)
            - [Parcial 2023-3.pdf](https://drive.google.com/file/d/1QNM5CQgZP9x7KRMeEjUraUhtG7tg1wua/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_exfinal():
    embed = discord.Embed(
        title="Ex. finales - calculo_integral",
        description=textwrap.dedent(f"""\
            - [Final 2022-1.jpg](https://drive.google.com/file/d/1O-Hc8DWjz4VBiLsYGSOFjut7ZJ4EAaxB/view?usp=sharing)
            - [Final 2022-2.pdf](https://drive.google.com/file/d/10tvGI9TWVRBQrjZLb35J2DwmnQ32MZ0j/view?usp=sharing)
            - [Final 2022-3.pdf](https://drive.google.com/file/d/1IY-b7K7XtSgdJt8g9hNFIsH8U8QfWBHR/view?usp=sharing)
            - [Final 2023-1.pdf](https://drive.google.com/file/d/1m48rS1l4vK5rF_11X8LZwLizowgbgXPZ/view?usp=sharing)
            - [Final 2023-2.pdf](https://drive.google.com/file/d/1TSXfvJr_WsQeot7RAHsgrwwZzQq2mHwW/view?usp=sharing)
            - [Final 2023-3.pdf](https://drive.google.com/file/d/17fYweI57qG0Jonc_hR7C6uG_WJ-amr0K/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - calculo_integral",
        description=textwrap.dedent(f"""\
            - [Susti 2022-1.pdf](https://drive.google.com/file/d/18PecgJnBzabDCnT8xJ4wN3r7URwWXuwv/view?usp=sharing)
            - [Susti 2022-2.pdf](https://drive.google.com/file/d/1WKxJ-SQF7E-NwdIvkaQCFtOYKmYcDCwo/view?usp=sharing)
            - [Susti 2023-1.pdf](https://drive.google.com/file/d/1SX1OJeKvCDTBPvs5Ox8TyZh0df4HGYjP/view?usp=sharing)
            - [Susti 2023-2.pdf](https://drive.google.com/file/d/1k3CZGzKeOmXAVtLAVJ7PwKrFZ7M8Zmxx/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - calculo_integral",
        description=textwrap.dedent(f"""\
            - [PE 2022-1.jpg](https://drive.google.com/file/d/1JqUJw1r5XHz_jjLUpjwe0OqPRz5KYjb6/view?usp=sharing)
            - [PE 2022-2.pdf](https://drive.google.com/file/d/1BGs8EPVJQOx541VqwL3aSHfopvKdb2aM/view?usp=sharing)
            - [PE 2023-1.pdf](https://drive.google.com/file/d/1gtgKWGy_N0G4RNCeD1dFysAMO-WUMNk8/view?usp=sharing)
            - [PE 2023-2.pdf](https://drive.google.com/file/d/1feNOO0F0B308bJvhgxYEUkbIXVlfM8Yk/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embed_algoritmos_1_pc1():
    embed = discord.Embed(
        title="1ra PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - [PC1 2022-1(Prof. Butler).pdf](https://drive.google.com/file/d/1pcEoo5uWJo2xZrPzP0qIQYEWqeUUIoGL/view?usp=sharing)
            - [PC1 2022-2 (Prof. Butler).pdf](https://drive.google.com/file/d/1z2NdkrFaN8hlkw8U-q2HmZlQO5HgumFI/view?usp=sharing)
            - [PC1 2022-2 (Prof. Cañamero).pdf](https://drive.google.com/file/d/1BUh1YWpDPCHgqT-jHo_Neg-PNA-1z51S/view?usp=sharing)
            - [PC1 2022-3 (Prof. Galvez).pdf](https://drive.google.com/file/d/1EI54MJHAerCVoID7L6uPe8egayc5QlAg/view?usp=sharing)
            - [PC1 BMA09 2023-3.pdf](https://drive.google.com/file/d/136yuPT9XJ3is7bJ3gH5ULH36TbUKHUze/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_pc2():
    embed = discord.Embed(
        title="2da PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - [PC2 2022-1(Prof. Butler).pdf](https://drive.google.com/file/d/1BWz0cCZ2pgc0nZHvHP8qsoW6U5iXCtyK/view?usp=sharing)
            - [PC2 2022-2(Prof. Butler).pdf](https://drive.google.com/file/d/1jSxxfvSvZyZkVcBh4Y-n9zZHGwgqJJNe/view?usp=sharing)
            - [PC2 2022-2(Prof. Cañamero).pdf](https://drive.google.com/file/d/1iB99bQWDF-kDXp-hAXpZ08TFvf0EOAKF/view?usp=sharing)
            - [PC2 BMA09 2023-3.pdf](https://drive.google.com/file/d/1zyXU1COc8YAM6hhxHGmvZqy2F5NCJ8lf/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_algoritmos_1_pc3():
    embed = discord.Embed(
        title="3ra PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - [PC3 2022-1(Prof. Butler).pdf](https://drive.google.com/file/d/1VRYOwVOHx5viVM-A22kL7M07cpE40U19/view?usp=sharing)
            - [PC3 2022-2(Prof. Butler).pdf](https://drive.google.com/file/d/1yF-zkCLs2wSR6sJ8AytjvMt4jj03l7Fv/view?usp=sharing)
            - [PC3 2022-2(Prof. Cañamero).pdf](https://drive.google.com/file/d/1O4DyvNSsOmpoUsOPGs2w43kyQDIb1NXZ/view?usp=sharing)
            - [PC3 2022-3(Prof. Galvez).pdf](https://drive.google.com/file/d/1p24xBuGx3opiyJm2GR1UeUwFSGxAK392/view?usp=sharing)
            - [PC3 BMA09 2023-3.pdf](https://drive.google.com/file/d/1eAb588EVRvFV_dGNl7tDJdgq0lzQle7k/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_pc4():
    embed = discord.Embed(
        title="4ta PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - [PC4 2022-1 (Prof. Butler).pdf](https://drive.google.com/file/d/1L64gJx3-eMEgr3lgBVtq4EVaGty2LbnE/view?usp=sharing)
            - [PC4 2022-2 (Prof. Butler).pdf](https://drive.google.com/file/d/1rB9cizci8ggh3nTRyUtAcWYl1Z7eyd13/view?usp=sharing)
            - [PC4 2022-2 Pt.1 (Prof. Cañamero).pdf](https://drive.google.com/file/d/10_VyXuG1G5BLLJYuuXttEgf5s4gXI84G/view?usp=sharing)
            - [PC4 2022-2 Pt.2 (Prof. Cañamero).pdf](https://drive.google.com/file/d/1OQ8ykmDX3COD627nOGs-5nQ3dODclyvg/view?usp=sharing)
            - [PC4 2022-3 (Prof. Galvez).pdf](https://drive.google.com/file/d/17tMyGMKv3YC_3c0J8dpuuhrDNOYa7CoL/view?usp=sharing)
            - [PC4  BMA09 2023-3.pdf](https://drive.google.com/file/d/13wUev1egTLnGiCSg6ZakV5IvJ-WC9iIg/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_algoritmos_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - algoritmos_1",
        description=textwrap.dedent(f"""\
            - [Parcial 2022-1 (Prof. Butler).pdf](https://drive.google.com/file/d/1736wmcSDhq9geikixqlHywB0o31h_9NO/view?usp=sharing)
            - [Parcial Test 2022-1 (Prof. Butler).pdf](https://drive.google.com/file/d/1GHt3QLTMHj_T9M8hpLm8w7oSaUHXZ5Np/view?usp=sharing)
            - [Parcial 2022-2 (Prof. Butler).pdf](https://drive.google.com/file/d/1mSay1fHPBEKtkdaDAUSQVlZtNegJjgWi/view?usp=sharing)
            - [Parcial 2022-3 (Prof. Galvez).pdf](https://drive.google.com/file/d/1dT60KhbvGRewPio_IW9mdldLw_ZVPpid/view?usp=sharing)
            - [Parcial 2023-1.pdf](https://drive.google.com/file/d/1nBxcXSDzpuZZZTJjD-EB5glG3Nq6O037/view?usp=sharing)
            - [Parcial 2023-2.pdf](https://drive.google.com/file/d/1QpAO7pjUfqOBK_6j0QwPtoWTxvp6k3yD/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - algoritmos_1",
        description=textwrap.dedent(f"""\
            - [Final 2022-1(Butler).pdf](https://drive.google.com/file/d/1qNXeT1oSCfqfLU9WFXhgj1oPJK8rB1Ik/view?usp=sharing)
            - [Final 2022-2(Butler).pdf](https://drive.google.com/file/d/1e70wbk4262o06R485bnZ3W38QdmGCNOQ/view?usp=sharing)
            - [Final 2022-3(Galvez).pdf](https://drive.google.com/file/d/1PXUw7MJxyEoG1y0IKDRmumXiPkxgRbPi/view?usp=sharing)
            - [Final 2023-1.pdf](https://drive.google.com/file/d/1n-Y4UKm6yFb_quVQhtuGlzuanGsrr5EI/view?usp=sharing)
            - [Final 2023-2.pdf](https://drive.google.com/file/d/12S8TDqPIno-W3iySiU6pjZ3M51rinVrt/view?usp=sharing)
            - [Final 2023-3.pdf](https://drive.google.com/file/d/1xyvT01jRMlxuViUDoLpRpxuICAWJ_-K2/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - algoritmos_1",
        description=textwrap.dedent(f"""\
            - [Susti 2022-1 (Butler).pdf](https://drive.google.com/file/d/1wdxgWsZmTiSBXk08o5HeqF2nHhNpIegO/view?usp=sharing)
            - [Susti 2022-2 (Butler).pdf](https://drive.google.com/file/d/11QAp8E1OkMb6pFFIj670dKAVhrqQs1s7/view?usp=sharing)
            - [Susti 2022-3.pdf](https://drive.google.com/file/d/1ufC9FH5W4h8YGvpV3s70YdWIuLF9RNZS/view?usp=sharing)
            - [Susti 2023-2.pdf](https://drive.google.com/file/d/1Gl5uu9tadWcUtNOlrr3KOD5XREDiqz6b/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - algoritmos_1",
        description=textwrap.dedent(f"""\
            - [P. Entrada 20-2 (Cañamero).pdf](https://drive.google.com/file/d/1IHkldzN0uU00D_EZKTqV_-aK_DMz91pR/view?usp=sharing)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed





def get_embed_quimica_1_pc1():
    embed = discord.Embed(
        title="1ra PC - Quimica General",
        description=textwrap.dedent(f"""\
            - [PC1 2022-1.pdf](https://drive.google.com/file/d/184b4culmbHj3MFayUMuwAQ0oewRW5gel/view?usp=sharing)
            - [PC1 2022-2.pdf](https://drive.google.com/file/d/1xpn6aOvmJzAFzgRY9SyP2jpxv7RiEach/view?usp=sharing)
            - [PC1 2023-1.pdf](https://drive.google.com/file/d/1WpxqD4HCHy_VxUSXugPlWanlRzYnWK1I/view?usp=sharing)
            - [PC1 2022-2.pdf](https://drive.google.com/file/d/150G-JiDIsUe-cqe4qVbhp_8c_f7QV4nk/view?usp=sharing) 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_pc2():
    embed = discord.Embed(
        title="2da PC - Quimica General",
        description=textwrap.dedent(f"""\
            - [PC2 2022-1.pdf](https://drive.google.com/file/d/1ieQhlrTe12y4ORvtt-9jRrfcejZ8Bp1-/view?usp=sharing)
            - [PC2 2022-2.pdf](https://drive.google.com/file/d/1Y7ZoaAvHtnRlTMGyfCVKZEkMm0HILF0N/view?usp=sharing)
            - [PC2 2023-1.pdf](https://drive.google.com/file/d/1LdP632oeXQ_HOCmGOASHdpdXNHYd7Q4k/view?usp=sharing)
            - [PC2 2022-2.pdf](https://drive.google.com/file/d/1L92bykC5-eK554QPoUP4eEejTTUn3KBD/view?usp=sharing) 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_quimica_1_pc3():
    embed = discord.Embed(
        title="3ra PC - Quimica General",
        description=textwrap.dedent(f"""\
            - [PC3 2022-1.pdf](https://drive.google.com/file/d/1HMKAETY1rnV6Q_JHVYtl4ZhsQKuuYJsa/view?usp=sharing)
            - [PC3 2022-2.pdf](https://drive.google.com/file/d/1JPdsTjM_2cyUlR4luKPwRdpHEvdea9Vw/view?usp=sharing)
            - [PC3 2023-1.pdf](https://drive.google.com/file/d/16Tr37JkeT3SiYCo11lrRqZuE0USdC2ZF/view?usp=sharing)
            - [PC3 2022-2.pdf](https://drive.google.com/file/d/1R3GLpr8To5R0iXvBvPmVfZPvxzxdhTc8/view?usp=sharing) 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_pc4():
    embed = discord.Embed(
        title="4ta PC - Quimica General",
        description=textwrap.dedent(f"""\
            - [PC4 2022-1.pdf](https://drive.google.com/file/d/1y_MXYRld6XPaVoYtUshhbRk5MM0lwWtH/view?usp=sharing)
            - [PC4 2022-2.pdf](https://drive.google.com/file/d/1BHNhRtkW2xxdCSfLRXtmClX8IIy5pd_x/view?usp=sharing)
            - [PC4 2023-1.pdf](https://drive.google.com/file/d/1G5J2ORd5qJgLR0-TP0yPo7lwjVq_4C_J/view?usp=sharing)
            - [PC4 2022-2.pdf](https://drive.google.com/file/d/1ZXgLwwlYvlwPRkPfZx5_QCmcZJ30J1Hq/view?usp=sharing) 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_quimica_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - Quimica General",
        description=textwrap.dedent(f"""\
           - [PC1 2022-1.pdf](https://drive.google.com/file/d/1mE_JzSjiTB37bsCFbowharsEBPqjfrx3/view?usp=sharing)
           - [PC1 2022-2.pdf](https://drive.google.com/file/d/1emmzlpzN5n9dPvQ8C6GPUsXXxfvQREKW/view?usp=sharing)
           - [PC1 2023-1.pdf](https://drive.google.com/file/d/1btpTSZiU_wg4UasaZhIVLGEwyXaP2eyg/view?usp=sharing)
           - [PC1 2022-2.pdf](https://drive.google.com/file/d/1_ZmLZZKw1HhcS6wJE4n6m9vMdT-8vUW-/view?usp=sharing) 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - Quimica General",
        description=textwrap.dedent(f"""\
           - [PC1 2022-1.pdf](https://drive.google.com/file/d/1mvtPR7GfSnMr07E4mnsTEqESpcm3gvMp/view?usp=sharing)
           - [PC1 2022-2.pdf](https://drive.google.com/file/d/1v1aLSAjrOxTIH6G_EEv9d-Cb-Nuub8Wb/view?usp=sharing)
           - [PC1 2023-1.pdf](https://drive.google.com/file/d/1CAkJEjsF3_ptaWlUKQsMiCm1l-MooyzD/view?usp=sharing)
           - [PC1 2022-2.pdf](https://drive.google.com/file/d/1MqlRM2Gtc9ttQyA7Tq1re6vI4LsvgkG-/view?usp=sharing) 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - Quimica General",
        description=textwrap.dedent(f"""\
           - [PC1 2022-1.pdf](https://drive.google.com/file/d/1R_vNnvEgmH4AsUcT6CU5-bh9pq6PG7QV/view?usp=sharing)
           - [PC1 2022-2.pdf](https://drive.google.com/file/d/1CaTDSyjufKFyhW6jQPaGi8g8n9uNHkb3/view?usp=sharing)
           - [PC1 2023-1.pdf]()
           - [PC1 2022-2.pdf]() 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - Quimica General",
        description=textwrap.dedent(f"""\
            
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embed_fundamentos_computador_pc1():
    embed = discord.Embed(
        title="1ra PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_pc2():
    embed = discord.Embed(
        title="2da PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_fundamentos_computador_pc3():
    embed = discord.Embed(
        title="3ra PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_pc4():
    embed = discord.Embed(
        title="4ta PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_pc5():
    embed = discord.Embed(
        title="5ta PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_exfinal():
    embed = discord.Embed(
        title="Ex. finales - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_redes_1_pc1():
    embed = discord.Embed(
        title="1ra PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_pc2():
    embed = discord.Embed(
        title="2da PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_pc3():
    embed = discord.Embed(
        title="3ra PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_pc4():
    embed = discord.Embed(
        title="4ta PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_pc5():
    embed = discord.Embed(
        title="5ta PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_pc1():
    embed = discord.Embed(
        title="1ra PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - [PC1 25-1 (Prof. Loayza)](https://docs.google.com/document/d/1ASF94Uh3QozChDxFAZHZVfcsaNBU6bWT/edit?usp=sharing&ouid=117048018312182294097&rtpof=true&sd=true)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_pc2():
    embed = discord.Embed(
        title="2da PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - [PC2 25-1 (Prof. Loayza)](https://docs.google.com/document/d/1faclJj7SagDL8_nCbvNs6-AMqpV6z8Id/edit?usp=drive_link&ouid=117048018312182294097&rtpof=true&sd=true)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_sistemas_operativos_1_pc3():
    embed = discord.Embed(
        title="3ra PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - [PC3 25-1 (Prof. Loayza)](https://docs.google.com/document/d/1-PAVTk0T05h48rGI3pKq8cH7j-l3B1wM/edit?usp=drive_link&ouid=117048018312182294097&rtpof=true&sd=true) 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_pc4():
    embed = discord.Embed(
        title="4ta PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - [PC4 25-1 (Prof. Loayza)](https://docs.google.com/document/d/1n3HxZGHRK0JVVUzph59wtHNZEz1tPL_z/edit?usp=drive_link&ouid=117048018312182294097&rtpof=true&sd=true)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embeds_fisica_2_pcs():

    lista = []

    lista.append(get_embed_fisica_2_pc1())
    lista.append(get_embed_fisica_2_pc2())
    lista.append(get_embed_fisica_2_pc3())
    lista.append(get_embed_fisica_2_pc4())
    lista.append("get_embed_fisica_2_pc5()")
    lista.append(get_embed_fisica_2_exparcial())
    lista.append(get_embed_fisica_2_exfinal())
    lista.append(get_embed_fisica_2_exsusti())
    lista.append(get_embed_fisica_2_entrada())

    return lista


def get_embeds_calculo_integral_pcs():

    lista = []

    lista.append(get_embed_calculo_integral_pc1())
    lista.append(get_embed_calculo_integral_pc2())
    lista.append(get_embed_calculo_integral_pc3())
    lista.append(get_embed_calculo_integral_pc4())
    lista.append(get_embed_calculo_integral_pc5())
    lista.append(get_embed_calculo_integral_exparcial())
    lista.append(get_embed_calculo_integral_exfinal())
    lista.append(get_embed_calculo_integral_exsusti())
    lista.append(get_embed_calculo_integral_entrada())

    return lista


def get_embeds_algoritmos_1_pcs():

    lista = []

    lista.append(get_embed_algoritmos_1_pc1())
    lista.append(get_embed_algoritmos_1_pc2())
    lista.append(get_embed_algoritmos_1_pc3())
    lista.append(get_embed_algoritmos_1_pc4())
    lista.append("get_embed_algoritmos_1_pc5()")
    lista.append(get_embed_algoritmos_1_exparcial())
    lista.append(get_embed_algoritmos_1_exfinal())
    lista.append(get_embed_algoritmos_1_exsusti())
    lista.append(get_embed_algoritmos_1_entrada())

    return lista

def get_embeds_quimica_1_pcs():

    lista = []

    lista.append(get_embed_quimica_1_pc1())
    lista.append(get_embed_quimica_1_pc2())
    lista.append(get_embed_quimica_1_pc3())
    lista.append(get_embed_quimica_1_pc4())
    lista.append("get_embed_quimica_1_pc5()")
    lista.append(get_embed_quimica_1_exparcial())
    lista.append(get_embed_quimica_1_exfinal())
    lista.append(get_embed_quimica_1_exsusti())
    lista.append(get_embed_quimica_1_entrada())

    return lista

def get_embeds_fundamentos_computador_pcs():

    lista = []

    lista.append(get_embed_fundamentos_computador_pc1())
    lista.append(get_embed_fundamentos_computador_pc2())
    lista.append(get_embed_fundamentos_computador_pc3())
    lista.append(get_embed_fundamentos_computador_pc4())
    lista.append(get_embed_fundamentos_computador_pc5())
    lista.append(get_embed_fundamentos_computador_exparcial())
    lista.append(get_embed_fundamentos_computador_exfinal())
    lista.append(get_embed_fundamentos_computador_exsusti())
    lista.append("get_embed_fundamentos_computador_entrada()")

    return lista


def get_embeds_redes_1_pcs():

    lista = []

    lista.append(get_embed_redes_1_pc1())
    lista.append(get_embed_redes_1_pc2())
    lista.append(get_embed_redes_1_pc3())
    lista.append(get_embed_redes_1_pc4())
    lista.append(get_embed_redes_1_pc5())
    lista.append(get_embed_redes_1_exparcial())
    lista.append(get_embed_redes_1_exfinal())
    lista.append(get_embed_redes_1_exsusti())
    lista.append(get_embed_redes_1_entrada())

    return lista


def get_embeds_sistemas_operativos_1_pcs():

    lista = []

    lista.append(get_embed_sistemas_operativos_1_pc1())
    lista.append(get_embed_sistemas_operativos_1_pc2())
    lista.append(get_embed_sistemas_operativos_1_pc3())
    lista.append(get_embed_sistemas_operativos_1_pc4())

    return lista

def get_embeds_quimica_1_labos():

    lista = []

    lista.append(get_embed_quimica_1_laboratorios_2021_II())
    
    return lista

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def get_embeds_cursos_labs_pcs_clases_segundo_ciclo():

    lista1 = [] # Laboratorios

    lista1.append("blank")
    lista1.append("blank")
    lista1.append("blank")
    lista1.append(get_embeds_quimica_1_labos()) # Química 1 Laboratorios

    lista2 = [] # PC's, exámenes

    lista2.append(get_embeds_fisica_2_pcs())
    lista2.append(get_embeds_calculo_integral_pcs())
    lista2.append(get_embeds_algoritmos_1_pcs())
    lista2.append(get_embeds_quimica_1_pcs())
    lista2.append(get_embeds_fundamentos_computador_pcs())
    lista2.append("get_embeds_redaccion_pcs()")
    lista2.append(get_embeds_redes_1_pcs())
    lista2.append(get_embeds_sistemas_operativos_1_pcs())

    lista3 = [] # Clases

    lista3.append("blank")

    lista = [] # Laboratorios, PC's y clases unidas

    lista.append(lista1) # [0] Laboratorios
    lista.append(lista2) # [1] PC's, exámenes
    lista.append(lista3) # [2] Clases

    return lista

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
