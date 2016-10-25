import sys
import jpgTools as jt
import mappingTools as mt
import glob

def inputdata():
    
    imgFile = input('Enter the image files: ')
    
    # input lat and lon
    while True:
        try:
            lat1 = eval(input('Enter origin latitude (in decimals): '))
            lon1 = eval(input('Enter origin longitude (in decimals): '))
            #if (lat1 <= 180.0 and lat1 >= -180.0):
            if (mt.validateLat(lat1)):
                #if(lon1 <= 90.0 and lon1 >= -90.0): break
                if(mt.validateLon(lon1)): break
                else: 
                    print ('The value you entered is incorrect, please enter again.')
                    continue
            else: 
                print ('The value you entered is incorrect, please enter again.')
                continue
                
        except ValueError:
            print ('The value you entered is incorrect, please enter again.')
        except TypeError:
            print ('The value you entered is incorrect, please enter again.')

    #input threshold
    while True:
        try:        
            threshold = eval(input('Enter the threshold (in KM): '))
            if (mt.validateRadius(threshold)): break
            else: continue

        except ValueError:
            print ('The value you entered is incorrect, please enter again.')

    outputFileName = input('Enter the output file name: ')

    return imgFile, lat1, lon1, threshold, outputFileName

    
def main():
    
    latPix = None
    lonPix = None
    
    if (len(sys.argv) >= 1):
        try:
            (directory, lat_origin, lon_origin, threshold, outputFileName) = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
            outputFileHandle = open(outputFileName, "w")
        
        except:
            (directory, lat_origin, lon_origin, threshold, outputFileName) = inputdata()
            outputFileHandle = open(outputFileName, "w")
        
    else:
        print('No files provided on the command line.')
        (directory, lat_origin, lon_origin, threshold, outputFileName) = inputdata()
        outputFileHandle = open(outputFileName, "w")
    
    for fileName in glob.glob(directory):
        exifData = jt.getExifData(fileName)
        latPix = jt.getLatLon(exifData)[0]
        lonPix = jt.getLatLon(exifData)[1]

        if (latPix != None) and (lonPix != None):
            distance = mt.distanceBetweenPoints(lat_origin, lon_origin, latPix, lonPix) * mt.earthRadiusKm
           
            if (distance <= threshold):

                print(fileName, latPix, lonPix, sep=",", end="\n", file=outputFileHandle)
                print(fileName, latPix, lonPix, sep=",", end="\n")
    
    outputFileHandle.close()
main()
#48.863, 2.326 /eccs/users/charliep/courses/cs128/images/*.jpg
#/eccs/users/charliep/courses/cs128/images/*.jpg