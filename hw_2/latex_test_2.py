from latex_tayjen import make_latex_table, create_base_latex_and_insert_image


if __name__ == '__main__':
    table = [
        ["Name", "Profit", "Work"],
        ["Ivan", 2000, "Sberbank"],
        ["Dmitry", 4000, "Gazprom"],
        ["Evgeny", 3500, "Yandex"]
    ]

    img_path = 'D:/main/university/itmo/courses/advanced_python/hw_2/images/superJumbo.jpg'
    tex_path = './artifacts/2_2.tex'

    with open(tex_path, 'w', encoding='utf-8') as f_tex:
        for latex_img_row in create_base_latex_and_insert_image(img_path):
            f_tex.write(latex_img_row)
            if img_path in latex_img_row:
                f_tex.write('\n')
                for row in make_latex_table(table, need_base=False):
                    f_tex.write(row)
