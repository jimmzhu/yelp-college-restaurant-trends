function [ f_x ] = applyStumps( dim , thresh , oppOrNah , data )
%applyStumps Apply Stump Functions on a set of data
%   
%   Inputs:
%       dim: Dimension to which the function is applied.
%       thresh:   The threshold
%       oppOrNah: Flips sign of stumps result if true
%       data: input data, with each column being an observation

    f_x = ( data( dim , : )' >= thresh) + (-1) * ( data(dim,:)' < thresh );
    
    if( oppOrNah )
        f_x = -f_x;
    end

end

