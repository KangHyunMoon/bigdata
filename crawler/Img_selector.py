import cv2 as cv
import os
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump

# 건물 : [237 242 245]
# 땅 : [209 221 224]
# 땅2 : [239 244 246]
# 산 : [158 219 179]
# 물 : [232 199 157]

building = [237, 242, 245]
building2 = [246, 243, 240]
building3 = [249, 251, 252]
mountain = [158, 219, 179]
water = [232, 199, 157]


def indent(elem, level=0):
    i = "\n" + level * "	"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "	"

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i

    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def __main__():

    file_folder = "img_basic"

    files = []

    for (dirpath, dirname, filenames) in os.walk('./' + file_folder + '/'):
        files = filenames

    #print(files)
    for file in files:
        img_color = cv.imread('./' + file_folder + '/' + file, cv.IMREAD_COLOR)

        #cv.imshow('result', img_color)
        #cv.waitKey(0)

        #mask for threshhold.
        for idy,y in enumerate(img_color):
            for idx,x in enumerate(y):
                x = list(x)
                #print(x)
                if (x != building) & (x != building2) & (x != building3)\
                        & (x != mountain) & (x != water) :
                    img_color[idy,idx] = [0,0,0]

        img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
        #color to gray

        ret, img_binary = cv.threshold(img_gray, 127,255, cv.THRESH_BINARY)
        # cv.imshow('result1', img_binary)
        # cv.waitKey(0)
        # gray to binary

        _, contour, hi = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        #find cont

        if len(contour) == 0:
            continue

        # xml tree :)

        annotation = Element("annotation")

        folder = Element("folder")
        folder.text = "img_satellite"
        annotation.append(folder)

        filename = Element("filename")
        filename.text = file
        annotation.append(filename)

        path = Element("path")
        path.text = os.getcwd() + "\\" + file
        #print(path.text)
        annotation.append(path)

        source = Element("source")

        database = Element("database")
        database.text = "Unknown"
        source.append(database)

        annotation.append(source)

        size = Element("size")

        width = Element("width")
        width.text = str(len(img_color))
        size.append(width)
        height = Element("height")
        height.text = str(len(img_color[0]))
        size.append(height)
        depth = Element("depth")
        depth.text = "3"
        size.append(depth)

        annotation.append(size)

        segmented = Element("segmented")
        segmented.text = "0"
        annotation.append(segmented)

        for cont in contour:

            object = Element("object")

            if len(cont) < 5:
                continue

            inner_fixel = img_color[cont[0][0][1],cont[0][0][0]]

            min_x = 10000
            min_y = 10000
            max_x = 0
            max_y = 0

            for i in cont :
                #print(i[0])
                if i[0][0] > max_x:
                    max_x = i[0][0]
                if i[0][1] > max_y:
                    max_y = i[0][1]

                if i[0][0] < min_x:
                    min_x = i[0][0]

                if i[0][1] < min_y:
                    min_y = i[0][1]

            if (max_x > len(img_color) | (max_y > len(img_color[0]))):
                continue

            name = Element("name")

            if (list(inner_fixel) == list(building)) | (list(inner_fixel) == list(building2)) | (list(inner_fixel) == list(building3)) :
                name.text = "building"
            elif (list(inner_fixel) == list(mountain)):
                name.text = "mountain"
            elif (list(inner_fixel) == list(water)):
                name.text = "water"
            else :
                #print("error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                #print("%d %d %d", inner_fixel[0], inner_fixel[1], inner_fixel[2])
                #cv.line(img_color, (min_x, min_y), (min_x, min_y), (0, 255, 0), 5)
                pass

            cv.line(img_color, (min_x, min_y), (min_x, min_y), (255, 0, 0), 5)
            cv.line(img_color, (min_x, max_y), (min_x, max_y), (255, 0, 0), 5)
            cv.line(img_color, (max_x, min_y), (max_x, min_y), (255, 0, 0), 5)
            cv.line(img_color, (max_x, max_y), (max_x, max_y), (255, 0, 0), 5)

            object.append(name)

            pose = Element("pose")
            pose.text = "Unspecified"
            object.append(pose)

            truncated = Element("truncated")

            if (min_x == 10000) | (min_y == 10000) | (max_x == 0) | (max_y == 0) :
                truncated.text = "1"

            else :
                truncated.text = "0"

            object.append(truncated)

            difficult = Element("difficult")
            difficult.text = "0"
            object.append(difficult)

            bndbox = Element("bndbox")

            xmin = Element("xmin")
            xmin.text = str(min_x)
            bndbox.append(xmin)

            ymin = Element("ymin")
            ymin.text = str(min_y)
            bndbox.append(ymin)

            xmax = Element("xmax")
            xmax.text = str(max_x)
            bndbox.append(xmax)

            ymax = Element("ymax")
            ymax.text = str(max_y)
            bndbox.append(ymax)

            object.append(bndbox)

            annotation.append(object)

            #cv.drawContours(img_color, [cont], 0, (255,0,0), 3)

        indent(annotation)

        TREE = ElementTree(annotation)

        TREE.write("./annotation/" + file + ".xml")

        #cv.imshow('result', img_color)
        #cv.waitKey(0)

        cv.imwrite("./img_basic_dot/" + file + ".png", img_color)

        print(file + ".png")


__main__()