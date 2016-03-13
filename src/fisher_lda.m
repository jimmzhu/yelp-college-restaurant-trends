function [discriminants, varargout] = fisher_lda( x_train, y_train, varargin )

[n, d] = size(x_train);
x_by_label = cell(1, 2);
for label = 0:1
  x_by_label{label+1} = x_train(y_train == label,:);
end

gamma = 0.01;

lda_pairs = { [1 2] };
discriminants = zeros(d, length(lda_pairs));

for i = 1:length(lda_pairs)
  lda_pair = lda_pairs{i};
  x_0 = x_by_label{lda_pair(1)};
  x_1 = x_by_label{lda_pair(2)};
  mu_0 = mean(x_0)';
  mu_1 = mean(x_1)';

  if nargin > 2 && isequal(varargin{1}, 'sparse')
    var_0 = var(x_0)';
    var_1 = var(x_1)';
    discriminant_diagonal = (mu_1 - mu_0).^2 ./ (var_0 + var_1);
    mean_discriminant_magnitude = mean(abs(discriminant_diagonal));
    nonzero_indices = abs(discriminant_diagonal) > mean_discriminant_magnitude;

    mu_0 = mu_0(nonzero_indices);
    mu_1 = mu_1(nonzero_indices);
    Sigma_0 = cov(x_0(:, nonzero_indices));
    Sigma_1 = cov(x_1(:, nonzero_indices));
    Sw = Sigma_0 + Sigma_1 + gamma*eye(sum(nonzero_indices));
    [~, ~, V] = svd(Sw \ (mu_1 - mu_0)*(mu_1 - mu_0)');
    discriminants(nonzero_indices,i) = V(:,1);

    varargout{1} = discriminant_diagonal;
    disp(sum(nonzero_indices));
  else
    Sigma_0 = cov(x_by_label{lda_pair(1)});
    Sigma_1 = cov(x_by_label{lda_pair(2)});
    Sw = Sigma_0 + Sigma_1 + gamma*eye(d);
    [~, ~, V] = svd(Sw \ (mu_1 - mu_0)*(mu_1 - mu_0)');
    discriminants(:,i) = V(:,1);
  end
end
