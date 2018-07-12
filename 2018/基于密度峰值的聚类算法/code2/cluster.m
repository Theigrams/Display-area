%% Clustering by density peaks
clc;clear;
%% 输入数据的距离矩阵
load('data1.dat');
%距离矩阵中第一列为 元素i 
%第二列为元素 j
%第三列为元素 i,j 之间的距离

A=data1;
n=max(A(:,2));
N=size(A,1);
D=zeros(n,n);
for i=1:N 
    D(A(i,1),A(i,2))=A(i,3);
    D(A(i,2),A(i,1))=A(i,3);
end

p=2;

%升序排列distance，然后取1%到2%的那个distance作为dc
position=round(N*p*2/100); 
sort_d=sort(A(:,3));
dc=sort_d(position);


%% 计算数据的密度 rho (利用 chi)
%rho=sum(D(:,:)<dc,2);

%% Gaussian kernel
rho=sum(exp(-D.^2./(dc^2)),2);

% 计算聚类中心点的密度

%% 将 rho 按降序排列，ordrho 保持序
[rho_sorted,ordrho]=sort(rho,'descend');

  
%% 处理 rho 值最大的数据点
delta(ordrho(1))=max(D(ordrho(1),:));

%% 计算delta矩阵
for i=2:n
    [delta(ordrho(i)),idx_delta]=min(D(ordrho(i),ordrho(1:i-1)));
    neigh(ordrho(i))=ordrho(idx_delta);
end

%% 画出决策图
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


%% 计算分配矩阵
% 人为确定聚类个数
k=input('请输入聚类的个数：\n')
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
%% 画出聚类后的图
for i=1:k
    T=find(assign==i);
    fprintf('\nCluster %d :\n\n',i)
    disp(T')
end






