for image_cam in DATA/image/* ;
do 

	name="$(cut -d'/' -f3 <<<"$image_cam")";                   

    echo "$name";
	
done;
