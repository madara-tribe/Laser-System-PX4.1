import tempfile
import os
import shutil
import cv2

def cv2_video_writer(w=1280, h=720, filename='output.mov'):
    # camera init
    fps = 10 # int(cap.get(cv2.CAP_PR
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    vid_writer = cv2.VideoWriter(filename, fourcc, fps, (w, h))
    return vid_writer

class Tmpfile:
    def __init__(self):
        self.tmpdir = "/tmp/tmp_2s487t8" #tempfile.mkdtemp()
        if isinstance(self.tmpdir, str):
            os.makedirs(self.tmpdir, exist_ok=True)
        print(self.tmpdir)
        
    def Xfile(self, fname):
        self.Xname = fname
        
    def Yfile(self, fname):
        self.Yname = fname
        
    def Xwrite(self, val):
        fp = open(os.path.join(self.tmpdir, self.Xname), 'w+', encoding='utf-8')
        fp.write(str(val))
        
    def Ywrite(self, val):
        fp = open(os.path.join(self.tmpdir, self.Yname), 'w+', encoding='utf-8')
        fp.write(str(val))
        
    def delete(self):
        shutil.rmtree(self.tmpdir)
