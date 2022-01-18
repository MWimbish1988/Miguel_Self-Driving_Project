#https://navoshta.com/detecting-road-features/

import os
import os.path
from PIL import Image

f0 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file0 in os.listdir(f0):
    f_img0 = f0+"/"+file0
    img0 = Image.open(f_img0)
    img0 = img0.resize((640, 480))
    img0.save(f_img0)


f1 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file1 in os.listdir(f1):
    f_img1 = f1+"/"+file1
    img1 = Image.open(f_img1)
    img1 = img1.resize((640, 480))
    img1.save(f_img1)

f2 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file2 in os.listdir(f2):
    f_img2 = f2+"/"+file2
    img2 = Image.open(f_img2)
    img2 = img2.resize((640, 480))
    img2.save(f_img2)

f3 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file3 in os.listdir(f3):
    f_img3 = f3+"/"+file3
    img3 = Image.open(f_img3)
    img3 = img3.resize((640, 480))
    img3.save(f_img3)

f4 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file4 in os.listdir(f4):
    f_img4 = f4+"/"+file4
    img4 = Image.open(f_img4)
    im4g = img4.resize((640, 480))
    im4g.save(f_img4)

f5 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file5 in os.listdir(f5):
    f_img5 = f5+"/"+file5
    img5 = Image.open(f_img5)
    img5 = img5.resize((640, 480))
    img5.save(f_img5)

f6 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file6 in os.listdir(f6):
    f_img6 = f6+"/"+file6
    img6 = Image.open(f_img6)
    img6 = img6.resize((640, 480))
    img6.save(f_img6)

f7 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file7 in os.listdir(f7):
    f_img7 = f7+"/"+file7
    img7 = Image.open(f_img7)
    img7 = img7.resize((640, 480))
    img7.save(f_img7)

f8 = r'C:/Users/m_wim/OneDrive/Desktop/DeepPiCar/driver/data/objects'
for file8 in os.listdir(f8):
    f_img8 = f8+"/"+file8
    img8 = Image.open(f_img8)
    img8 = img8.resize((640, 480))
    img8.save(f_img8)
'''
f9 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/9'
for file9  in os.listdir(f9 ):
    f_img9  = f9 +"/"+file9 
    img9  = Image.open(f_img9 )
    img9  = img9 .resize((30, 30))
    img9 .save(f_img9 )

f10 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/10'
for file10 in os.listdir(f10):
    f_img10 = f10+"/"+file10
    img10 = Image.open(f_img10)
    img10 = img10.resize((30, 30))
    img10.save(f_img10)

f11 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/11'
for file11 in os.listdir(f11):
    f_img11 = f11+"/"+file11
    img11 = Image.open(f_img11)
    img11 = img11.resize((30, 30))
    img11.save(f_img11)

f12 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/12'
for file12 in os.listdir(f12):
    f_img12 = f12+"/"+file12
    img12 = Image.open(f_img12)
    img12 = img12.resize((30, 30))
    img12.save(f_img12)

f13 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/13'
for file13 in os.listdir(f13):
    f_img13 = f13+"/"+file13
    img13 = Image.open(f_img13)
    img13 = img13.resize((30, 30))
    img13.save(f_img13)

f14 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/14'
for file14 in os.listdir(f14):
    f_img14 = f14+"/"+file14
    img14 = Image.open(f_img14)
    img14 = img14.resize((30, 30))
    img14.save(f_img14)

f15 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/15'
for file15 in os.listdir(f15):
    f_img15 = f15+"/"+file15
    img15 = Image.open(f_img15)
    img15 = img15.resize((30, 30))
    img15.save(f_img15)

f16 =r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/16'
for file16 in os.listdir(f16):
    f_img16 = f16+"/"+file16
    img16 = Image.open(f_img16)
    img16 = img16.resize((30,30))
    img16.save(f_img16)

f17 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/17'
for file17 in os.listdir(f17):
    f_img17 = f17+"/"+file17
    img17 = Image.open(f_img17)
    img17 = img17.resize((30, 30))
    img17.save(f_img17)

f18 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/18'
for file18 in os.listdir(f18):
    f_img18 = f18+"/"+file18
    img18 = Image.open(f_img18)
    img18 = img18.resize((30, 30))
    img18.save(f_img18)

f19 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/19'
for file19 in os.listdir(f19):
    f_img19 = f19+"/"+file19
    img19 = Image.open(f_img19)
    img19 = img19.resize((30, 30))
    img19.save(f_img19)


f20 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/21'
for file20 in os.listdir(f20):
    f_img20 = f20+"/"+file20
    img20 = Image.open(f_img20)
    img20 = img20.resize((30, 30))
    img20.save(f_img20)

################################################################

f21 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/21'
for file21 in os.listdir(f21):
    f_img21 = f21+"/"+file21
    img21 = Image.open(f_img21)
    img21 = img21.resize((30, 30))
    img21.save(f_img21)


f22 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/22'
for file22 in os.listdir(f22):
    f_img22 = f22+"/"+file22
    img22 = Image.open(f_img22)
    img22 = img22.resize((30, 30))
    img22.save(f_img22)

f23 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/23'
for file23 in os.listdir(f23):
    f_img23 = f23+"/"+file23
    img23 = Image.open(f_img23)
    img23 = img23.resize((30, 30))
    img23.save(f_img23)


f24 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/24'
for file24 in os.listdir(f24):
    f_img24 = f24+"/"+file24
    img24 = Image.open(f_img24)
    img24 = img24.resize((30, 30))
    img24.save(f_img24)

f25= r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/25'
for file25 in os.listdir(f25):
    f_img25 = f25+"/"+file25
    img25 = Image.open(f_img25)
    img25 = img25.resize((30, 30))
    img25.save(f_img25)

f26 =r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/26'
for file26 in os.listdir(f26):
    f_img26 = f26+"/"+file26
    img26 = Image.open(f_img26)
    img26 = img26.resize((30, 30))
    img26.save(f_img26)

f27 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/27'
for file27 in os.listdir(f27):
    f_img27 = f27+"/"+file27
    img27 = Image.open(f_img27)
    img27 = img27.resize((30, 30))
    img27.save(f_img27)

f28 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/28'
for file28 in os.listdir(f28):
    f_img28 = f28+"/"+file28
    img28 = Image.open(f_img28)
    img28 = img28.resize((30, 30))
    img28.save(f_img28)

f29 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/29'
for file29 in os.listdir(f29):
    f_img29= f29+"/"+file29
    img29 = Image.open(f_img29)
    img29 = img29.resize((30, 30))
    img29.save(f_img29)

f30 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/30'
for file30  in os.listdir(f30):
    f_img30  = f30 +"/"+file30 
    img30  = Image.open(f_img30 )
    img30  = img30 .resize((30, 30))
    img30 .save(f_img30 )

f31 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/31'
for file31 in os.listdir(f31):
    f_img31 = f31+"/"+file31
    img31 = Image.open(f_img31)
    img31 = img31.resize((30, 30))
    img31.save(f_img31)

f32 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/32'
for file32 in os.listdir(f32):
    f_img32 = f32+"/"+file32
    img32 = Image.open(f_img32)
    img32 = img32.resize((30, 30))
    img32.save(f_img32)

f33 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/33'
for file33 in os.listdir(f33):
    f_img33 = f33+"/"+file33
    img33 = Image.open(f_img33)
    img33 = img33.resize((30, 30))
    img33.save(f_img33)

f34 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/34'
for file34 in os.listdir(f34):
    f_img34 = f34+"/"+file34
    img34 = Image.open(f_img34)
    img34 = img34.resize((30, 30))
    img34.save(f_img34)

f35 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/35'
for file35 in os.listdir(f35):
    f_img35 = f35+"/"+file35
    img35 = Image.open(f_img35)
    img35 = img35.resize((30, 30))
    img35.save(f_img35)

f36 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/36'
for file36 in os.listdir(f36):
    f_img36 = f36+"/"+file36
    img36 = Image.open(f_img36)
    img36 = img36.resize((30, 30))
    img36.save(f_img36)

f37 =r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/37'
for file37 in os.listdir(f37):
    f_img37 = f37+"/"+file37
    img37 = Image.open(f_img37)
    img37 = img37.resize((30,30))
    img37.save(f_img37)

f38 =r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/38'
for file38 in os.listdir(f38):
    f_img38 = f38+"/"+file38
    img38 = Image.open(f_img38)
    img38 = img38.resize((30, 30))
    img38.save(f_img38)

f39 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/39'
for file39 in os.listdir(f39):
    f_img39 = f39+"/"+file39
    img39 = Image.open(f_img39)
    img39 = img39.resize((30, 30))
    img39.save(f_img39)

f40 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/40'
for file40 in os.listdir(f40):
    f_img40 = f40+"/"+file40
    img40 = Image.open(f_img40)
    img40 = img40.resize((30, 30))
    img40.save(f_img40)

f41 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/41'
for file41 in os.listdir(f41):
    f_img41= f41+"/"+file41
    img41 = Image.open(f_img41)
    img41 = img41.resize((30, 30))
    img41.save(f_img41)

f42 = r'C:/Users/m_wim/OneDrive/Desktop/Autonomous_Self-Driving_Car_by_Use_of_CV/data/Train/42'
for file42 in os.listdir(f42):
    f_img42 = f42+"/"+file42
    img42 = Image.open(f_img42)
    img42 = img42.resize((30, 30))
    img42.save(f_img42)
'''