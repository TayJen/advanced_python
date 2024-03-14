from latex_tayjen.latex import make_latex_table


if __name__ == '__main__':
    table = [
        ["Name", "Profit", "Work"],
        ["Ivan", 2000, "Sberbank"],
        ["Dmitry", 4000, "Gazprom"],
        ["Evgeny", 3500, "Yandex"]
    ]

    with open('./artifacts/2_1.tex', 'w', encoding='utf-8') as f_tex:
        for row in make_latex_table(table, need_base=True):
            f_tex.write(row)
