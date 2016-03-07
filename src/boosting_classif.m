%ECE 271B Project Using Boosting on our data.


clear all;
close all;
clc;

%% Import CSV Data

tr_data   = (csvread( '../data/businesses-train.csv'))';

test_data = (csvread( '../data/businesses-test.csv'))';

num_tr_samples   = size(tr_data,2);
num_test_samples = size( test_data,2);

%Notes: Each business (column or tr_data and test_data) ...
%		- First 56 entries are top 3 check in time data where peak check in data is formatted as(day,hour,number of check ins )
%		- Next 251 entries are 1 hot encoding of the categories involved.
%		- Final entry contains distance in longitude-lattitude of a given business to the nearest college

%% Labelling

mean_dist_to_college = tr_data(end,:) * ( 1/size(tr_data,2) ) * ones( size( tr_data , 2 ) , 1 );

%thresh = 263;

tr_pError = [];
test_pError = [];

%Choosing all of data or subset
chooseCheckInsOnly = false;

if ~chooseCheckInsOnly
	x = tr_data( [1 : end-1], : );
	z = test_data( [1 : end-1], : );
end

if chooseCheckInsOnly
	x = tr_data( [ 1 : 56] , : );
	z = test_data( [ 1 : 56 ] , :);
end
%% Adaboost

%Loop over this for multiple different thresholds.

th_ind = 0;

final_tr_errors = [ ] ;
final_test_errors = [ ];

%Optimal threshold given according to our 

thresh = 2;

%=================================================
%Prepare Adaboost Boosting Variables for iteration
g_x = zeros(size(x,2),1); %Assume that function assumes everything is NOT Class '0' first.
g_test = zeros( size(z,2),1);

%Place 1 if we are close to a college, -1 otherwise
tr_labels 	= ( tr_data(end,:) <= thresh ) + (-1)*( tr_data(end,:) > thresh );
test_labels = ( test_data(end,:) <= thresh ) + (-1)*( test_data(end,:) > thresh );

y  = tr_labels';
y2 = test_labels';

R_emp = ones(1 , size(tr_data,2) ) * exp( - y .* g_x ) ;

endLoop = false;
loopNum = 0;

margins = [];

boosting_iter = 250;

%Stump Function Variables.
stumpThresh = 0;
stumpDim    = 0;
stumpOpp    = false;

while( ~endLoop )

	%Calculate weights
	weights = exp( - y .* g_x );

	%Find the function u that minimizes the sum of all weights!
	[ stumpDim stumpThresh stumpOpp ] = findUMin_stumps( x , y , weights );

	min_wl = applyStumps( stumpDim , stumpThresh , stumpOpp , x  );
	min_testsWL = applyStumps( stumpDim , stumpThresh , stumpOpp , z );

	%Compute step size
	epsil0 = ( weights' * ( y ~= min_wl ) ) / ( weights' * ones(size(weights)) );
	w_t = (1/2) * log( (1-epsil0)/epsil0 );

	%epsil_test = ( weights' * ( y_te ~= min_testsWL ) ) / ( weights' * ones(size(weights)) )

	%Update the learned function
	g_x = g_x + w_t * min_wl;
	g_test = g_test + w_t * min_testsWL;

	%Loop Updates
	loopNum = loopNum + 1;
	R_emp(loopNum+1) = ones(1 , size(tr_data,2) ) * exp( - y .* (g_x) ) ;

	disp( [ 'Finished ' num2str( loopNum ) ' Loops.' ] ) %Visual confirmation.

	%SAVING
	%Save the margins at certain iteration numbers.
	if( ( loopNum == 5 ) || ( loopNum == 10 ) || ( loopNum == 50 ) || ( loopNum == 100 ) || ( loopNum == 250 ) )
		margins = [ margins y.*g_x ];
	end

	%Saving the largest weight at each iteration.
	[ ignoreValue largestWght_at(loopNum)] = max( weights );

	%Saving Training Error and Test Error of Each Iteration.
	tr_err(loopNum)     = sum( y ~= sign(g_x) ) / length(y);
	test_error(loopNum) = sum( y2 ~= sign( g_test )) / length(y2);


	if( loopNum == boosting_iter )
		endLoop = true;
	end

	% if( loopNum > 3 )
	% 	if( R_emp(loopNum) == R_emp(loopNum-1) )
	% 		endLoop = true;
	% 	end
	% end
end

%Update th_ind 

th_ind = th_ind+1;

disp('');
disp([ 'Finished ' num2str( th_ind ) ' Boosting Classifiers!' ])

final_tr_errors = [ final_tr_errors tr_err(end) ]
final_test_errors = [ final_test_errors test_error(end)]



figure;
plot(tr_err)
hold on;
plot(test_error)
xlabel('Iteration number')
ylabel('P_E_r_r_o_r')
title('P_E_r_r_o_r vs. Iteration # for Our Boosting algorithm w/ Decision Stumps')