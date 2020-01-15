function [ ceny, cenx ] = TCOG( Spot, Threshold )
% function [ ceny cenx ] = COG( Spot, Threshold )
% Returns the centroid of a lone spot by the Thresholding centroid method
% (TCOG) with selectable Threshold

[sizey, sizex] = size(Spot);
Thr = Threshold*max(max(Spot));
Spot = Spot-Thr;

cenx = 0;
Tot = 0;
for x = 1:sizex
    for y = 1:sizey
        if Spot(y,x) > 0
            cenx = cenx + x*Spot(y,x);  %centro de grav x= coord*valor
            Tot = Tot + Spot(y,x);      %Soma apenas os valores acima da treshold
        end
    end
end
cenx = cenx/Tot;
cenx = cenx - sizex/2 - 0.5;            %recentra?

ceny = 0;
Tot = 0;
for x = 1:sizex
    for y = 1:sizey
        if Spot(y,x) > 0
            ceny = ceny + y*Spot(y,x);
            Tot = Tot + Spot(y,x);
        end
    end
end
ceny = ceny/Tot;
ceny = ceny - sizey/2 - 0.5;
end