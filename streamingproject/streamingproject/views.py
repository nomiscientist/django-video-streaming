from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse, HttpResponseServerError

from django.views.decorators import gzip

import cv2
import time

class VideoCamera(object):
    def __init__(self,path):
        self.video = cv2.VideoCapture(path)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret,image = self.video.read()
        ret,jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def indexscreen(request): 
    try:
        template = "screens.html"
        return render(request,template)
    except HttpResponseServerError:
        print("aborted")

@gzip.gzip_page
def dynamic_stream(request,num=0,stream_path="172.16.4.129"):
    stream_path = "rtsp://admin:admin123@"+stream_path+"/streaming/channels/2"
    return StreamingHttpResponse(gen(VideoCamera(stream_path)),content_type="multipart/x-mixed-replace;boundary=frame")

