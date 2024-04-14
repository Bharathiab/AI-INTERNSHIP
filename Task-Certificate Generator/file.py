import cv2

list_of_names = ['Cristopher Greman','John Ken','Abdul', 'Rahim', 'Harris', 'Akshit', 'Samuel']

for index, name in enumerate(list_of_names):
    template = cv2.imread(r"C:\Users\S.Bharathi\Desktop\certificate generator\Sample-Certificate.png")
    cv2.putText(template, name, (187, 176), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imwrite(f'C:/Users/S.Bharathi/Desktop/certificate gen/generated certificate/{name}.jpg', template)
    print('Processing Certificate {}/{}'.format(index + 1, len(list_of_names)))
