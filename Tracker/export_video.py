# USeage: python export_video.py --path saved_frames/cam_01/

import cv2
import os
import argparse
import time


def get_argument():
	parser = argparse.ArgumentParser(description='Convert images to video')
	parser.add_argument("--path", '-p', required=True, help="The directory path of images.")
	parser.add_argument("--frame_rate", "-fps", default=10, help="The frame rate of video.")
	return vars(parser.parse_args())

def export_from_image_to_video(input_path: str, output_path: str, frame_rate): 

	image_folder = input_path
	video_name = output_path

	images = []

	for file in os.listdir(image_folder):
		# print(file)
		# input()
		images.append(int(file.rstrip(".jpg"))
	
	images.sort()	

	print(os.path.join(image_folder, images[0]))
	input()

	frame = cv2.imread(os.path.join(image_folder, images[0]))
	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, 0, frame_rate, (width,height))

	count = 0

	for image in images:
		count += 1
		video.write(cv2.imread(os.path.join(image_folder, str(image) + ".jpg")))
		if count % 100 == 0:
			print("[INFO] Processing the frame {:>8} th".format(count))

	cv2.destroyAllWindows()
	video.release()


def main(args):

	video_path = os.path.join("output_trackers", args['path'].split("/")[-2] + ".avi")
	
	print("The image got from camera {}.".format(args['path'].split("/")[-2]))
	print("The output video have path {}".format(video_path))
	print("The frame per seconds (fps) parameter: {}".format(args['frame_rate']))
	time.sleep(1)

	export_from_image_to_video(input_path=args['path'], output_path=video_path, frame_rate=args['frame_rate'])


if __name__ == '__main__':
	args = get_argument()
	main(args)
