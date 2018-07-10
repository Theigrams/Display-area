clc;clear;
% 输入数据的距离矩阵
load('spiral.txt');
N=3;
P=spiral;
n=size(P,1);
X=P(:,1:2);
[idx,C] = kmeans(X,N);


figure;
hold on;
axis equal

for i=1:N
    plot(X(idx==i,1),X(idx==i,2),'.','MarkerSize',12)
end

plot(C(:,1),C(:,2),'o','MarkerSize',4,'MarkerFaceColor','k','MarkerEdgeColor','k')
title('K-mean')
hold off