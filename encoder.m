function e = encoder(img,audio,email,filename)

%Reading Image File
disp('Reading Image....')
sourceimage=imread(img);
[r,c,d]=size(sourceimage);
rsi=sourceimage(:,:,1);
gsi=sourceimage(:,:,2);
bsi=sourceimage(:,:,3);

%Key Genearation
disp('Generating key...')
rng('shuffle');
key=randi([1000 9999],1,1);
key2=int2str(key);
disp('Reading Image....')

%converting image data into a linear 1-D array
linimage=zeros(1,r*c*d); %pre allocating to improve speed (optimisation)
f=1;
for i=1:r
    for j=1:c
            linimage(f)=rsi(i,j);
            linimage(f+(r*c))=gsi(i,j);
            linimage(f+(2*r*c))=bsi(i,j);
       f=f+1;
    end
end

disp('Reading audio file....')
%reading audio file and converting to binary array
[audiodata , samples]=audioread(audio);
binaudio= dec2bin(uint8((audiodata+0.5).*255),16);

disp('Encrypting....')
%encryption 
linimage=double(linimage);
linimage1=linimage.*key;
binimage=dec2bin(linimage1);
binimagesize=size(binimage);
bl=binimagesize(2);

%file boundary checking
if r*c*d*bl>(length(binaudio))
     disp('Watermark too large for the given audio file, use a larger audio file or a smaller watermark image')
    return
end

disp('Writing encrypted Audio....')
%writing image dimensions to audio file
imginfo=[r c d bl];
imginfo=imginfo.*key;
binimginfo=dec2bin(imginfo,32);
k=2*key;
for i=1:4
    for j=1:32
        binaudio(k,16)=binimginfo(i,j);
        k=k+1;
    end
end


%writing the image data to audio file
for i=1:r*c*d
    for j=1:bl
        binaudio(k,16)=binimage(i,j);
        k=k+1;
    end
end

%converting the encrypted audio back to decimal and writing the file.
encodedaudio = bin2dec(binaudio);
encodedaudio=reshape(encodedaudio,length(encodedaudio)/2,2);
filename=strcat(filename,'.wav');
audiowrite(filename,(double(encodedaudio)./255 - .5),samples);

disp('Sending Email....')

setpref('Internet','SMTP_Server','smtp.gmail.com');
setpref('Internet','E_mail','harikrishnan.vamsi2018@vitstudent.ac.in');
setpref('Internet','SMTP_Username','harikrishnan.vamsi2018@vitstudent.ac.in');
setpref('Internet','SMTP_Password','print.active@2090');
props = java.lang.System.getProperties;
props.setProperty('mail.smtp.auth','true');
props.setProperty('mail.smtp.socketFactory.class', 'javax.net.ssl.SSLSocketFactory');
props.setProperty('mail.smtp.socketFactory.port','465');
sendmail(email,'Passkey for Decoding',key2) ;
disp('Encrypting Complete!')
e = 'Thank you';
