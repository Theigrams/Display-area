clc;
clear;
format long;
data = csvread('link.csv');
alpha = 0.85;
% AA[i,j]==1表示用户 i 关注了用户 j
% sum(AA,1)为行向量，表示i的被关注人数
% sum(AA,2)为列向量，表示i的关注人数
data = data';
sum_data = sum(data,1);
order = find(sum_data == 0);

for i = 1 : length(data(1, :))
    if ismember(i, order) == 0
        data(:, i) = data(:, i) / sum_data(i);
    end
end

P = ones(size(data,1),1)/size(data,1);
E = (1 - alpha) * P;

for i=1:10000
    P = alpha * data * P + E;
end
P