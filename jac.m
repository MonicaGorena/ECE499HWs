function [angles]= jac(x,y)
%analytical method: 
d1=0.3;
d2=0.2;
num=(x^2)+(y^2)-(d1^2)-(d2^2);
den=(2*d1*d2);
angtheo2= acos(num/den)
one=y*(d1+d2*cos(angtheo2))-x*(d2*sin(angtheo2));
two=x*(d1+d2*cos(angtheo2))-y*(d2*sin(angtheo2));
angtheo1=atan(one/two)
%----------------------------------------
% jacobian IK method  
ee=[x;y];
nee=[1;1];
%inital angles
ang1=0.01;
ang2=0.01;
newx=0;
while (.1+1)<newx<(.1-1)
 	%Jacobian inverse
	ja=inv([-(d1*sin(ang1)+d2*sin(ang1+ang2)) -d2*sin(ang1+ang2); d1*cos(ang1)+d2*cos(ang1+ang2) d2*cos(ang1*ang2)]);
	angles=ja*nee
	ang1=angles(1,1);
	ang2=angles(2,1);
	%new pos-> update ee
	T=fk2(d1,d2,ang1,ang2)
	newx=T(1,1);
	newy=T(2,1);
	nee=[newx;newy];
end
end
%call: [result]=jac(.1,.1)

