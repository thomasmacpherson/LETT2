

while in tap through mode:
	if colourPickerButton:
		break

	if screenChange:
		if pixelAt(x,y) != -1: # not a custom colour
			if pixelAt(x,y) == numberOfStandardCOlours-1:
				pixelAt(x,y) = 0
			else
				pixelAt(x,y)++
		else
			pixelAt(x,y) = 0  # custom colour set to first standard colour
		refreshPixel(x,y)
	
	while in colourPickerMode:
		wait for selected pixel
		calculate colour RGB values

		while customColour:
			if screenChange:
				pixelAt(x,y) = -1
				changePixelColour(R,G,B)
				refreshPixel(x,y)
