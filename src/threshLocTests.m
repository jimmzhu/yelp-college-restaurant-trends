%ECE 271B Project Observing P_Error when the Threshold is assumed to change.


clear all;
close all;
clc;

%% Import CSV Data

tr_data   = (csvread( '../data/businesses-train.csv'))';

test_data = (csvread( '../data/businesses-test.csv'))';

num_tr_samples   = size(tr_data,2);
num_test_samples = size( test_data,2);

%Notes: Each business (column or tr_data and test_data) ...
%		- First 9 entries are top 3 check in time data where peak check in data is formatted as(day,hour,number of check ins )
%		- Next 251 entries are 1 hot encoding of the categories involved.
%		- Final entry contains distance in longitude-lattitude of a given business to the nearest college

%% Labelling

mean_dist_to_college = tr_data(end,:) * ( 1/size(tr_data,2) ) * ones( size( tr_data , 2 ) , 1 );

tr_pError = [];
test_pError = [];

%Debugging sign error
sign_correctQ = [];

x = tr_data( [1 : end-1], : );
z = test_data( [1 : end-1], : );

for th_exp = [ -1 : 0.01 : 2 ]

	%Assign labels based on the threshold we choose.
	thresh = 10^th_exp;

	%Place 1 if we are close to a college, -1 otherwise
	tr_labels 	= ( tr_data(end,:) <= thresh ) + (-1)*( tr_data(end,:) > thresh );
	test_labels = ( test_data(end,:) <= thresh ) + (-1)*( test_data(end,:) > thresh );

	%% LDA

	% separate class 1 and class 2 data

	x1 = x( : , tr_labels == 1 );
	x2 = x( : , tr_labels == -1 );

	% Means and covariances.

	% mu1 = (1/size(x1,2)) * x1 * ones( size(x1,2),1);
	% mu2 = (1/size(x2,2)) * x2 * ones( size(x2,2),1);

	% cov1 = ( 1 / size(x1,2)) * ( x1 - repmat( mu1 , 1 , size( x1 , 2 ) ) ) * ( x1 - repmat( mu1 , 1 , size( x1 , 2 ) ) )';
	% cov2 = ( 1 / size(x2,2)) * ( x2 - repmat( mu2 , 1 , size( x2 , 2 ) ) ) * ( x2 - repmat( mu2 , 1 , size( x2 , 2 ) ) )';

	mu1 = mean( x1 , 2 );
	mu2 = mean( x2 , 2 );

	cov1 = cov( x1' , 1);
	cov2 = cov( x2' , 1);

	% Rayleigh Eigenvector Matrices

	S_B = (mu2 - mu1) * ( mu2 - mu1 )';

	S_W = cov1 + cov2;

	%S_W is not invertible unfortunately. :'(
	%Introduce a regularization to get an invertible and solvalble form of our problem.

	gamma = 10^(-1);

	[ rayleigh_eVec rayleigh_eVal ] = eig( (S_W + gamma * eye( size(S_W))) \ S_B );

	[ max_rEVal max_rEVal_ind ] = max( diag( rayleigh_eVal ) );

	%Linear Discriminant should be easily 
	f_lin_discr = rayleigh_eVec(:,max_rEVal_ind);

	check_sign = sign( f_lin_discr' * mu2 - f_lin_discr'*( mu2 + mu1)/2 );

	%Check the sign of our linear discriminant. And fix it if it is pointing opposite of the way we need it to.
	if check_sign == -1 
		f_lin_discr = -f_lin_discr;
	end

	%Calculate classification results on training and test_data.
	y = f_lin_discr' * ( x - repmat( ( mu2+mu1 )/2 , 1 , size( x , 2 ) ) );

	y2 = f_lin_discr' * ( z - repmat( ( mu2+mu1 )/2 , 1 , size( z , 2 ) ) );

	sign_correctQ = [ sign_correctQ sign( f_lin_discr' * mu2 + f_lin_discr'*( mu2 + mu1)/2 ) ];

	%Probability of Error

	%Be careful here, because the labels are constructed the OPPOSITE of how the lin. discr. was constructed.
	%For example, tr_labels =1 when the point is in class mu1, which would in fact be when y < 0!
	tr_pError = [ tr_pError sum( ( (y < 0) + (-1)*(y>=0) ) ~= tr_labels )/length(tr_labels) ];  
	test_pError = [ test_pError sum( ( (y2 < 0) + (-1)*(y2>=0) ) ~= test_labels )/length(test_labels) ];
end

th_exp = [ -1 : 0.01 : 2 ];
x_axis = 10.^th_exp;

figure;
semilogx(x_axis, tr_pError);
hold on;
semilogx(x_axis, test_pError,':');

legend('Training','Test')

xlabel('Threshold Value')
ylabel('P_E_r_r_o_r')