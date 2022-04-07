Va = P*L/2+M1/L-M2/L;
Vb = P*L/2-M1/L+M2/L;
Vmax = Math.Max(Va,Vb);
xv0 = Va/P;
Mpos = Va*xv0-P*xv0*xv0/2-M1;
Mneg1 = M1;
Mneg2 = M2;
Cargas = [M1,Mpos,M2];