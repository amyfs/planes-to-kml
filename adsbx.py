import json,sys
import simplekml as sk

def read_json(obj):
    lst = []
    for item in obj["trace"]:
        lst.append((item[2],item[1]))
    return lst

def make_kml(lst,filename):
    kml = sk.Kml()
    kml.newlinestring(coords=lst)
    kml.save(filename+".kml")

if __name__ == "__main__":
    with open(sys.argv[1],"r") as f:
        j = json.load(f)
        l = read_json(j)
        make_kml(l,sys.argv[1])


