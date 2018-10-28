function [imgRow, imgCol, FaceContainer, faceLabel] = ReadFaces(nFacesPerPerson, nPerson, bTest)

%nPerson : the number of person

nargin = 0;
if nargin == 0
    nFacesPerPerson = 5;%train by 5 photos
    nPerson = 40;
    bTest = 0;
elseif nargin < 3
    bTest = 0;
end

img = imread('D:\***');
[imgRow, imgCol] = size(img);

FaceContainer = zeros(nFacesPerPerson * nPerson, imgRow * imgCol);
faceLabel = zeros(nFacesPerPerson * nPerson, 1);

for i = 1: nPerson
    i1 = mod(i, 10);
    i0 = char(i / 10);
    strPath = '***';
    if(i0 ~= 0)
        strPath = strcat(strPath, '0' + i0);
    end
    strPath = strcat(strPath, '0' + i1);
    strPath = strcat(strPath, '\');
    tempStrPath = strPath;
    for j = 1: nFacesPerPerson
        strPath = tempStrPath;
        if bTest == 0
            strPath = strcat(strPath, '0' + j);
        else
            strPath = strcat(strPath, num2str(5+j));
        end
        strPath = strcat(strPath, '.pgm');
        img = imread(strPath);
        FaceContainer((i - 1) * nFacesPerPerson + j, :) = img(:);
        faceLabel((i - 1) * nFacesPerPerson + j) = i;
    end
end

save('FaceMat.mat', 'FaceContainer')    
