# coding=utf-8

def CreateIcon():
    file_name = input("请输入应用名称：")
    file_fullname = "/usr/share/applications/" + file_name + ".desktop"
    f = open(file_fullname, "w")
    exec_path = input("请输入二进制文件地址（绝对地址）:")
    icon_path = input("请输入图标地址（绝对地址）:")
    print("1.Development;IDE;\n2.Office;\n3.System;\n4.Network;\n5.chat;\n6.Audio;AudioVideo;\n7.Player;AudioVideo;"
          "\n8.Graphics")
    try:
        categoriesNum = int(input("请选择你的应用类型："))
    except ValueError:
        print("请输入相应的序号！！！")
    else:
        if categoriesNum <= 8:
            categoriesTable = {1: "Development;IDE;", 2: "Office;", 3: "System;", 4: "Network;", 5: "chat;",
                               6: "Audio;AudioVideo;",
                               7: "Player;AudioVideo;", 8: "Graphics;"}
            categories = categoriesTable[categoriesNum]
            text = "[Desktop Entry]\nName=" + file_name + "\nType=Application\nTerminal=False\nExec=" + exec_path + \
                   "\nIcon=" + icon_path + "\nCategories=" + categories
            f.write(text)
        else:
            print("输入的数字过大了!!!")


if __name__ == "__main__":
    CreateIcon()
