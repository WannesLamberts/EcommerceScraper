def ToJson(products,images):
    f = open('products.json', 'w')
    f.write("{\"products\":[")
    for x in range(len(products)-1):
        f.write("{ \"productname\":\""+str(products[x].productName)+"\",")
        f.write("\"brand\":\""+str(products[x].brand)+"\",")
        f.write("\"price\":\""+str(products[x].price)+"\",")
        f.write("\"images\":\""+str(images[x])+"\"")
        f.write("},\n")

    f.write("{ \"productname\":\"" + str(products[len(products)-1].productName) + "\",")
    f.write("\"brand\":\"" + str(products[len(products)-1].brand) + "\",")
    f.write("\"price\":\"" + str(products[len(products)-1].price) + "\",")
    f.write("\"images\":\"" + str(images[x]) + "\"")

    f.write("}\n")

    f.write("]}")
    f.close()
