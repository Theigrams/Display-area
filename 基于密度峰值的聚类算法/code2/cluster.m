%% Clustering by density peaks
clc;clear;
%% �������ݵľ������
load('data1.dat');
%��������е�һ��Ϊ Ԫ��i 
%�ڶ���ΪԪ�� j
%������ΪԪ�� i,j ֮��ľ���

A=data1;
n=max(A(:,2));
N=size(A,1);
D=zeros(n,n);
for i=1:N 
    D(A(i,1),A(i,2))=A(i,3);
    D(A(i,2),A(i,1))=A(i,3);
end

p=2;

%��������distance��Ȼ��ȡ1%��2%���Ǹ�distance��Ϊdc
position=round(N*p*2/100); 
sort_d=sort(A(:,3));
dc=sort_d(position);


%% �������ݵ��ܶ� rho (���� chi)
%rho=sum(D(:,:)<dc,2);

%% Gaussian kernel
rho=sum(exp(-D.^2./(dc^2)),2);

% ����������ĵ���ܶ�

%% �� rho ���������У�ordrho ������
[rho_sorted,ordrho]=sort(rho,'descend');

  
%% ���� rho ֵ�������ݵ�
delta(ordrho(1))=max(D(ordrho(1),:));

%% ����delta����
for i=2:n
    [delta(ordrho(i)),idx_delta]=min(D(ordrho(i),ordrho(1:i-1)));
    neigh(ordrho(i))=ordrho(idx_delta);
end

%% ��������ͼ
figure

tt=plot(rho,delta,'o','MarkerSize',4,'MarkerFaceColor','k','MarkerEdgeColor','k');
title ('Decision Graph','FontSize',15.0)
xlabel ('\rho')
ylabel ('\delta')

figure
xx=1:n;
gamma=delta/sum(delta).*rho'/sum(rho);
[gamma,ordgamma]=sort(gamma,'descend');
scatter(xx,gamma)


%% ����������
% ��Ϊȷ���������
k=input('���������ĸ�����\n')
assign=zeros(n,1);
for i=1:k
    assign(ordgamma(i))=i;
end

[M,I]=min(D(ordrho(1),ordgamma(1:k)));
neigh(ordrho(1))=ordgamma(I);

for i=1:n
    if(~assign(ordrho(i)))
        assign(ordrho(i))=assign(neigh(ordrho(i))); 
    end
end 
%% ����������ͼ
for i=1:k
    T=find(assign==i);
    fprintf('\nCluster %d :\n\n',i)
    disp(T')
end






