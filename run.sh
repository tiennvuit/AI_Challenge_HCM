# Preprocess
################################################################
# Clean all directories contain data                           #
                                                               #
echo "Removing all directories and ..."                        #
                                                               #
rm -rf data/images/*										   #
															   #
# Loop through all videos and extract to images				   #
for video in test_data/*.mp4; 								   #
do  														   #
															   #
	# Get the camera name									   #
	name="$(cut -d'/' -f2 <<<"$video")";                       #
	name="$(cut -d'.' -f1 <<<"$name")";                        #
	   														   #
	# Create output directory store extracted images	       #
	output="data/image/$name"								   #
	mkdir $output											   #
															   #
	echo "Extracting $name to images ..." ;					   #
															   #
	ffmpeg -i $video -r 10/1 $output/image_%d.jpg			   #
															   #
done;														   #
															   #
															   #
################################################################

# Detection progress
############################################################################################################################################################################################################################
print("Detecting vehicle in cam 01 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_01 --output_path data/detection_results/cam_01_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 02 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_02 --output_path data/detection_result/cam_02_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 04 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_04 --output_path data/detection_result/cam_04_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 06 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_06 --output_path data/detection_result/cam_06_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 07 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_07 --output_path data/detection_result/cam_07_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 09 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_09 --output_path data/detection_result/cam_09_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 10 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_10 --output_path data/detection_result/cam_10_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 12 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_12 --output_path data/detection_result/cam_12_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 14 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_14 --output_path data/detection_result/cam_14_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 16 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_16 --output_path data/detection_result/cam_16_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 18 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_18 --output_path data/detection_result/cam_18_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 21 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_21 --output_path data/detection_result/cam_21_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 23 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_23 --output_path data/detection_result/cam_23_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
print("Detecting vehicle in cam 24 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_24 --output_path data/detection_result/cam_24_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth

print("Detecting vehicle in cam 03 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_03 --output_path data/detection_result/cam_03_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
print("Detecting vehicle in cam 05 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_05 --output_path data/detection_result/cam_05_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
print("Detecting vehicle in cam 08 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_08 --output_path data/detection_result/cam_08_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
print("Detecting vehicle in cam 11 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_11 --output_path data/detection_result/cam_11_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
print("Detecting vehicle in cam 13 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_13 --output_path data/detection_result/cam_13_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
print("Detecting vehicle in cam 15 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_15 --output_path data/detection_result/cam_15_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
print("Detecting vehicle in cam 17 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_17 --output_path data/detection_result/cam_17_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
print("Detecting vehicle in cam 19 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res.py --input_path data/image/cam_19 --output_path data/detection_result/cam_19_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth

print("Detecting vehicle in cam 20 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res_bw.py --input_path data/image/cam_20 --output_path data/detection_result/cam_20_det.txt --model_path model_weights/Detect/Black_white/output/model_final.pth
print("Detecting vehicle in cam 22 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res_bw.py --input_path data/image/cam_22 --output_path data/detection_result/cam_22_det.txt --model_path model_weights/Detect/Black_white/output/model_final.pth
print("Detecting vehicle in cam 25 ...")
CUDA_VISIBLE_DEVICES=0 python src/Detect/create_detection_res_bw.py --input_path data/image/cam_25 --output_path data/detection_result/cam_25_det.txt --model_path model_weights/Detect/Black_white/output/model_final.pth 
#####################################################################################################################################################################################################################################



