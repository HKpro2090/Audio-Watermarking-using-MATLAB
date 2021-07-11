function e = decoder(audio,key1,imgname)

%reading encoded audio file
disp('Reading Audio')
[audiodata , samples]=audioread(audio);

%converting audio file to binary array
binaudio= dec2bin(uint8((audiodata+.5).*255),16);

%Getting Key and Checking Validity
key = str2num(key1);
if key<1000 || key>9999
    disp('Invalid Key');
    return
end

%Decoding Image Dimensions
f=2*key;
binimginfo=repmat(char(0),4,32); %pre allocating to improve speed (optimisation)
for i=1:4
    for j=1:32
        binimginfo(i,j)=binaudio(f,16);
        f=f+1;
    end
end
imginfo=bin2dec(binimginfo);
imginfo=imginfo./key;
r=imginfo(1);
c=imginfo(2);
d=imginfo(3);
bl=imginfo(4);

%Checking key validity
if (mod(r,1)) ~= 0 || mod(c,1)~=0 || mod(d,1)~=0 || mod(bl,1)~=0 || r<1
    disp('Wrong Key');
    return
end

%reading image data from binary audio
disp('Decrypting Audio')

%pre allocating to improve speed (optimisation)
rimgbin=repmat(char(0),r*c,bl);
gimgbin=repmat(char(0),r*c,bl);
bimgbin=repmat(char(0),r*c,bl);

for i=1:(r*c)
    for j=1:bl
    rimgbin(i,j)=binaudio(f,16);
    gimgbin(i,j)=binaudio((f+(r*c*bl)),16);
    bimgbin(i,j)=binaudio((f+(r*c*bl*2)),16);
    f=f+1;
    end
end

%Converting binary image data into double
rdecimg=double(bin2dec(rimgbin));
gdecimg=double(bin2dec(gimgbin));
bdecimg=double(bin2dec(bimgbin));

%Decrypting image data
disp('Decrypting Image')
rdecimg=rdecimg./key;
gdecimg=gdecimg./key;
bdecimg=bdecimg./key;

%Reconstructing R G B Image layers
disp('Creating Image')
rimg=uint8((reshape(rdecimg,r,c)));
gimg=uint8((reshape(gdecimg,r,c)));
bimg=uint8((reshape(bdecimg,r,c)));

%Assembling the RGB Image Layers 
disp('Showing Image')
imdata=(cat(d,rimg,gimg,bimg));
imdata=reshape(imdata,c,r,d);

%Rotating and Displaying the Image
imdata=rot90(imdata,3);
imdata = flimdim(imdata,2);
imshow(imdata)

%Writing the Image File
imgname=strcat(imgname,'.png');
imwrite(imdata,imgname,'png');
disp('Decryption Complete!!')
e = 'Thank you';
