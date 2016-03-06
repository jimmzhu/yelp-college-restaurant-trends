function [ dim , T , oppOrNah ] = findUMin_stumps( data , labels , weights )
%findUMin_stumps Return the function (or the function evaluated at each
%point), such that
%       - We only consider decision stumps
%       - We minimize the sum of all weights that are classified as NOT
%       within our class of interest
%       - Only consider the set of decision functions which is the decision
%       stumps
% Inputs:
%   data:    A matrix of data where each column is an observation
%   labels:  Labels for the associated data where there are 1's wherever the
%            desired class is and 0's otherwise.
%   weights: An array of weights associated with ALL of the datapoints.
% Outputs:
%   T: The final threshold that achieved the minimum sum.
%   oppOrNah: Whether or not we chose the opposite polarity stump (true) or the
%   true one (false)


%Create arrays to store the sum of weights associated with each weak learner (stumps)
sum_wl     = []; %If this is for all u's
sum_wl_opp = []; %Then this is for all -u's

N = 100;
J = size(data,1); %Number of dimensions stored at J

for i = 0 : N
   
    t = i / (2*N) ; %Threshold is defined as such!
    
    for j = 1 : J
        
        %Apply this rule to each of the dimensions in data.
        
        weakL = (data(j,:) >= t)' + (-1) * (data(j,:) < t )'; %This is the
        %true classification.
        
        %But for calculation purposes we want to only focus on summing the
        %weights for things that are NOT properly classified.
        
        sum_wl(j,i+1)     = weights' * (weakL ~= labels);
        sum_wl_opp(j,i+1) = weights' * (weakL == labels);
        
    end
    
end

concat_sums = [sum_wl sum_wl_opp ] ;

%Find the minimum sum in both arrays.

[ min_sum min_ind ] = min( min( concat_sums ) );

% %min_ind will be the column that contained the smallest number.
% %Make sure that the columns are each corresponding to i so we can easily
% %extract the threshold.
% 
% T = (min_ind - 1 )/50;
% 
% %If the index is in the first 51 columns, then it was in the first matrix
% %"sum_wl" which means it WAS NOT the opposite one.
% oppOrNah = ( min_ind > 51 ); 

%Obtain the exact column and row for our purposes.
indMat_columns = repmat( [ 1 : size( concat_sums , 2 ) ] , size( concat_sums , 1 ) , 1 );
indMat_rows    = repmat( [ 1 : size( concat_sums , 1 ) ]' , 1 , size( concat_sums , 2 ));

min_j = indMat_rows( concat_sums == min_sum );
min_t_indexes = indMat_columns( concat_sums == min_sum );

%If the above returns multiple indexes, then we will take just one!
min_t_ind = min_t_indexes(1);

if( min_t_ind(1) > (N+1) )
    min_t = (min_t_ind - (N + 1) - 1)/(2*N);
else
    min_t = (min_t_ind - 1)/(2*N);
end

%Create outputs
T        = min_t(1);
dim      = min_j(1);
oppOrNah = min_t_ind(1) > (N+1) ;

%Can finally construct the weak learner that minimizes the desired sum.

disp( [ 'Threshold chosen: ' num2str( min_t(1) ) ', Desired Dim: ' num2str( min_j(1) ) ] )

end

