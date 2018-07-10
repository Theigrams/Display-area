%% Clustering by density peaks
% by ZHANG JIN

clc;clear;
% 输入数据的距离矩阵
load('spiral.txt');
P=spiral;
n=size(P,1);
N=n*n;
D=zeros(n,n);
for i=1:n 
    for j=1:n
         D(i,j)=get_distance(P(i,1),P(i,2),P(j,1),P(j,2));
    end
end

% 升序排列distance，然后取1%到2%的那个distance作为dc
p=2;
position=round(N*p*2/100); 
sort_d=sort(D(:));
dc=sort_d(position);

%% 计算密度rho 
% cutoff
% rho=sum(D(:,:)<dc,2);

% Gaussian kernel
rho=sum(exp(-D.^2./(dc^2)),2);

%% 计算距离delta
% 将 rho 按降序排列，ordrho 保持序
[rho_sorted,ordrho]=sort(rho,'descend');

% 处理 rho 值最大的数据点
delta(ordrho(1))=max(D(ordrho(1),:));

% 计算delta矩阵
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
figure
for i=1:k
    T=find(assign==i);
    hold on
    plot(P(T,1),P(T,2),'.','Markersize',10)
end

% 标出聚类中心
title('Clustering by fast search and find of density peaks')
for i=1:k
    plot(P(ordgamma(i),1),P(ordgamma(i),2),'o','MarkerSize',4,'MarkerFaceColor','k','MarkerEdgeColor','k');
end
axis equal

%% 画出neighbor关系图
figure
hold on
axis equal
for i=1:n
 plot([P(ordrho(i),1);P(neigh(ordrho(i)),1)],[P(ordrho(i),2),P(neigh(ordrho(i)),2)])
 pause(0.02)
end


figure
hold on
axis equal
plot(P(:,1),P(:,2),'.','Markersize',10)
%% 距离函数
function z=get_distance(x1,y1,x2,y2)
    z=sqrt((x1-x2)^2+(y1-y2)^2);
end
