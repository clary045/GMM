% CAPSTONE DESIGN 2 PROJECT: FRUIT SORTING MACHINE
% BY :Clary Norman - 2017141960
% SUPERVISOR: Edwin Vans 
% YEAR: 2020

% This is an example code for collecting fruit sample colors using roipoly
% close all
%  load appledata;
imagepath = './apple';
Samples = [];
for k=1:20
    % Load image
    J = imread(sprintf('%s/%03d.jpg',imagepath,k));
    I = imresize(J,[400 400]);
    
    % You may consider other color space than RGB
    R = I(:,:,1);
    G = I(:,:,2);
    B = I(:,:,3);
    
    % Collect samples 
    disp('');
    disp('INTRUCTION: Click along the boundary of the ball. Double-click when you get back to the initial point.')
    disp('INTRUCTION: You can maximize the window size of the figure for precise clicks.')
    figure(1), 
    mask = roipoly(I); 
    figure(2), imshow(mask); title('Mask');
    sample_ind = find(mask > 0);
    
    R = R(sample_ind);
    G = G(sample_ind);
    B = B(sample_ind);
    
    Samples = [Samples; [R G B]];
     
    
    disp('INTRUCTION: Press any key to continue. (Ctrl+c to exit)')
    pause
end

% Saving sampling data for python
  writematrix(Samples,'Apple_data_test.csv')


% visualize the sample distribution
% figure,
% scatter3(Samples(:,1),Samples(:,2),Samples(:,3),'.');
% title('Pixel Color Distribubtion');
% xlabel('Red');
% ylabel('Green');
% zlabel('Blue');
% 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % [IMPORTANT]
% Gaussian Mixture Model
% Now choose you model type and estimate the parameters (mu and Sigma) from
% % the sample data.
% %
% D = 3;
% X = double(Samples);
% mu = mean(X);
% s = size(Samples);
% Sigma = cov(X);
% p = zeros(s(1), 1);
% for n = 1:s(1)  
%    x = X(n, :); 
%    p(n) = (1/((2*pi)^(D/2)*det(Sigma)^0.5))*exp(-0.5*(x - mu) * (Sigma\(x - mu)'));
% end



