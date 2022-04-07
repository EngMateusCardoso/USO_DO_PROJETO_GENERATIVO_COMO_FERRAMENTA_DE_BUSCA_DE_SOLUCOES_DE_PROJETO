vType = FamilyInstance.Type(vigaV);
cor;
b1=b;
h1=h;
c1=c;
custo;
//Parametros de tipo
pt1=vType.Parameters[0].Name;
 //b;
pt2=vType.Parameters[12].Name;
 //h;
pt3=vType.Parameters[7].Name;
 //custo;
//Parametros de instância
pi1=vigaV.Parameters[30].Name;
 //cobrimento;
pi2=vigaV.Parameters[31].Name;
 //cobrimento;
pi3=vigaV.Parameters[32].Name;
 //cobrimento;
updatevalues=[Imperative]{
if(vType!=null && vigaV!=null){
vType.SetParameterByName(pt1, b1);
vType.SetParameterByName(pt2, h1);
vType.SetParameterByName(pt3, custo);
//
vigaV.SetParameterByName(pi1, c1);
vigaV.SetParameterByName(pi2, c1);
vigaV.SetParameterByName(pi3, c1);
vigaV.OverrideColorInView(cor);
vType=null;
return "Atualizado!";
}else{return "Não atualizar!";
};
};