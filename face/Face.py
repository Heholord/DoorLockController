import cv2
import os
import numpy as np


class Face_recognizer:
    def __init__(self):
        self.subjects = ["", ]
        self.training_folder = "training"
        self.test_dir = "test"

    def detect_face(self, img):
        #convert the test image to gray image as opencv face detector expects gray images
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #load OpenCV face detector, I am using LBP which is fast
        #there is also a more accurate but slow Haar classifier
        face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

        #let's detect multiscale (some images may be closer to camera than others) images
        #result is a list of faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

        #if no faces are detected then return original img
        if (len(faces) == 0):
            return None, None

        #under the assumption that there will be only one face,
        #extract the face area
        (x, y, w, h) = faces[0]

        #return only the face part of the image
        return gray[y:y+w, x:x+h], faces[0]

    def prepare_training_data(self, data_folder_path):
        #------STEP-1--------
        #get the directories (one directory for each subject) in data folder
        dirs = os.listdir(data_folder_path)

        #list to hold all subject faces
        faces = []
        #list to hold labels for all subjects
        labels = []

        #let's go through each directory and read images within it
        for dir_name in dirs:

            #our subject directories start with letter 's' so
            #ignore any non-relevant directories if any
            if not dir_name.startswith("s"):
                continue;

            #------STEP-2--------
            #extract label number of subject from dir_name
            #format of dir name = slabel
            #, so removing letter 's' from dir_name will give us label
            label = int(dir_name.replace("s", ""))

            #build path of directory containin images for current subject subject
            #sample subject_dir_path = "training-data/s1"
            subject_dir_path = data_folder_path + "/" + dir_name

            #get the images names that are inside the given subject directory
            subject_images_names = os.listdir(subject_dir_path)

            #------STEP-3--------
            #go through each image name, read image,
            #detect face and add face to list of faces
            for image_name in subject_images_names:

                #ignore system files like .DS_Store
                if image_name.startswith("."):
                    continue;

                #build image path
                #sample image path = training-data/s1/1.pgm
                image_path = subject_dir_path + "/" + image_name
                print(image_path)

                #read image
                image = cv2.imread(image_path)

                #display an image window to show the image
                cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
                cv2.waitKey(100)

                #detect face
                face, rect = self.detect_face(image)

                #------STEP-4--------
                #for the purpose of this tutorial
                #we will ignore faces that are not detected
                if face is not None:
                    #add face to list of faces
                    faces.append(face)
                    #add label for this face
                    labels.append(label)

        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()

        return faces, labels

    def draw_rectangle(self, img, rect):
        (x, y, w, h) = rect
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    def draw_text(self, img, text, x, y):
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    def predict(self, test_img):
        #make a copy of the image as we don't want to chang original image
        img = test_img.copy()
        #detect face from the image
        face, rect = self.detect_face(img)

        #predict the image using our face recognizer
        label, confidence = self.face_recognizer.predict(face)
        #get name of respective label returned by face recognizer
        label_text = self.subjects[label]

        #draw a rectangle around face detected
        self.draw_rectangle(img, rect)
        #draw name of predicted person
        self.draw_text(img, label_text, rect[0], rect[1]-5)

        return img

    def recognize(self):
        test_images_folder = os.listdir(self.test_dir)

        test_images = []
        predicted_images = []

        for image_name in test_images_folder:
            #ignore system files like .DS_Store
            if image_name.startswith("."):
                continue;
            #load test images
            test_images.append(cv2.imread(self.test_dir + "/" + image_name))

        for image in test_images:
            # perform a prediction
            predicted_images.append(self.predict(image))
            print("Prediction complete")

        i = 0
        for image in predicted_images:
            # display both images
            cv2.imshow(self.subjects[i], cv2.resize(image, (400, 500)))
            i += 1

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        exit

    def train(self):
        faces, labels = self.prepare_training_data(self.training_folder)

        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_recognizer.train(faces, np.array(labels))
        return self.face_recognizer


    def test(self):
        self.train()
        self.recognize()
