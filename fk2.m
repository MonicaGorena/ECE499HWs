function [T]=fk2(l1,l2,a1,a2)
r1= [cosd(a1) -sind(a1) 0; sind(a1) cosd(a1) 0; 0 0 1];
r2= [cosd(a2) -sind(a2) 0; sind(a2) cosd(a2) 0; 0 0 1];
d1= [l1;0;0];
d2=[l2;0;0];
d11=r1*d1;
d22=r2*d2;
t1=[r1, d11; 0 0 0 1];
t2=[r2, d22; 0 0 0 1];
T=t1*t2

end
